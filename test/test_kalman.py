from uscopy.kalman import KalmanDenoiser
import numpy as np


stack = np.ones((10, 5, 5), dtype=np.uint16)
denoiser = KalmanDenoiser()
denoiser.gain = 0.5
denoiser.variance = 0.5
denoised = denoiser.filter(stack)
assert stack.shape == denoised.shape
