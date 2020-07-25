import otp
import hashlib


def generator():
    global hashvalue2
    otp.word_generate()
    hashvalue1 = otp.wrd1 + otp.wrd2 + otp.wrd3 + \
                 otp.wrd4 + otp.wrd5 + otp.wrd6 + \
                 otp.wrd7 + otp.wrd8

    hashvalue = hashvalue1.split()
    hashvalue = "".join(hashvalue)
    hashobj1 = hashlib.sha512()
    hashobj1.update(hashvalue1.encode())
    sha_512 = hashobj1.hexdigest()
    # print("SHA-512: " + sha_512)
    return hashvalue
