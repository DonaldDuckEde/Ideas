import random
import string

def password():
    amountCharacters = int(input("How many characters would you like in your password? "))
    if amountCharacters > 0:
        print("Generating password...")
        password = []
        password.append(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase))
        
        for i in range(amountCharacters - 1):
        
        print(password[0])

password()