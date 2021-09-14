# uscopy

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://img.shields.io/github/workflow/status/shohamlab/uscopy/tests)](
    https://github.com/shohamlab/uscopy/actions)
[![Coverage Status](https://coveralls.io/repos/github/shohamlab/uscopy/badge.svg?branch=master)](https://coveralls.io/github/shohamlab/uscopy?branch=master)

uscopy (pronounced *microscopy*) is a set of tools for routine analysis of bioimaging time-series data. 

You can build this package from source with pip:

```bash
cd <path_to_uscopy>
pip install .
```

# Usage


```python
from uscopy.kalman import KalmanDenoiser


denoiser = KalmanDenoiser()
denoiser.gain = 0.75
denoiser.variance = 0.5
denoised = denoiser.filter(stack)
```