from Diffie import *

Antrang = DiffieHellmanKeyExchange()
Member = DiffieHellmanKeyExchange()

Antrang_private = Antrang.generate_private_key()
Antrang_public = Antrang.generate_public_key()

Member_private = Member.generate_private_key()
Member_public = Member.generate_public_key()

Antrang_shared = Antrang.generate_shared_key(Member_public)
Member_shared = Member.generate_shared_key(Antrang_public)

print(f"Antrang:\n{Antrang_private}\n\n{Antrang_public}")
print()
print(f"Member:\n{Member_private}\n\n{Member_public}")
print()

print(Antrang_shared == Member_shared)
print(Antrang_shared)
print()

Antrang_shared = DiffieHellmanKeyExchange.generate_shared_key_static(Antrang_private, Member_public)
Member_shared = DiffieHellmanKeyExchange.generate_shared_key_static(Member_private, Antrang_public)

print(Antrang_shared == Member_shared)
print(Antrang_shared)

input('Press ENTER to exit')