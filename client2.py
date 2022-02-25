from Encryption_Decryption import *
from Keys import *
from Diffie import *

message = "This is the Message"
encrypted_message = encrypt(message, Antrang_shared_key)

print("Encrypted Message : \n")
print(encrypted_message)

print("Decrypted Message : \n")
decrypted_message = decrypt(encrypted_message, Member_shared_key)

print(decrypted_message)

input('Press ENTER to exit')