import json
import jwt
import requests # note this is the PyJWT module, not python-jwt


FLAG = "niceguy"
SECRET_KEY ="secret123456" 


def authorise(token):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except Exception as e:
        return {"error": str(e)}
    print(decoded)
    if "admin" in decoded and decoded["admin"] == "True":
        return {"response": f"Welcome admin, here is your flag: {FLAG}"}
    elif "username" in decoded:
        return {"response": f"Welcome {decoded['username']}"}
    else:
        return {"error": "There is something wrong with your session, goodbye"}


def create_session(username):
    body = '{' \
              + '"admin": "' + "False" \
              + '", "username": "' + str(username) \
              + '"}'
    encoded = jwt.encode(json.loads(body), SECRET_KEY, algorithm='HS256')
    return {"session": encoded}
def test():
    username_injection='","admin":"True'#Json injection in username
    ac=create_session(username_injection)
    print(ac)
    url=f"https://web.cryptohack.org/json-in-json/authorise/{ac['session']}"
    res = requests.get(url).json()
    print(res)
test()