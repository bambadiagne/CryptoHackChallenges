import ssl
import socket
from asn1crypto import pem, x509
from oscrypto.asymmetric import load_public_key


def get_public_key(url):
    ctx = ssl.create_default_context()
    s = ctx.wrap_socket(socket.socket(), server_hostname=url)
    s.connect((url, 443))
    der = s.getpeercert(binary_form=True)
    cert = x509.Certificate.load(der)

    pubkey = load_public_key(cert.public_key).unwrap()
    # .replace('-----BEGIN PUBLIC KEY-----','-----BEGIN RSA PUBLIC KEY-----').replace('-----END PUBLIC KEY-----','-----END RSA PUBLIC KEY-----').encode()
    return pem.armor("RSA PUBLIC KEY", pubkey.contents)
