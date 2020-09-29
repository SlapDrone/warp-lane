"""
config.py

Loads a configuration yaml file 'config.yml' in the parent directory, executes
logic on its content and makes its contents available to other modules
by importing this module as e.g.:

    >> import gim_cv.config as cfg
    >> print(cfg.data_path)

`config.yml` contains various paths which allow one to define which directories
are used for storing data, models and results.
"""

import logging
from pathlib import Path

import yaml

project_root_dir = Path(__file__).absolute().parent.parent
cfg_yml_path = project_root_dir / Path("config.yml")

assert cfg_yml_path.exists(), "config.yml missing from project directory!"

log = logging.getLogger(__name__)


def join(loader, node):
    """
    Function to handle joining paths in yaml file.

    When encountering '!join' tags, will treat subsequent items as
    a list of strings to be concatenated.

    Allows self-referencing paths like !join [\\*BASE_PATH, /subdirectory/]
    """
    seq = loader.construct_sequence(node)
    return "".join([str(i) for i in seq])


def verify_path_exists(path, raise_exc=True):
    """Check a path exists and raise a FileNotFoundError if not"""
    if not path.exists():
        msg = f"File {path} not found!"
        if raise_exc:
            raise FileNotFoundError(msg)
        # warn
        log.warning(msg)


# -----------------------------------------------------------------------------
# register the tag handler
yaml.SafeLoader.add_constructor(tag="!join", constructor=join)

# check file exists
log.debug("Loading configuration file...")

# load the yml file as a dict
with open(cfg_yml_path, "r") as f:
    try:
        _cfg = yaml.safe_load(f)
    except Exception as e:
        log.error(e)
        raise

# update the local namespace with the values in the config dict, enabling
# us to access them when importing this file as attributes `config.model` etc
locals().update(_cfg)
