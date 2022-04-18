import jwt
import os

from requests import session
os.chdir('C:\\Users\\user\\Documents\\Etudes\\L3TDSI\\Khadim_Sauvegarde\\Programmation\\Python\\cryptohack\\webcrypto\\challenge5\\')
FLAG="niceguy"
with open('rsa-or-hmac-public.pem', 'rb') as f:
   PUBLIC_KEY = f.read()
with open('private.pem', 'rb') as f:
   PRIVATE_KEY = f.read()

def authorise(token):
    try:
        decoded = jwt.decode(token, PUBLIC_KEY, algorithms=['HS256', 'RS256'])
    except Exception as e:
        print('----------------',str(e))
        return {"error": str(e)}
    if "admin" in decoded and decoded["admin"]:
        return {"response": f"Welcome admin, here is your flag: {FLAG}"}
    elif "username" in decoded:
        return {"response": f"Welcome {decoded['username']}"}
    else:
        return {"error": "There is something wrong with your session, goodbye"}
def create_session(username):
    encoded = jwt.encode({'username': 'admin', 'admin': True}, PUBLIC_KEY, algorithm='RS256')
    return {"session": encoded}        
ac=create_session("admin")
print(ac)
#print(authorise(ac["session"]))
