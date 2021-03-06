import setuptools
from distutils.core import setup

# read the contents of README.md
from pathlib import Path

this_directory = Path(__file__).parent
with (this_directory / "readme.md").open(encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="scarpa",
    version="v0.1.1",
    description="Tools for signal decomposition",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Robert Guggenberger",
    author_email="robert.guggenberger@uni-tuebingen.de",
    url="https://github.com/translationalneurosurgery/tool-scarpa",
    download_url="git@github.com:translationalneurosurgery/tool-scarpa.git",
    license="MIT",
    packages=setuptools.find_packages(exclude=["test", "docs"]),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha ",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
    ],
)
