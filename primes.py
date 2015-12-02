import math


def primes(n):
    """
    Find all primes less than n.

    >>> primes(3)
    [2]
    >>> primes(15)
    [2, 3, 5, 7, 11, 13]
    """
    candidates = [True] * n
    candidates[0] = candidates[1] = False
    for i in range(n):
        if candidates[i]:
            for j in range(2 * i, n, i):
                candidates[j] = False
    return [i for (i, c) in enumerate(candidates) if c]

print "Primes below 20:", ", ".join(map(str, primes(20)))
