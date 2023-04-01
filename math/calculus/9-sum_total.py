#!/usr/bin/env python3

def summation_i_squared(n):
    """
    Calculates the sum of the squares of the first n positive integers.

    Args:
    - n: an integer representing the stopping condition

    Returns:
    - an integer representing the sum of the squares of the first n positive integers,
      or None if n is not a positive integer
    """
    if not isinstance(n, int) or n <= 0:
        return None
    return int(n * (n + 1) * (2 * n + 1) / 6)
