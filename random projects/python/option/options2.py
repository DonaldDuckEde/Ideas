import random

def randomOption():
    items = []
    keepAdding = True

    while keepAdding != False:
        tempItem = input("Add item: ")
        
        if tempItem != "done":
            items.append(tempItem)
        elif tempItem == "done":
            print(random.choice(items))
    
randomOption()