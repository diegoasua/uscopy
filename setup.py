from distutils.core import setup
from setuptools import find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="uscopy",
    version="0.1.0",
    author="Diego Asua",
    author_email="baxuaa@gmail.com",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="imaging microscopy 2-photon time-series kalman",
    description="A set of tools for routine analysis of bioimaging time-series data.",
)
