#!/usr/bin/env python3
"""
This module defines the Exponential class, which represents
an exponential distribution.
"""


class Exponential:
    def __init__(self, data=None, lambtha=1.):
        """
        Initializes an instance of the Exponential class.

        Args:
            data (list): A list of data points used to estimate the
distribution. Defaults to None.
            lambtha (float): The expected number of occurrences in a
given time frame. Defaults to 1.

        Attributes:
            lambtha (float): The expected number of occurrences in
a given time frame.

        Raises:
            ValueError: If lambtha is not a positive value and data
is not given.
            TypeError: If data is not a list.
            ValueError: If data does not contain at least two data points.
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = 1 / (sum(data) / float(len(data)))
