import random

print("Hello welcome to this rock, paper, scissors game!")
print("Please type: 'r', 'p', or 's' for rock, paper, or scissors.")

def rock_paper_scissors():
    user_choice = input("Enter your choice: ")
    
    computer_choice = random.choice(["r", "p", "s"])
    
    if computer_choice == "r":
        print("Rock")
    elif computer_choice == "p":
        print("Paper")
    elif computer_choice == "s":
        print("Scissors")
    else:
        print("If this shows up, it means that something went terribly wrong.")            
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "r" and computer_choice == "s":
        print("You win!")
    elif user_choice == "r" and computer_choice == "p":
        print("You lose!")
    elif user_choice == "p" and computer_choice == "s":
        print("You win!")
    elif user_choice == "p" and computer_choice == "r":
        print("You lose!")
    elif user_choice == "s" and computer_choice == "r":
        print("You win!")
    elif user_choice == "s" and computer_choice == "p":
        print("You lose!")

rock_paper_scissors()        