"""
Adapted from:

https://hackernoon.com/audio-handling-basics-how-to-process
-audio-files-using-python-cli-jo283u3y
"""
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from threading import RLock
from typing import List, Optional, Tuple, Union

import numpy as np
import soundfile
import warplane.audio_interface as au
import warplane.config as cfg
from sanic.log import logger
from scipy.io import wavfile

lock = RLock()
executor = ThreadPoolExecutor()
# TODO: this is just selecting one audio interface from the config.yml file ATM
interface_input = au.get_input_interface(cfg.interface_input_id)  # type: ignore
interface_output = au.get_output_interface(cfg.interface_output_id)  # type: ignore
channels_input = cfg.interface_input_channels  # type: ignore
channels_output = cfg.interface_output_channels  # type: ignore


def read_wav_file(
    wav_file: Union[str, Path], normalise: bool = True
) -> Tuple[np.ndarray, int, int]:
    """
    Read a wav file, returning the raw numpy array and sample rate/bit depth

    Parameters
    ----------
    wav_file:
        path to a wav file
    normalise:
        boolean flag to norm to [0,1] by dividing by bit depth

    Returns
    -------
    A tuple of (numpy array, sample rate, bit depth) for selected file
    """
    bit_depth = int(soundfile.SoundFile(wav_file).subtype.split("_")[-1])
    sample_rate, wav_arr = wavfile.read(wav_file)
    if normalise:
        wav_arr = wav_arr / 2 ** (bit_depth - 1)
    return wav_arr, sample_rate, bit_depth


def pass_through_interface(
    wav_arr: np.ndarray,
    interface_output=interface_output,
    interface_input=interface_input,
    sample_rate: int = 44_100,
    interface_input_channels: List[int] = channels_input,
    interface_output_channels: List[int] = channels_output,
    input_blocksize: int = 128,
    output_blocksize: int = 128,
    record_grace_factor: float = 1.05,
    executor=None,
    lock: Optional[RLock] = None,
) -> np.ndarray:
    """
    Plays wav file through audio interface and records interface's inputs.

    Ideal for passing audio through external hardware and recapturing it.

    Parameters
    ----------
    wav_arr:
        Numpy array of audio signal of shape (samples, channels)
    interface_output:
        soundcard output ("speaker") object
    interface_input:
        soundcard input ("microphone") object
    sample_rate:
        sampling rate of audio signal in Hz
    interface_input_channels:
        which input channels to record on interface
    interface_output_channels:
        which output channels on interface to play audio array through
    input_blocksize:
        recording sample buffer size
    output_blocksize:
        playback sample buffer size
    record_grace_factor:
        multiplicative factor for time which to record relative to original
    executor:
        a threading :obj:`ThreadPoolExecutor` object to enable simulatenous
        playback/recording
    lock:
        a :obj:`threading.RLock` to reserve the soundcard. May need to
        extend this to cover processes too.

    Returns
    -------
    np.ndarray:
        the captured selected inputs on the soundcard corresponding to the
        period the audio was played through the selected outputs
    """
    assert wav_arr.shape[1] <= 2, "Only mono/stereo audio supported ATM!"
    if executor is None:
        if False:  # app.cfg.STRICTLY_ONE_EXECUTOR:
            raise ValueError("Need to pass a specific ThreadPoolExecutor!")
        executor = ThreadPoolExecutor()
    if lock is None:
        raise ValueError(
            "Pass a threading.RLock instance to co-ordinate reservation of sound card!"
        )
    # block access to soundcard for other threads
    with lock:
        logger.debug("Lock acquired.")
        logger.info("Playing/recording file through audio interface...")
        with interface_input.recorder(
            samplerate=sample_rate,
            channels=interface_input_channels,
            blocksize=input_blocksize,
        ) as input_, interface_output.player(
            samplerate=sample_rate,
            channels=interface_output_channels,
            blocksize=output_blocksize,
        ) as output_:
            # decide length of recording: input length * grace factor to allow for latency correction
            n_frames_record = int(wav_arr.shape[0] * record_grace_factor)
            logger.info("Playing/recording file through audio interface...")
            # start recording in one thread and immediately start playing in another
            data = executor.submit(input_.record, numframes=n_frames_record)
            executor.submit(output_.play, wav_arr)
            # halt for the time taken for the sample to play/record
            time.sleep(n_frames_record / sample_rate)
            # obtain array from future
            mod_wav_arr = data.result()
    logger.debug("Lock released.")
    return mod_wav_arr


def capture_audio_and_save(
    in_file: Path,
    out_dir: Path,
    interface_output=interface_output,
    interface_input=interface_input,
    interface_input_channels: List[int] = channels_input,
    interface_output_channels: List[int] = channels_output,
    input_blocksize: int = 128,
    output_blocksize: int = 128,
    record_grace_factor=1.05,
    executor=executor,
    lock=lock,
) -> Path:
    """
    Play a wav file through the selected output channels on
    a given audio interface and listen to the input on the
    selected input channels.
    """
    wav_arr, sample_rate, bit_depth = read_wav_file(in_file)
    mod_wav_arr = pass_through_interface(
        wav_arr,
        interface_output=interface_output,
        interface_input=interface_input,
        sample_rate=sample_rate,
        interface_input_channels=interface_input_channels,
        interface_output_channels=interface_output_channels,
        input_blocksize=input_blocksize,
        output_blocksize=output_blocksize,
        record_grace_factor=record_grace_factor,
        executor=executor,
        lock=lock,
    )
    out_name = Path(in_file.parts[-1][:-4] + "_modified.wav")
    out_file = out_dir / out_name
    logger.info(f"Writing modified audio to {out_file}...")
    wavfile.write(out_file, sample_rate, mod_wav_arr)
    return out_file


def invert_wav_file(in_file: Path, out_dir: Path):
    fs_wav, wav_arr = wavfile.read(in_file)
    out_name = Path(in_file.parts[-1][:-4] + "_backwards.wav")
    out_file = out_dir / out_name
    logger.info(f"Writing to {out_file}...")
    wavfile.write(out_file, fs_wav, wav_arr[::-1])
    return out_file
