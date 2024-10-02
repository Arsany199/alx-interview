#!/usr/bin/python3
"""module for the prime game"""


def isWinner(x, nums):
    """function that determine winner in prime game session in some rounds"""
    if x < 1 or not nums:
        return None
    marias_win = 0
    bens_win = 0
    n = max(nums)
    isprimes = [True for _ in range(1, n + 1, 1)]
    isprimes[0] = False
    for i, is_prime in enumerate(isprimes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            isprimes[j - 1] = False
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, isprimes[0: n])))
        bens_win += primes_count % 2 == 0
        marias_win += primes_count % 2 == 1
    if marias_win == bens_win:
        return None
    elif marias_win > bens_win:
        return "Maria"
    elif bens_win > marias_win:
        return "Ben"
