from Encryption_Decryption import *
from Keys import *

message = "Random message"
encrypted_message = encrypt(message, Antrang_shared_key)

print(encrypted_message)

decrypted_message = decrypt(encrypted_message, Member_shared_key)

print(decrypted_message)