#!/usr/bin/env python3

"""
adds two arrays element-wise.
"""


def add_arrays(arr1, arr2):
    """
    Parameters:
    - arr1 (list of int/float): The first array.
    - arr2 (list of int/float): The second array.

    Returns:
    - A new list containing the element-wise sum of arr1 and
arr2, or None if arr1 and arr2 are not the same shape.
    """
    if len(arr1) != len(arr2):
        return None
    else:
        result = []
        for i in range(len(arr1)):
            result.append(arr1[i] + arr2[i])
        return result
