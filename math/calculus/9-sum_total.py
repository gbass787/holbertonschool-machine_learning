#!/usr/bin/env python3

def summation_i_squared(n):
"""
    Calculates the summation of i^2 for i from 1 to n.

    Parameters:
        n (int): The stopping condition for the summation. Must be a positive integer.

    Returns:
        int: The integer value of the summation.

        If n is not a valid number, returns None.
"""
    if not isinstance(n, int) or n <= 0:
        return None
    return sum(i ** 2 for i in range(1, n+1))
