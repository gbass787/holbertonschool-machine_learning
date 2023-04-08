#!/usr/bin/env python3

"""Binomial distribution class."""


class Binomial:
    """Binomial distribution class."""

    def __init__(self, data=None, n=1, p=0.5):
        """
        Initialize the binomial distribution.

        Parameters
        ----------
        data : list, optional
            List of data to estimate the distribution. Default is None.
        n : int, optional
            Number of Bernoulli trials. Default is 1.
        p : float, optional
            Probability of success. Default is 0.5.

        Raises
        ------
        ValueError
            If n is not a positive value or p is not a valid probability.
        TypeError
            If data is not a list.
        ValueError
            If data does not contain at least two data points.
        """
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if not (0 < p < 1):
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.n = round(sum(data) / len(data))
            self.p = sum(data) / (self.n * 1.0)
            self.n = int(self.n)
            self.p = float(self.p)
