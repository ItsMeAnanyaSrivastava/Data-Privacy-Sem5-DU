#Write a Python program that generates a password using a random combination of 
#words from a dictionary file. 
import random

def generate_password(dictionary_file,num_words):
    with open(dictionary_file,'r') as file:
        words=file.read().splitlines()
    paaword=''.join(random.sample(words,num_words))
    return paaword

dictionary_file='dictionary.txt'
num_words=3
password=generate_password(dictionary_file,num_words)
print("Generated password:",password)