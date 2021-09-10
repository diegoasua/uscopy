from distutils.core import setup

from setuptools import find_namespace_packages

with open("requirements_dev.txt") as f:
    requirements_dev = f.read().splitlines()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

with open("README.md") as f:
    long_description = f.read()


setup(
    name="uscopy",
    version="0.1.0",
    author="Diego Asua",
    author_email="baxuaa@gmail.com",
    license="MIT",
    packages=find_namespace_packages(exclude=("tests*")),
    install_requires=requirements,
    extras_require=dict(dev=requirements_dev),
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
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shohamlab/uscopy",
)
