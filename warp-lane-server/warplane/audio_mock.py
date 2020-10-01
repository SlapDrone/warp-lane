from pathlib import Path
from sanic.log import logger
from scipy.io import wavfile


def invert_wav_file(in_file: Path, out_dir: Path) -> Path:
    fs_wav, wav_arr = wavfile.read(in_file)
    out_name = Path(in_file.parts[-1][:-4] + "_backwards.wav")
    out_file = out_dir / out_name
    logger.info(f"Writing to {out_file}...")
    wavfile.write(out_file, fs_wav, wav_arr[::-1])
    return out_file
