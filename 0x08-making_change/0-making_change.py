#!/usr/bin/python3
"""making change module"""


def makeChange(coins, total):
    """Determines the min. num. of coins needed to meet given amount"""
    if total <= 0:
        return 0

    remaining = total
    count = 0
    idx = 0
    sort = sorted(coins, reverse=True)
    n = len(coins)
    while remaining > 0:
        if idx >= n:
            return -1
        if remaining - sort[idx] >= 0:
            remaining -= sort[idx]
            count = count + 1
        else:
            idx = idx + 1
    return (count)
