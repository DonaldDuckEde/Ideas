import random

print("Hello welcome to this rock, paper, scissors game!")
print("Please type: 'r', 'p', or 's' for rock, paper, or scissors.")

everyThingGood = True

wins, losses, ties = 0, 0, 0

def rock_paper_scissors():
    user_choice = input("Enter your choice: ")
    
    if user_choice == "r" or user_choice == "p" or user_choice == "s":
        everyThingGood = False
    else:
        print("Please enter a valid input.")
            
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
        ties += 1
    elif user_choice == "r" and computer_choice == "s":
        print("You win!")
        wins += 1
    elif user_choice == "r" and computer_choice == "p":
        print("You lose!")
        losses += 1
    elif user_choice == "p" and computer_choice == "s":
        print("You win!")
        wins += 1
    elif user_choice == "p" and computer_choice == "r":
        print("You lose!")
        losses += 1
    elif user_choice == "s" and computer_choice == "r":
        print("You win!")
        wins += 1
    elif user_choice == "s" and computer_choice == "p":
        print("You lose!")
        losses += 1
    
    print(f"Wins: {wins}, Losses: {losses}, Ties: {ties}")    

rock_paper_scissors()        