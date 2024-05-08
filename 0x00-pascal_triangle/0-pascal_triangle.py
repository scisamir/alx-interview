#!/usr/bin/python3
"""
Factorial Algorithm
"""


def _factorial(n):
    """ Returns the Factorial of a number, n """
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact


"""
Pascal's Triangle Algorithm
"""


def pascal_triangle(n):
    """ Returns a list of lists representing a pascal's triangle """
    my_list = []

    if n <= 0:
        return my_list

    for y in range(n):
        new_list = []

        for x in range(y + 1):
            new_val = _factorial(y) // (_factorial(y - x) * _factorial(x))
            new_list.append(new_val)

        my_list.append(new_list)

    return my_list
