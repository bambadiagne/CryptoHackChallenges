import requests
from pwn import xor
BASE_URL="http://aes.cryptohack.org/ecbcbcwtf/"        
cipher_text_iv=requests.get(f'{BASE_URL}encrypt_flag/').json()['ciphertext']
iv,cipher_text=cipher_text_iv[:32],cipher_text_iv[32:64]
plain_text_iv=requests.get(f'{BASE_URL}decrypt/{cipher_text}').json()['plaintext']
plain_text=xor(bytes.fromhex(iv),bytes.fromhex(plain_text_iv)).decode()
print(plain_text)
plain_text_iv=requests.get(f'{BASE_URL}decrypt/{cipher_text_iv[64:]}').json()['plaintext']
plain_text+=xor(bytes.fromhex(cipher_text),bytes.fromhex(plain_text_iv)).decode()
print(plain_text)