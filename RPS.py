# 1. Game between computer and User
# 2.computer has to choose randomly
# 3. user has to choose either rock, paper or scissor

import  random

choices = ('rock','paper','scissor')

computerChoice = random.choice(choices)

userInput = input("Enter Your Choice :  ")
userChoice = userInput.lower()
# user Winnig Criteria
#   scissor X paper
#   paper X rock
#   rock X scissor

if(userChoice =='scissor' and computerChoice =='paper' or userChoice =='paper' and computerChoice=='rock' or userChoice =='rock' and computerChoice =='scissor'):
    print(f"Computer chooses {computerChoice}")
    print("You Won")

elif(userChoice == computerChoice):
    print(f"Computer chooses {computerChoice}")
    print("It's TIE")

else:
    print(f"Computer chooses {computerChoice}")
print("Computer Won")


# import random

# choices = ('rock', 'paper', 'scissor')

# while True:
#     computerChoice = random.choice(choices)

#     userInput = input("Enter your choice (rock/paper/scissor): ")
#     userChoice = userInput.lower()

#     if userChoice not in choices:
#         print("Invalid choice. Please choose rock, paper, or scissor.")
#         continue

#     print(f"Computer chooses {computerChoice}")

#     if (userChoice == 'scissor' and computerChoice == 'paper' or
#         userChoice == 'paper' and computerChoice == 'rock' or
#         userChoice == 'rock' and computerChoice == 'scissor'):
#         print("You Won!")

#     elif userChoice == computerChoice:
#         print("It's a TIE!")

#     else:
#         print("Computer Won!")

#     # Ask if the user wants to play again
#     playAgain = input("Do you want to play again? (yes/no): ").strip().lower()
#     if playAgain == 'no':
#         print("Game stopped. Thanks for playing!")
#         break
#     elif playAgain != 'yes':
#         print("Invalid input. Stopping game.")
#         break
