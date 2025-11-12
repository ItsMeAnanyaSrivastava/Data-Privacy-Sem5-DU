#Write a program to perform encryption and decryption using Rail Fence Cipher 
#(transpositional cipher) 
from cryptography.fernet import Fernet

def generate_key():
    """Generate a key for encryption and decryption."""
    return Fernet.generate_key()

def encrypt_data(data, key):
    """Encrypt the data using the provided key."""
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data.encode())
    return encrypted

def decrypt_data(encrypted_data, key):
    """Decrypt the data using the provided key."""
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_data).decode()
    return decrypted

key=generate_key
text=str(input("Enter the text to be encrypted: "))
encrypted_text=encrypt_data(text,key)
print("Encrypted text:", encrypted_text)
decrypted_text=decrypt_data(encrypted_text,key)
print("Decrypted text:", decrypted_text)
