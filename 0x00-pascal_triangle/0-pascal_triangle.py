#!/usr/bin/python3
"""
Pascal's Triangle Algorithm
"""
from math import factorial

def pascal_triangle(n):
    """ Returns a list of lists representing a pascal's triangle """
    my_list = []

    if n <= 0:
        return my_list

    for y in range(n):
        new_list = []

        for x in range(y + 1):
            new_val = factorial(y) / (factorial(y - x) * factorial(x))
            new_list.append(int(new_val))

        my_list.append(new_list)

    return my_list
