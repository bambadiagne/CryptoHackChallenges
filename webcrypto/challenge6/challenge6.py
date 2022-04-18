from Crypto.Util.number import bytes_to_long
import jwt
import json
SECRET_KEY="secret"
def create_session(username):
    body = '{' \
              + '"admin": "' + "False" \
              + '", "username": "' + str(username) \
              + '"}'
    print(body)          
    encoded = jwt.encode(json.loads(body), SECRET_KEY, algorithm='HS256')
    return {"session": encoded}
a=create_session("admin")
#print(a)
decoded=""
try:
    decoded = jwt.decode(a['session'], SECRET_KEY, algorithms=['HS256'])
except Exception as e:
    print( {"error": str(e)})
print(decoded)

