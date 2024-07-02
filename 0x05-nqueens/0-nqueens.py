#!/usr/bin/python3
"""model of the n queen problem"""
import sys

if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

n = int(sys.argv[1])


def find(n, i=0, x=[], y=[], z=[]):
    """function to find the possible positions for the queen"""
    if i < n:
        for j in range(n):
            if j not in x and i + j not in y and i - j not in z:
                yield from find(n, i + 1, x + [j], y + [i + j], z + [i - j])
    else:
        yield (x)


def answer(n):
    """function to solve the n queen"""
    key = []
    i = 0
    for sol in find(n, 0):
        for s in sol:
            key.append([i, s])
            i = i + 1
        print(key)
        key = []
        i = 0


answer(n)
