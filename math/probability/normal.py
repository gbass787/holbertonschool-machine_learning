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

    def z_score(self, x):
        """
        Calculates the z-score of a given x-value.

        Args:
            x (float): The x-value for which to calculate the z-score.

        Returns:
            The z-score of x.
        """
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """
        Calculates the x-value of a given z-score.

        Args:
            z (float): The z-score for which to calculate the x-value.

        Returns:
            The x-value of z.
        """
        return z * self.stddev + self.mean

    def pdf(self, x):
        """
        Calculates the value of the PDF for a given x-value.

        Args:
            x (float): The x-value for which to calculate the PDF.

        Returns:
            The value of the PDF for the given x-value.
        """
        factor1 = 1 / (self.stddev * ((2 * 3.14159265359) ** 0.5))
        factor2 = 2.71828182846 ** (
            -0.5 * ((x - self.mean) / self.stddev) ** 2)
        return factor1 * factor2
