# Game Criteria
# 1. Starts by generating a Random number b/w 1-20
# 2. user has to Guess the SecretNumber
# 3. UG > SN (Too High)
# 4. UG < SN (Too LOw)
# 5. UG == SN (Correct GUess)

import random

# random : it's a Module which is used to generate the random number or random entities

secretNumber = random.randint(1,20)
print(secretNumber)
# Taking user Input
score = 20

while True:
    userGuess = int(input("Enter the Guess.:  "))
    if not userGuess:
        print("Enter a Valid Number")

    if (userGuess > secretNumber):
        print("Too High")
        score -=1

    elif(userGuess < secretNumber):
        print("Too Low")
        score -=1

    else:
        print("Correct Guess")
        print(f"Your score is {score}")
    
    