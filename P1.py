#Write a program to perform encryption and decryption using Caesar cipher 
#(substitutional cipher).  
def encrypt(text,shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text,shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char
    return result

text=str(input("Enter the text to be encrypted: "))
shift=int(input("Enter the shift value (1-25): "))
encrypted_text=encrypt(text,shift)
print("Encrypted text:", encrypted_text)
decrypted_text=decrypt(encrypted_text,shift)
print("Decrypted text:", decrypted_text)
