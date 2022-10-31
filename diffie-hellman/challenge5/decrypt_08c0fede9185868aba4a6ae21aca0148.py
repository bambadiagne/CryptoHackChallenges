from operator import mod
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
from Crypto.Util.number import inverse


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
        return unpad(plaintext, 16)
    else:
        return plaintext.decode("utf-8")

g = 2

p = int(0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff)


A = int(0xd331e7799b43103a3c6298bebe710b76490cab46f918335807427c1947cdb85e1520afea93e46de8b92ce23a305247ae5ecd021a171cc6a537ea675c6d35f806059069ca456ef041ad5ad336676ef027b5c770bfca39f6abce8292003eac55e73f0579bc1b32174bb4c500cd60ff8380421155b6a5f50cedb02d4df64bb7d4bdd62520931ef860a27f97f8f31a5d245cb30757293b2bcecfe2ad25252d46d4cc1d768b16f5c5cab8024bd090aeedc9a4884c7ca69b890a34e2de53df370fa2b8)



B = int(0x600d154ef1a03f14c09d4424d6b6f3c3a98c2a6c4af9e3dfd45b418c7b0c3bd23727ce517b86077d92f2fc508b96b3b04214bc25c37ac13e126d91a4725e828237125e13210408764fb02665c97e524addcf070458eb4cd1ab434677804d4c1160443e80b82a8c49a8e141083ffe48b0c215c65fb3554c96416af65dc8d2a7a7bbf3b5cc06388b6388a508d35a02a721b1ef448ff0c8535f627ed66f69d9b0f5695d994aaa1c002e4377727e46f607b9f60178a321b560f2d09ad06122955ada)
b = mod(B*inverse(2,p),p)

iv,encrypted_flag={"iv": "799323e86e329f1576f64ddbd394815a", "encrypted_flag": "02d64b41cee7d4e2aa75ed41cd111fc14bfe09eefe2634c1d5c8818bb3447fff5fcc614f402c9547df2b51d7bfccf346"}.values()
shared_secret = mod(A*b,p)

print(decrypt_flag(shared_secret, iv, encrypted_flag))
