from uscopy.kalman import KalmanDenoiser
import numpy as np
from tifffile import imread, imwrite
from pathlib import Path


path_stack = Path('/home/diego/Desktop/nyulangone/data/30hz_gcamp8f/ch1/JG7965_210831_field1_odor_00003_00005.tif')
stack = imread(path_stack)
denoiser = KalmanDenoiser()
denoiser.gain = 0.5
denoiser.variance = 0.5
denoised = denoiser.filter(stack)
imwrite('/home/diego/Desktop/nyulangone/data/30hz_gcamp8f/ch1/denoised.tif', denoised)
