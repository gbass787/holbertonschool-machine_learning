#!/usr/bin/env python3

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
    if not isinstance(n, int) or n <= 0:
        return None
    return sum(i ** 2 for i in range(1, n+1))
