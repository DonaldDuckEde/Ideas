import random

def randomOption():
    def randomInput():
        try:
            amountOfOptions = int(input("Amount of items to the list: "))
        except ValueError():
            print("Please enter a valid input.")
            randomInput()
            
    randomInput()
    
    items = []
    
    for i in range(amountOfOptions):
        tempItem = input("Please enter your item: ")
        items.append(tempItem)
        
    def wantRandom():    
        AskRandom = input("Do you want to get a random item? Please enter 'yes' or 'no'")
        
        AskRandom = AskRandom.lower()
        
        if AskRandom == "yes":
            print()
        elif AskRandom == "no":
            print("Shutting down....")
        else:
            print("Please enter a valid input")
            wantRandom()
    
    wantRandom()
    