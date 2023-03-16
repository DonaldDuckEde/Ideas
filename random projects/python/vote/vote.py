def main():
    fullname = ""
    userId = [-1]
    idTry = 0
    
    try:
        fullName = str(input("Full name: "))
        tempId = int(input("User ID: "))
        
    except ValueError():
        print("Please enter a valid number.")
        main()

    print("Welcome to the vote system.")
    
    userId.append(int(tempId))
    
    print("please type help for a list of commands.")
    tempCommand = input("Command: ")
    
    if tempCommand == "vote":
        vote = input("What would you like to vote for? ")
        if vote == "":
    
main()