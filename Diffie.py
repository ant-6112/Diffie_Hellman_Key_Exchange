from binascii import hexlify
from hashlib import sha256
from os import urandom
from Primes_Base_Gen import primes

class DiffieHellmanKeyExchange:

    def __init__(self, group: int = 14) -> None:
        if group not in primes:
            raise ValueError("Unsupported Group")
        self.prime = primes[group]["prime"]
        self.generator = primes[group]["generator"]

        self.__private_key = int(hexlify(urandom(32)), base=16)

    def generate_private_key(self) -> str:
        return hex(self.__private_key)[2:]

    def generate_public_key(self) -> str:
        public_key = pow(self.generator, self.__private_key, self.prime)
        return hex(public_key)[2:]

    def is_valid_public_key(self, key: int) -> bool:
        if 2 <= key and key <= self.prime - 2:
            if pow(key, (self.prime - 1) // 2, self.prime) == 1:
                return True
        return False

    def generate_shared_key(self, other_key_str: str) -> str:
        other_key = int(other_key_str, base=16)
        if not self.is_valid_public_key(other_key):
            raise ValueError("Invalid public key")
        shared_key = pow(other_key, self.__private_key, self.prime)
        return sha256(str(shared_key).encode()).hexdigest()

    @staticmethod
    def is_valid_public_key_static(
        local_private_key_str: str, remote_public_key_str: str, prime: int
    ) -> bool:
        if 2 <= remote_public_key_str and remote_public_key_str <= prime - 2:
            if pow(remote_public_key_str, (prime - 1) // 2, prime) == 1:
                return True
        return False

    @staticmethod
    def generate_shared_key_static(
        local_private_key_str: str, remote_public_key_str: str, group: int = 14
    ) -> str:
        local_private_key = int(local_private_key_str, base=16)
        remote_public_key = int(remote_public_key_str, base=16)
        prime = primes[group]["prime"]
        if not DiffieHellmanKeyExchange.is_valid_public_key_static(
            local_private_key, remote_public_key, prime
        ):
            raise ValueError("Invalid public key")
        shared_key = pow(remote_public_key, local_private_key, prime)
        return sha256(str(shared_key).encode()).hexdigest()
