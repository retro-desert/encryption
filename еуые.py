from Cryptodome.Cipher import AES

__key__ = 'This is a key12456788765gtyhgtre'

obj = AES.new(__key__.encode(), AES.MODE_GCM, 'This is an IV456'.encode())
message = "Theanswerisлол1234№@!#".encode()
ciphertext = obj.encrypt(message)
print(ciphertext)

obj2 = AES.new(__key__.encode(), AES.MODE_GCM, 'This is an IV456'.encode())
print(obj2.decrypt(ciphertext).decode())
