#Write a Python program that defines a function and takes a password string as input and 
#returns its SHA-256 hashed representation as a hexadecimal string.
import hashlib

def hash_password(password):
    hash=hashlib.sha256(password.encode()).hexdigest()
    return hash

password=str(input("Enter the password to be hashed: "))
hashed_password=hash_password(password)
print("Hashed password:", hashed_password)