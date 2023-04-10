# The pubkey 34.pem divided the pubkey 21.pem

import os
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long, inverse
import pathlib
import math
current_directory = pathlib.Path(__file__).parent.resolve()
msg = "???"
KEYS_DIRECTORY = os.path.join(current_directory, 'keys_and_messages')


with open(os.path.join(KEYS_DIRECTORY, '21.pem')) as f:
    original_key = RSA.importKey(f.read())

with open(os.path.join(KEYS_DIRECTORY, '21.ciphertext')) as f:
    CIPHER_TEXT = f.read()
ALL_KEYS = (file for file in os.listdir(os.path.join(current_directory,
            'keys_and_messages')) if (file.endswith('.pem') and not file.startswith('21')))

for key_ in ALL_KEYS:
    with open(os.path.join(KEYS_DIRECTORY, key_)) as f:
        possible_key = RSA.importKey(f.read())
        if (math.gcd(original_key.n, possible_key.n) != 1):
            p = math.gcd(original_key.n, possible_key.n)
            q = original_key.n//p
            break

phi = (p - 1) * (q - 1)
d = inverse(original_key.e, phi)

key = RSA.construct((original_key.n, original_key.e, d))
cipher = PKCS1_OAEP.new(key)

ciphertext = bytes.fromhex(CIPHER_TEXT)

print(cipher.decrypt(ciphertext).decode())
# def factorize():
#     for file in os.listdir():


# with open('21.pem') as f:
#     key = RSA.importKey(f.read())

# cipher = PKCS1_OAEP.new(key)
# ciphertext = cipher.encrypt(msg)

# with open('21.ciphertext', 'w') as f:
#     f.write(ciphertext.hex())
