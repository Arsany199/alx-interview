#!/usr/bin/python3
"""module to make Pascal's Triangle"""


def pascal_triangle(n):
    """Create a function def pascal_triangle(n) that represented in n"""
    result = []
    if n > 0:
        for i in range(1, n + 1):
            level = []
            c = 1
            for j in range(1, i + 1):
                level.append(c)
                c = c * (i - j) // j
            result.append(level)
    return result
