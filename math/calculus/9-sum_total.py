#!/usr/bin/env python3
"""
task 9
"""


def summation_i_squared(n):
    """
    Calculates the summation of the squares of the first n natural numbers.

    Args:
    - n: an integer value indicating the stopping condition

    Returns:
    - an integer value representing the summation of
the squares of the first n natural numbers.
    - If n is not a valid number, return None.
    """
    if n > 0:
        return int(n*(n+1)*((2*n)+1)/6)
    return None
