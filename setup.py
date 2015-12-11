import os
from setuptools import setup

setup(
    name="pyprogressbar",
    version="0.0.1",
    author="Gefu Tang",
    author_email="tanggefu@gmail.com",
    description=("pyprogressbar is a progress bar control for python"),
    long_description=open("README.md").read().strip() if os.path.exists(
        "README.md") else "",
    license="GPLv3",
    keywords="progress bar",
    url="https://github.com/primetang/pyprogressbar",
    packages=['pyprogressbar'],
    package_dir={'pyprogressbar': 'src'},
)
