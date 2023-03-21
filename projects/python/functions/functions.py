import random
import string

def generatepassword(length):
    pw = ""
    for i in range(length):
        pw += random.choice(string.ascii_letters + string.digits)
    return pw

def randomChar(type):
    if type == "upper":
        random.choice(string.ascii_uppercase)
    elif type == "lower":
        random.choice(string.ascii_lowercase)