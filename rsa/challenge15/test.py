from random import randrange
from math import gcd


def ned_to_pq(n, e, d):
    """
    https://crypto.stanford.edu/~dabo/papers/RSA-survey.pdf#:~:text=Given%20d%2C,reveals%20the%20factorization%20of%20N%2E
    """
    k = d * e - 1
    t = bit_scan1(k)
    while True:
        g = randrange(2, n - 1)
        for j in range(1, t + 1):
            x = pow(g, k >> j, n)
            if x == 1: continue  # trivial
            if pow(x, 2, n) == 1:
                a = gcd(x - 1, n)
                b = gcd(-x - 1, n)
                p, q = sorted([a, b])
                return p, q


def bit_scan1(i):
    return (i & -i).bit_length() - 1


