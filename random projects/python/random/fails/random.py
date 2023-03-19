import random

print("Hello welcome to the random number generator.")

genNums = []

def genNum():
    print("For all types, type help.")
    inputAction = input("Type: ")
    
    action = inputAction.lower()
        
    if action == "help":
        help("help")
    try:
        num1 = int(input("From: "))
        num2 = int(input("To: "))
    except ValueError():
        print("Please enter a valid input.")
    if action == "":
        generatedNumber = random.randint(a, b)
        
def help(type):
    if type == "types":
        print("Types: ")
        print("Leaf empty for a normal random number.")
        print("Type safe if you want a more secure and random number")