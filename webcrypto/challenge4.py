import jwt
encoded = jwt.encode({'username': "admin", 'admin': True},
                     "secret", algorithm='HS256')
print(encoded)
