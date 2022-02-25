from Keys import *
import requests

BASE_URL = "http://127.0.0.1:5000" 

Antrang = requests.get(f"{BASE_URL}/generate-keys").json()
Antrang_private = Antrang["private_key"]
Antrang_public = Antrang["public_key"]

Member = requests.get(f"{BASE_URL}/generate-keys").json()
Member_private = Member["private_key"]
Member_public = Member["public_key"]

Antrang_params = {
    "local_private_key": Antrang_private, 
    "remote_public_key": Member_public,
}

Member_params = {
    "local_private_key": Member_private, 
    "remote_public_key": Antrang_public
}

print(f"Antrang:\n{Antrang_private}\n\n{Antrang_public}")
print()
print(f"Member:\n{Member_private}\n\n{Member_public}")
print()

Antrang_shared_key = requests.get(
    f"{BASE_URL}/generate-shared-key", 
    params=Antrang_params).json()

Antrang_shared_key = Antrang_shared_key["shared_key"]

Member_shared_key = requests.get(
    f"{BASE_URL}/generate-shared-key",
    params=Member_params).json()

Member_shared_key = Member_shared_key["shared_key"]

assert Antrang_shared_key == Member_shared_key

print("Antrang Shared Key : \n")
print(Antrang_shared_key)

print("Memeber Shared Key : \n")
print(Member_shared_key)

print(Antrang_shared_key == Member_shared_key)
print()


input('Press ENTER to exit')