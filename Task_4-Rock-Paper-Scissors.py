import random

user_wins = 0
computer_wins= 0

options = ["rock", "paper", "scissors"]
options[0]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit : ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2

    computer_pick = options[random_number]

    print("Computer picked", computer_pick + ".")
#rokc vs scissors
    if user_input == "rock" and computer_pick == "scissors":
        print("You WON!")
        user_wins += 1
#paper vs rock        
    elif user_input == "paper" and computer_pick == "rock":
        print("You WON!")
        user_wins += 1
#scissors vs paper        
    elif user_input == "scissors" and computer_pick == "paper":
        print("You WON!")
        user_wins += 1
#TIE
    elif user_input == computer_pick:
        print("Its a TIE!")
       
    else:
        print("You Loss")
        computer_wins += 1

print("You Won", user_wins, "times.")
print("Computer Won", computer_wins, "times.")
