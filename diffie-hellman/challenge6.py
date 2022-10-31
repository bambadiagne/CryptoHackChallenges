from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib

from pwn import *
con=remote('socket.cryptohack.org',13371,level='debug')
from random import randint
import json

alice_initial=con.recvline()
data=json.loads(alice_initial[24:])
p_hex=data['p']
g_hex=data['g']
A_hex=data['A']
p=int(p_hex,16)
A=int(A_hex,16)
g=int(g_hex,16)
#Generate attacker's random secret
r=randint(1,p//2)
s=pow(g,r,p)
# Compute shared secret with A
shared_A=pow(A,r,p)
to_bob={"p":p_hex,"g":g_hex,"A":hex(s)}
con.sendline(json.dumps(to_bob))
bob=con.recvline()
bob_data=json.loads(bob[35:])
B_hex=bob_data['B']
# Compute shared secret with B
shared_B=pow(int(B_hex,16),r,p)
to_alice={"B":hex(s)}
con.sendline(json.dumps(to_alice))
content=con.recvline()
iv_hex=json.loads(content[39:])['iv']
enc_flag_hex=json.loads(content[39:])['encrypted_flag']



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
        return unpad(plaintext, 16).decode()
    else:
        return plaintext.decode()


shared_secret = shared_A
iv = iv_hex
ciphertext = enc_flag_hex

print(decrypt_flag(shared_secret, iv, ciphertext))