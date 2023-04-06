#!/usr/bin/env python3
"""
This module contains the Poisson class
"""


class Poisson:
    """
    Represents a Poisson distribution
    """

    def __init__(self, data=None, lambtha=1.):
        """Poisson class constructor"""
        self.lambtha = float(lambtha)

        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """Calculates the value of the PMF for a given number of “successes”"""
        if not isinstance(k, int):
            k = int(k)

        if k < 0:
            return 0

        factorial_k = 1
        for i in range(1, k+1):
            factorial_k *= i

        pmf_value = ((e ** -self.lambtha) * (self.lambtha ** k)) / factorial_k
        return pmf_value

    def cdf(self, k):
        """Calculates the value of the CDF for a given number of successes"""
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0
        cdf_value = 0
        for i in range(k + 1):
            cdf_value += self.pmf(i)
        return cdf_value
