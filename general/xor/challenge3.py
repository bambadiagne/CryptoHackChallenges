from pwn import xor
from Crypto.Util.number import *
hidden_flag="73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
for i in range(1,100):
    possible_text=xor(bytes.fromhex(hidden_flag),int(i).to_bytes(1,"little")).decode('utf-8')
    if("crypto" in possible_text):
        print(possible_text)
    