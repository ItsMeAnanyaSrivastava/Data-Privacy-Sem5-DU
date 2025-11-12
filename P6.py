#Write a Python program that simulates a brute-force attack on a password by trying out 
#all possible character combinations.
import itertools
import string

def brute_force_attack(target_password):
    characters= string.ascii_letters + string.digits + string.punctuation
    attempts =0 
    for password_length in range (1,9):
        for guess in itertools.product(characters,repeat=password_length):
            attempts+=1
            guess=''.join(guess)
            if guess==target_password:
                return f"Password Found: {guess} in {attempts} attempts"
    return "password not found"

if __name__=="__main__":
    target_password=str(input("Enter Password:"))
    result=brute_force_attack(target_password)
    print(result)