#!/usr/bin/python3
"""making change module"""


def makeChange(coins, total):
    """Determines the min. num. of coins needed to meet given amount"""
    if total <= 0:
        return 0

    myremaining = total
    mycount = 0
    idx = 0
    sort = sorted(coins, reverse=True)
    n = len(coins)
    while myremaining > 0:
        if idx >= n:
            return -1
        if myremaining - sort[idx] >= 0:
            myremaining -= sort[idx]
            mycount = mycount + 1
        else:
            idx = idx + 1
    return (mycount)
