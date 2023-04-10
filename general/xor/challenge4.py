from pwn import xor
encrypted_flag = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
crypto_bytes = bytes("crypto{".encode())
# xor(crypto_bytes,bytes.fromhex("0e0b213f26041e"))
xor_crypto = bytes("myXORkey".encode())
print("key", xor_crypto.decode())
print(xor(xor_crypto, bytes.fromhex(encrypted_flag)).decode("utf-8"))
