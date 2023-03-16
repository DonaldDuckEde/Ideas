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
        
    if tempId < 0:
       main()
    elif tempId > 0:
        print("Checking user ID...")
    else:
        print("Unvalid input.")
        main()
       
    if fullname == "":
        print("Please enter something.")
        main()
    else:
        print("Checking full name...")
        print(f"Full name checked: {fullname}")
    userId.append(int(tempId))
main()