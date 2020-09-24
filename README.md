# Warp Lane

Experiment with Sanic, receiving, modifying and serving back audio files.

Install environment (requires [Anaconda](https://www.anaconda.com/products/individual)):

```bash
conda env create -f env.yml
conda activate warplane
```

Now run the server:

```bash
python server.py
```

Now, with a .wav file handy, [upload](http://0.0.0.0:8000/upload) it and listen to the result.

# Client

The first version of the client app is created using Angular and written in typescript. The code is contained in the folder "warp-lane-ng-client", see the README.md file within for further details.




