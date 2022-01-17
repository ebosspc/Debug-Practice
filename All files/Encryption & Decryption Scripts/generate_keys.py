#   a212_generate_keys.py
import rsa as rsa

print("Generating your public/private keypairs now . . .")
keys = rsa.generate_keypair()
print("Public key: ", keys[0])
print("Private key: ", keys[1])
print("Modulus: ",keys[2])
