from functools import reduce
import math


def inv(k1, k2):
    if (math.gcd(k1, k2) != 1):
        print("Ce nombre n'est pas inversible")
    else:
        for i in range(k2):
            if ((k1*i) % k2 == 1):
                return i


def premier(p):
    # Fonction qui permet de savoir si p est premier ou non
    bol, j = True, 0
    for i in range(2, int(p)+1):
        a = p % i
        if (a == 0):
            j += 1
    if (j >= 2):
        return False
    else:
        return True


def residu_quadratique(a, p):
    listResidu = []
    while not premier(p):
        p = input('Entrer un nombre premier')
    listResidu = [i for i in range(1, p) if ((i**2) % p == a)]
    # "{} n'est pas residu quadratique  modulo {}".format(a,p)
    return listResidu if len(listResidu) >= 1 else False


def symbole_legendre(a, p):
    if (residu_quadratique(a, p)):
        return 1
    elif (a % p == 0):
        return 0
    else:
        return -1


def symbole_jacolbi(a, m):
    if (premier(m)):
        return symbole_legendre(a, m)
    else:
        divM, numberdivM = [i for i in range(2, m) if m % i == 0], 1
        for i in range(len(divM)):
            numberdivM *= divM[i]
            if (numberdivM == m):
                divM = divM[:i+1]
                break
        return reduce(lambda x, y: x*y, [symbole_legendre(a, i) for i in divM])


def addition_P(P1: tuple(), P2: tuple(), a, b, n):
    if (P1 == P2):
        D = ((3*(P1[0])**2 + a)*(inv((2*P1[1]) % n, n))) % n
    else:
        if (P1[0] == P2[0]):
            D = 0
        else:
            D = ((P2[1]-P1[1])*inv((P2[0]-P1[0]) % n, n)) % n

    x3 = (D**2-P1[0]-P2[0]) % n
    y3 = (D*(P1[0]-x3)-P1[1]) % n

    return (x3, y3)


def inv_P(P: tuple(), n):
    return (P[0], -P[1] % n)


def k_P(k: int(), P: tuple(), a, b, n):
    Q = tuple()
    for elt in list(bin(k)[2:]):
        if (Q != ()):
            Q = addition_P(Q, Q, a, b, n)
        if (elt == '1'):
            if (Q == ()):
                Q = P
            else:
                Q = addition_P(Q, P, a, b, n)
    return Q


def ord_P(P: tuple(), a, b, n):
    P2, i = P, 2
    Pinv = (P[0], -P[1] % n)
    while (P2 != Pinv):

        P2 = addition_P(P2, P, a, b, n)
        i += 1
    return i
