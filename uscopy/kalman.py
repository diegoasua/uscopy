import numpy as np
from tqdm import tqdm


# TODO: Consider default cast to float64 if safe for increased precision
class KalmanDenoiser:
    """
    Main class for denoising via Kalman filtering.
    """

    _variance = 0.05
    _gain = 0.08

    @property
    def variance(self):
        return self._variance

    @variance.setter
    def variance(self, value):
        if not 0 < value <= 1:
            raise ValueError("Variance must be between 0 and 1.")
        self._variance = value

    @property
    def gain(self):
        return self._gain

    @gain.setter
    def gain(self, value):
        if not 0 < value <= 1:
            raise ValueError("Gain must be between 0 and 1.")
        self._gain = value

    # TODO: Speed up with numba, break up function
    def filter(self, stack: np.array) -> np.array:
        """
        Performs Kalman denoising of a 3D array (time, width, height)
        """
        assert len(stack) != 0, "Stack is empty."
        assert len(stack) != 1, "Stack must contain more than one element."
        stack = np.concatenate((stack, np.expand_dims(stack[-1], 0)))
        _, width, height = stack.shape

        previous = stack[0]
        predicted = np.tile(self._variance, (width, height))
        noise = predicted

        ones = np.ones((width, height))
        denoised = np.zeros_like(stack)

        for i_frame, frame in enumerate(tqdm(stack[1:])):
            estimate = predicted / (predicted + noise)
            corrected = (
                self._gain * previous
                + (1 - self._gain) * frame
                + estimate * (frame - previous)
            )

            predicted = predicted * (ones - estimate)
            previous = corrected
            denoised[i_frame] = corrected

        # get rid of extra frame at the end
        denoised = denoised[:-1]

        return denoised
