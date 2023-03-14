def addPerson(free, places):
    if free > 0:
        passengers = []
        for i in range(free):
            nameInput = input("Enter the passenger's name: ")
            passengers.append(nameInput)

print("Welcome to the placing system!")

try:
    placesInput = int(input("How many places are there? "))
    freeInput = int(input("How many free places are there? "))
    
    if freeInput > placesInput:
        print("Error: You can't have more free places than there are places!")
    elif freeInput < placesInput:
        addPerson(freeInput, placesInput)
    elif freeInput == placesInput: 
       addPerson(free, places)

except ValueError():
    print("Wrong input, please enter a number.")
    main()