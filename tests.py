import crypter
import time
import re
import hash_generate
import base64
import hashlib
from Cryptodome.Cipher import AES


def ensure_periodic_value(interval):
    def wrapper(func):
        def inner(*args, **kwargs):
            if time.monotonic() - getattr(func, "ttl", interval) >= interval:
                func.periodic_value = hash_generate.generator()
                func.ttl = time.monotonic()
            return func(func.periodic_value)
        return inner
    return wrapper


# @ensure_periodic_value(interval=600)
# def encrypt(hash):
#     global ciphertext
#     # print(f"Random value is: {random_value}")
#     raw = str(crypter.encrypt(key=crypter.pad(hash), plaintext=data))
#     print("This:", raw)
#     obj = AES.new(password.encode(), AES.MODE_GCM, iv.encode())
#     message = str(raw).encode()
#     ciphertext = obj.encrypt(message)
#     print("Ciphertext:", ciphertext)
#     return ciphertext
#
#
# @ensure_periodic_value(interval=600)
# def decrypt(hash):
#     obj2 = AES.new(password.encode(), AES.MODE_GCM, iv.encode())
#     ciphertext = obj2.decrypt(ciphertext)  # .decode()
#     print(crypter.decrypt(key=crypter.pad(hash), ciphertext=ciphertext))


@ensure_periodic_value(interval=600)
def encrypt(hash):
    global ciphertext
    # plaintext = str(crypter.encrypt(key=crypter.pad(hash), plaintext=data))
    ciphertext = str(crypter.encrypt(key=crypter.pad(hash), plaintext=data))
    # obj = AES.new(crypter.pad(password), AES.MODE_GCM, iv.encode())
    # plaintext = plaintext.encode()
    # ciphertext = obj.encrypt(plaintext)
    # print(ciphertext)
    return ciphertext


@ensure_periodic_value(interval=600)
def decrypt(hash):
    # obj2 = AES.new(crypter.pad(password), AES.MODE_GCM, iv.encode())
    print(crypter.decrypt(key=crypter.pad(hash), ciphertext=ciphertext))
    # return obj2.decrypt(ciphertext).decode()


# freenewbusinessoonalwesternneara Th1s 1s aN IV058
password = input("Input password: ")
iv = input("Input IV: ")
data = input("input data: ")


# __key__ = hashlib.sha256(key1.encode()).digest()


def main():
    global encrypted, enc_dict
    encrypted = encrypt()
    enc_dict = encrypted
    print(encrypted)

    decrypted = decrypt()
    print(bytes.decode(decrypted))


main()

# encrypt()
# decrypt()
# while True:
#     encrypt_decrypt()
#     time.sleep(5)
