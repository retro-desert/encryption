from Cryptodome.Cipher import AES
import hash_generate


def encrypt(key, plaintext):
    obj = AES.new(key.encode(), AES.MODE_GCM, "Th1s 1s aN IV058".encode())
    plaintext = plaintext.encode()
    ciphertext = obj.encrypt(plaintext)
    return ciphertext

    ###############################################################################################################


def decrypt(key, ciphertext):
    obj2 = AES.new(key.encode(), AES.MODE_GCM, "Th1s 1s aN IV058".encode())
    return obj2.decrypt(ciphertext).decode()


def pad(key):
    pad_key = key[:16] + key[-16:]
    # print(pad_key)
    return pad_key


# print(decrypt(key=pad(hash_generate.generator()), ciphertext=encrypt(key=pad(hash_generate.generator()),
#                                                                      plaintext="lol1234")))
