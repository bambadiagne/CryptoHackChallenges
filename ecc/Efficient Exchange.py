from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
from ecc_functions import *


def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')


dict_params = {'iv': 'cd9da9f1c60925922377ea952afc212c',
               'encrypted_flag': 'febcbe3a3414a730b125931dccf912d2239f3e969c4334d95ed0ec86f6449ad8'}
G = (1804, 5368)
p = 9739
a = 497
b = 1768
Nb = 6534
x = G
q_x = 4726
while True:
    x = addition_P(x, G, a, b, p)
    if (x[0] == q_x):
        break
possibles_alice = [x, (x[0], -x[1] % p)]
for possible_alice_point in possibles_alice:
    x = k_P(Nb, possible_alice_point, a, b, p)
    shared_secret = x[0]  # x[1]
    iv = dict_params['iv']
    ciphertext = dict_params['encrypted_flag']
    try:
        print(decrypt_flag(shared_secret, iv, ciphertext))

    except BaseException as e:
        print(str(e))
