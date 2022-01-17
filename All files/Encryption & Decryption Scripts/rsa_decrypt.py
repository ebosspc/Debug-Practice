#   a212_rsa_decrypt.py
import rsa as rsa

key = int(input("Enter the Decryption Key: " ))
mod_value = int(input("Enter the Modulus: " ))
encrypted_msg = input("What message would you like to decrypt (No brackets): ")

#break apart the list that is cut/copied over on ", "
msg = encrypted_msg.split(", ")
print (rsa.decrypt(key,mod_value , msg))
