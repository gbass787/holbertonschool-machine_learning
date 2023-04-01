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
    if type(poly) is not list:
        return None
    elif not poly:
        return None
    elif len(poly) == 0:
        return None
    elif type(C) is not int:
        return None
    elif poly == [0]:
        return [C]
    else:
        integral = []
        integral.append(C)
        for i in range(len(poly)):
            x = poly[i] / (i + 1)
            integral.append(int(x) if x.is_integer() else x)
        return integral
