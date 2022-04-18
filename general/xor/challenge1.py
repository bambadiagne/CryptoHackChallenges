from pwn import *
print("".join(chr(ord(i)^13) for i in "label"))

