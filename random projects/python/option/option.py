import random

def randomOption():
    try:
        amountOfOptions = int(input("Amount of items to the list: "))
    except ValueError():
        print("Please enter a valid input.")
    
    for i in range(amountOfOptions):
        