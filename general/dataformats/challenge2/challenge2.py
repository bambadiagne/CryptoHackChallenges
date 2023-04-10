import os
from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long
os.chdir('C:\\Users\\user\\Documents\\Etudes\\L3TDSI\\Khadim_Sauvegarde\\Programmation\\Python\\cryptohack\\general\dataformats\\challenge2')
# with open("2048b-rsa-example-cert_3220bd92e30015fe4fbeb84a755e7ca5.der","rb") as f:

#     # key = RSA.importKey(f.read())
#     # print(key.e)
#     k=f.read().replace('\\',"")
#     c=""
#     for i in k:
#         a=int(i,16)
#         print(chr(a))
modulus_hex = "3082010a0282010100b4cfd15e3329ec0bcfae76f5fe2dc899c67879b918f80bd4bab4d79e02520609f418934cd470d142a0291392735077f60489ac032cd6f106abad6cc0d9d5a6abcacd5ad2562651e54b088aafcc190f253490b02a29410f55f16b93db9db3ccdcecebc75518d74225de49351432929c1ec669e33cfbf49af8fb8bc5e01b7efd4f25ba3fe596579a2479491727d7894b6a2e0d8751d9233d068556f858310eee81997868cd6e447ec9da8c5a7b1cbf24402948d1039cefdcae2a5df8f76ac7e9bcc5b059f695fc16cbd89cedc3fc129093785a75b45683fafc4184f6647934351cac7a850e73787201e72489259eda7f65bcaf8793198cdb7515b6e030c708f8590203010001"
modulus_hex = "00b4cfd15e3329ec0bcfae76f5fe2dc899c67879b918f80bd4bab4d79e02520609f418934cd470d142a0291392735077f60489ac032cd6f106abad6cc0d9d5a6abcacd5ad2562651e54b088aafcc190f253490b02a29410f55f16b93db9db3ccdcecebc75518d74225de49351432929c1ec669e33cfbf49af8fb8bc5e01b7efd4f25ba3fe596579a2479491727d7894b6a2e0d8751d9233d068556f858310eee81997868cd6e447ec9da8c5a7b1cbf24402948d1039cefdcae2a5df8f76ac7e9bcc5b059f695fc16cbd89cedc3fc129093785a75b45683fafc4184f6647934351cac7a850e73787201e72489259eda7f65bcaf8793198cdb7515b6e030c708f859"
modulus = bytes_to_long(bytes.fromhex(modulus_hex))
print(modulus)
