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
    
    
main()