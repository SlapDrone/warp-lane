import os

# import io
from setuptools import find_packages, setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="warplane",
    version="0.1",
    description="Computer vision tools for semantic segmentation on rasters",
    author="Liam R. Moore, Lies Melville",
    packages=find_packages(
        exclude=["tests", "media", "docs", "notebooks", "bin", "static"]
    ),
    long_description=read("README.md"),
)
