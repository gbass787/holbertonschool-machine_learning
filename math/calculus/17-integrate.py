#!/usr/bin/env python3
"""
def poly_integral
"""


def poly_integral(poly, C=0):
    """
    Calculates the integral of a polynomial.
    Args:
    - poly: a list of coefficients representing a polynomial.
    - C: an integer representing the integration constant (default=0).
    Returns:
    - a new list of coefficients representing the integral of the polynomial.
    - If poly or C are not valid, return None.
    """
    if not isinstance(poly, list) or not isinstance(C, int):
        return None
    if len(poly) == 0:
        return [C]
    if not all(isinstance(c, (int, float)) for c in poly):
        return None
    integral = [C]
    for i in range(len(poly)):
        coef = poly[i] / (i + 1)
        if coef.is_integer():
            integral.append(int(coef))
        else:
            integral.append(coef)
    while integral[-1] == 0 and len(integral) > 1:
        integral.pop()
    return integral
