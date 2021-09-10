from uscopy.kalman import KalmanDenoiser
import numpy as np
from tifffile import imread, imsave


stack = imread('/home/diego/Desktop/nyulangone/data/30hz_gcamp8f/ch1/JG7965_210831_field1_odor_00003_00005.tif')
denoiser = KalmanDenoiser()
denoiser.gain = 0.75
denoiser.variance = 0.5
denoised = denoiser.filter(stack)
imsave(
    f'/home/diego/Desktop/nyulangone/data/30hz_gcamp8f/ch1/denoised_gain_{denoiser.gain}_variance{denoiser.variance}.tif',
    denoised
)
