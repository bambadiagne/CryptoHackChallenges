import base64
from Crypto.Util.number import bytes_to_long
from Crypto.PublicKey import RSA
import os
os.chdir('C:\\Users\\user\\Documents\\Etudes\\L3TDSI\\Khadim_Sauvegarde\\Programmation\\Python\\cryptohack\\general\dataformats\\challenge3')
with open("bruce.pem","r") as f:
    # base64_=encoded_file.read().split(" ")[1]
    # hex_content=bytes.hex(base64.b64decode(base64_))
    # with open("pub_key2","w") as pub:
    #     # pub.write(hex_content)
    #     len_hex=len(hex_content)//32
    #     for i in range(len_hex):
    #         cn=hex_content[32*i:32*(i+1)]
    #         print(len(cn))
    #         line=" ".join(cn[2*j:2*(j+1)] for j in range(0,len(cn),2))
    #         pub.write(line+"\n")
    key = RSA.importKey(f.read())
    
    print(key.n)
