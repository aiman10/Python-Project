import base64
from cryptography.fernet import Fernet

def encrypt(key, data):
    cipher_suite = Fernet(key)
    return cipher_suite.encrypt(data)

def decrypt(key, data):
    cipher_suite = Fernet(key)
    return cipher_suite.decrypt(data)