#!/usr/bin/env python3
"""
def poly_derivative(poly) function
"""


def poly_derivative(poly):
    """
    Calculates the derivative of a polynomial.

    Args:
    - poly: a list of coefficients representing a polynomial
        the index of the list represents the power of x
that the coefficient belongs to
        Example: if f(x) = x^3 + 3x + 5, poly is equal to [5, 3, 0, 1]

    Returns:
    - a new list of coefficients representing the derivative of the polynomial

    If poly is not valid, return None.
    If the derivative is 0, return [0].
    """

    if not isinstance(poly, list) or len(poly) == 0:
        return None

    if len(poly) == 1:
        return [0]

    derivative = []
    for i in range(1, len(poly)):
        coefficient = poly[i] * i
        derivative.append(coefficient)

    if len(derivative) == 0:
        return [0]

    return derivative
