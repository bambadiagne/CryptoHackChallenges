
from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes
n = 17258212916191948536348548470938004244269544560039009244721959293554822498047075403658429865201816363311805874117705688359853941515579440852166618074161313773416434156467811969628473425365608002907061241714688204565170146117869742910273064909154666642642308154422770994836108669814632309362483307560217924183202838588431342622551598499747369771295105890359290073146330677383341121242366368309126850094371525078749496850520075015636716490087482193603562501577348571256210991732071282478547626856068209192987351212490642903450263288650415552403935705444809043563866466823492258216747445926536608548665086042098252335883
e = 3
ct = 243251053617903760309941844835411292373350655973075480264001352919865180151222189820473358411037759381328642957324889519192337152355302808400638052620580409813222660643570085177957

# while d == -1:
#     p = getPrime(1024)
#     q = getPrime(1024)
#     phi = (p - 1) * (q - 1)
#     d = inverse(e, phi)

# n = p * q

flag = b"XXXXXXXXXXXXXXXXXXXXXXX"
# pt = bytes_to_long(flag)
# ct = int(pow(pt,1/e))


def lrack(n, k=2):
    """Racine kième entière d'un nb entier n de taille quelconque
       Génère une exception "ValueError" si n est négatif et k paire.
    """

    # initialisation du signe et traitement des  cas particuliers
    signe = +1
    if n < 2:
        if n < 0:
            if k % 2 == 0:
                raise ValueError("Erreur: racine paire d'un nombre négatif")
            else:
                # le calcul sera fait avec n>0 et on corrigera à la fin
                signe, n = -1, abs(n)
        else:
            return n  # ici n = 0 ou 1

    # trouve une valeur approchée de la racine (important pour les grds nb)
    rac1, i = n, 0  # i = compteur du nb de positions binaires utilisées
    while rac1 != 0:
        rac1 >>= 1
        i += 1
    rac1 = 1 << (i // k)

    # calcul de la racine en partant de la racine approchée rac1
    km1 = k - 1  # précalcul pour gagner du temps
    delta = n
    while True:
        rac2 = (km1 * rac1 + n // (rac1 ** km1)) // k
        if delta <= 1 and rac2 >= rac1:
            if signe > 0:
                return rac1
            return -rac1
        delta = abs(rac2 - rac1)  # on garde pour la prochaine boucle
        rac1 = rac2


print(f"n = {n}")
print(f"e = {e}")
print(f"ct = {ct}")

pt = lrack(ct, 3)
decrypted = long_to_bytes(pt)
print(decrypted)

# assert decrypted == flag
