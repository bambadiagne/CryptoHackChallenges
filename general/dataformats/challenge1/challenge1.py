import os
from Crypto.PublicKey import RSA
os.chdir('C:\\Users\\user\\Documents\\Etudes\\L3TDSI\\Khadim_Sauvegarde\\Programmation\\Python\\cryptohack\\general\dataformats\\challenge1')
with open("privacy_enhanced_mail_1f696c053d76a78c2c531bb013a92d4a.pem","r") as f:

    key = RSA.importKey(f.read())
    
    print(key.public_key().size_in_bits())