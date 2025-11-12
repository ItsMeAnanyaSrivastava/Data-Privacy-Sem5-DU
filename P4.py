#Write a Python program that reads a file containing a list of usernames and passwords, 
#one pair per line (separated by a comma). It checks each password to see if it has been 
#leaked in a data breach. You can use the "Have I Been Pwned" API 
#(https://haveibeenpwned.com/API/v3) to check if a password has been leaked. 
import requests
import hashlib

def check_password_leaks(password):
    sha1_password=hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char,tail=sha1_password[:5],sha1_password[5:]
    url=f"https://api.pwnedpasswords.com/range/{first5_char}"
    response=requests.get(url)
    hashes=(line.split(':') for line in response.text.splitlines())
    for h,count in hashes:
        if h==tail:
            return True
    return False

def read_credentials(file_path):
    with open(file_path,'r') as file:
        credentials=[line.strip().split(',') for line in file]
    return credentials

def main():
    file_path='a.csv'
    credentials=read_credentials(file_path)
    for username,password in credentials:
        if check_password_leaks(password):
            print(f"Password for user {username} has been leaked")
        else:
            print(f"Password for user name {username} is safe" )

if __name__=="__main__":
    main()
    