import subprocess
import os
import jwt
import requests  # note this is the PyJWT module, not python-jwt
from get_pubkey import get_public_key

# Private key generated using: openssl genrsa -out rsa-or-hmac-2-private.pem 2048
# with open('challenge_files/rsa-or-hmac-2-private.pem', 'rb') as f:
#    PRIVATE_KEY = f.read()
# Public key generated using: openssl rsa -RSAPublicKey_out -in rsa-or-hmac-2-private.pem -out rsa-or-hmac-2-public.pem
full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)
os.chdir(path)

# k=os.system("openssl s_client -showcerts -connect web.cryptohack.org/:443 | openssl x509 -pubkey -noout > rightPubKey.pem")
with open('rightPubKey.pem', 'rb') as f:
    PUBLIC_KEY = f.read()
# PUBLIC_KEY = get_public_key('web.cryptohack.org')
# PUBLIC_KEY= subprocess.check_output("openssl x509 -pubkey -noout -in cert.pem")
FLAG = "niceguy"
# print("PUB",PUBLIC_KEY)


def authorise(token):
    try:
        decoded = jwt.decode(token, PUBLIC_KEY, algorithms=['HS256', 'RS256'])
    except Exception as e:
        return {"error": str(e)}

    if "admin" in decoded and decoded["admin"]:
        return {"response": f"Welcome admin, here is your flag: {FLAG}"}
    elif "username" in decoded:
        return {"response": f"Welcome {decoded['username']}"}
    else:
        return {"error": "There is something wrong with your session, goodbye"}


def create_session(username):
    encoded = jwt.encode(
        {'username': username, 'admin': True}, PUBLIC_KEY, algorithm='HS256')
    return {"session": encoded}


def test():
    ac = create_session("admin")
    print(ac)
    url = f"https://web.cryptohack.org/rsa-or-hmac-2/authorise/{ac['session']}"
    res = requests.get(url).json()
    print(res)


test()
# openssl x509 -pubkey -noout -in cert.cer
