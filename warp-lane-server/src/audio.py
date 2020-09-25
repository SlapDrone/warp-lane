"""
Adapted from:

https://hackernoon.com/audio-handling-basics-how-to-process
-audio-files-using-python-cli-jo283u3y
"""
import numpy as np
import plotly.graph_objs as go
import plotly

from pathlib import Path
from pydub import AudioSegment
from scipy.io import wavfile
from plotly.offline import init_notebook_mode
from sanic.log import logger


def invert_wav_file(in_file : Path, out_dir : Path):
    fs_wav, wav_arr = wavfile.read(in_file)
    out_name = Path(in_file.parts[-1][:-4] + '_backwards.wav')
    out_file = out_dir / out_name
    logger.info(f"Writing to {out_file}...")
    wavfile.write(out_file, fs_wav, wav_arr[::-1])
    return out_file