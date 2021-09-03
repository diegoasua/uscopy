class KalmanDenoiser:
    variance = 0.05
    gain = 0.08

    def run(self):
        pass

    def filter(self):
        pass

    def filter_rgb(self, parameter_list):
        """
        docstring
        """
        raise NotImplementedError

    def from_double(self, parameter_list):
        """
        docstring
        """
        raise NotImplementedError

    def to_double(self, parameter_list):
        """
        docstring
        """
        raise NotImplementedError