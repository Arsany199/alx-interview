#!/usr/bin/python3
"""model minimum number of operations"""


def minOperations(n):
    """function to get the minimum number of operations needed to
    result in exactly n H char"""
    if not isinstance(n, int):
        return (0)
    oper = 0
    iterate = 2
    while (iterate <= n):
        if not (n % iterate):
            n = int(n / iterate)
            oper += iterate
            iterate = 1
        iterate += 1
    return (oper)
