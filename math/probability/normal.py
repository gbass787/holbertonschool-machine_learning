#!/usr/bin/env python3
"""
Normal distribution
"""


class Normal:
    """ class Normal """
    def __init__(self, data=None, mean=0., stddev=1.):
        """
        Normal distribution class.

        Args:
            data (list): A list of the data to be used to estimate the
                distribution.
            mean (float): The mean of the distribution.
            stddev (float): The standard deviation of the distribution.

        Sets the instance attributes:
            mean (float): The mean of the distribution.
            stddev (float): The standard deviation of the distribution.

        Raises:
            ValueError: If stddev is not a positive value and data is
                not given.
            TypeError: If data is not a list.
            ValueError: If data does not contain at least two data points.
        """
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = sum(data) / float(len(data))
            variance = sum([(x - self.mean) ** 2 for x in data]) \
                / float(len(data))
            self.stddev = variance ** 0.5
