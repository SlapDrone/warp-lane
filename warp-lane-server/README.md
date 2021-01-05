# warp-lane web server

Code for the warp-lane python web-server.

##  Install
Both of the following will create a python environment with the
warp_lane_server package installed in editable mode.

Must be run from this dir.

### Conda
Create a conda env from conda_env.yml:

```bash
conda env create -f conda_env.yml
```

### Pipenv
Use the Pipfile to create a virtual env from the Pipfile:

```bash
pipenv install
```

## Run

The server script is in `scripts/run_server.py`.
