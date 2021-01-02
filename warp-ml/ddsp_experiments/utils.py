import IPython.display as ipd
import numpy as np
from scipy.io import wavfile

DEFAULT_SAMPLE_RATE = 16_000


def play(array_of_floats, sample_rate=DEFAULT_SAMPLE_RATE):
    """
    Plays an audio array

    Parameters
    ----------
    array_of_floats:
        A 1D or 2D array-like container of float sound samples.
        Values outside of the range [-1, 1] will be clipped.
    sample_rate:
        Sample rate in samples per second.

    Returns
    -------
    An IPython audio widget to play in-memory audio file
    """
    # If batched, take first element.
    if len(array_of_floats.shape) == 2:
        array_of_floats = array_of_floats[0]
    normalizer = float(np.iinfo(np.int16).max)
    array_of_ints = np.array(
        np.asarray(array_of_floats) * normalizer, dtype=np.int16
    )
    with open("/tmp/audio.wav", "wb") as fp:
        wavfile.write(fp, sample_rate, array_of_ints)
    return ipd.Audio("/tmp/audio.wav", rate=sample_rate)
