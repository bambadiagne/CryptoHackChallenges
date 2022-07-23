import jwt
import os

from requests import session
import requests
os.chdir('C:\\Users\\user\\Documents\\Etudes\\L3TDSI\\Khadim_Sauvegarde\\Programmation\\Python\\cryptohack\\webcrypto\\challenge5\\')
FLAG="niceguy"
with open('public.pem', 'rb') as f:
   PUBLIC_KEY = f.read().strip()
with open('private.pem', 'rb') as f:
   PRIVATE_KEY = f.read()

PUBLIC_KEY=bytes("-----BEGIN RSA PUBLIC KEY-----\nMIIBCgKCAQEAvoOtsfF5Gtkr2Swy0xzuUp5J3w8bJY5oF7TgDrkAhg1sFUEaCMlR\nYltE8jobFTyPo5cciBHD7huZVHLtRqdhkmPD4FSlKaaX2DfzqyiZaPhZZT62w7Hi\ngJlwG7M0xTUljQ6WBiIFW9By3amqYxyR2rOq8Y68ewN000VSFXy7FZjQ/CDA3wSl\nQ4KI40YEHBNeCl6QWXWxBb8AvHo4lkJ5zZyNje+uxq8St1WlZ8/5v55eavshcfD1\n0NSHaYIIilh9yic/xK4t20qvyZKe6Gpdw6vTyefw4+Hhp1gROwOrIa0X0alVepg9\nJddv6V/d/qjDRzpJIop9DSB8qcF1X23pkQIDAQAB\n-----END RSA PUBLIC KEY-----\n","UTF-8")

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
# def create_session(username):
#     encoded = jwt.encode({'username': username, 'admin': False}, PRIVATE_KEY, algorithm='RS256')
#     return {"session": encoded}
def create_session(username):
    encoded = jwt.encode({'username': username, 'admin': True}, PUBLIC_KEY, algorithm='HS256')
    return {"session": encoded}        
def test():
    ac=create_session("admin")
    print(ac)
    url=f"https://web.cryptohack.org/rsa-or-hmac/authorise/{ac['session']}"
    res = requests.get(url).json()
    print(res)

test()
# openssl rsa -RSAPublicKey_in -in /path/to/pub_key.pem -noout -text