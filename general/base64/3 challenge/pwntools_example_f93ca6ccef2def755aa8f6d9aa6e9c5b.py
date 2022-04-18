from pwn import * # pip install pwntools
import json
from Crypto.Util.number import bytes_to_long, long_to_bytes

import base64
import codecs

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)
ENCODINGS = [
    "base64",
    "hex",
    "rot13",
    "bigint",
    "utf-8",
]

for i in range(101):
    received = json_recv()

    print("Received type: ")
    print(received["type"])
    print("Received encoded value: ")
    print(received["encoded"])

    to_send = {
        "decoded": ""
    }
    if received["type"] == "base64":
        to_send["decoded"] = base64.b64decode(received["encoded"].encode()).decode() # wow so encode
    elif received["type"] == "hex":
            to_send["decoded"] = bytes.fromhex(received["encoded"]).decode("utf-8")
    elif received["type"] == "rot13":
            to_send["decoded"] = codecs.decode(received["encoded"], 'rot_13')
    elif received["type"] == "bigint":
            to_send["decoded"] = long_to_bytes(int(received["encoded"][2:],16)).decode("utf-8")
    elif received["type"] == "utf-8":
        print("___________________",received["encoded"])
        to_send["decoded"] = "".join(chr(b) for b in received["encoded"])
    json_send(to_send)
    
