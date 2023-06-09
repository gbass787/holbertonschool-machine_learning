#!/usr/bin/env python3
"""
Exponential
"""


class Exponential:
    """
    Exponential Class
    """

    def __init__(self, data=None, lambtha=1.):
        """
        Represents an exponential distribution.
        Args:
            data (list): A list of the data to be used to estimate
                the distribution.
            lambtha (float): The expected number of occurrences in
                a given time frame.
        Sets the instance attribute:
            lambtha (float): The expected number of occurrences in a
                given time frame.
        Raises:
            ValueError: If lambtha is not a positive value and data is
                not given.
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

    def pdf(self, x):
        """
        Calculates the value of the PDF for a given time period.

        Args:
            x (float): The time period.

        Returns:
            float: The PDF value for x.

        """
        if x < 0:
            return 0
        return self.lambtha * pow(2.7182818285, -1 * self.lambtha * x)

    def cdf(self, x):
        """
        Cumulative Distribution Function
        """
        if x < 0:
            return 0
        return 1 - pow(2.7182818285, -self.lambtha * x)
