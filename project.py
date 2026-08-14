import random
#--Banner---
print("*" * 30)
print("Rock, Paper, Scissors")
print("*" * 30)

#--setup---
choices = ("rock", "paper", "scissors")
beats={
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock",
    
}
score = {"player": 0, "computer": 0, "ties": 0}
#--game loop---
while True:
    #--player choice---
    player_choice = input("Enter your choice (rock, paper, scissors) or 'quit' to exit: ").lower()
    if player_choice == "quit":
        break
    if player_choice not in choices:
        print("Invalid choice. Please try again.")
        continue

    #--computer choice---
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    #--determine winner---
    if player_choice == computer_choice:
        print("It's a tie!")
        score["ties"] += 1
    elif beats[player_choice] == computer_choice:
        print("You win!")
        score["player"] += 1
    else:
        print("Computer wins!")
        score["computer"] += 1
        
