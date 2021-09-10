# uscopy

uscopy (pronounced *microscopy*) is a set of tools for routine analysis of bioimaging time-series data. 

You can build this package from source with pip:

```bash
cd <path_to_uscopy>
pip install .
```

# Usage


```python
from uscopy.kalman import KalmanDenoiser
from tifffile import imread

stack = imread(...)
denoiser = KalmanDenoiser()
denoiser.gain = 0.75
denoiser.variance = 0.5
denoised = denoiser.filter(stack)
```