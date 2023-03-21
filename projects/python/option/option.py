import random

def randomOption():
    try:
        amountOfOptions = int(input("Amount of items to the list: "))
    except ValueError():
        print("Please enter a valid input.")
    
    items = []
    
    for i in range(amountOfOptions):
        tempItem = input("Please enter your item: ")
        items.append(tempItem)
  
    AskRandom = input("Do you want to get a random item? Please enter 'yes' or 'no' ")
      
    AskRandom = AskRandom.lower()
     
    if AskRandom == "yes":
        randomItem = random.choice(items)
        print(randomItem)
        return randomItem
    elif AskRandom == "no":
        print("Shutting down....")
    else:
        print("Please enter a valid input")
    
randomOption()