# Setup

## ALSAAudio

It's worth noting that I had to update my base conda environment to include
python 3.8 and install 'pyalsaaudio' there via PyPI before this conda env would 
build. Without this, there was some issue with the underlying C library not 
being correctly linked.