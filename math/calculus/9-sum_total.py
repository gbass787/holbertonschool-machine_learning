#!/usr/bin/env python3

def summation_i_squared(n):
    if not isinstance(n, int) or n <= 0:
        return None
    return sum(i ** 2 for i in range(1, n+1))
