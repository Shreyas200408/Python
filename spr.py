# #chat gpt

# import random

# def get_computer_choice():
#     choices = ('rock', 'paper', 'scissor')
#     return random.choice(choices)

# def decide_winner(user_choice, computer_choice):
#     """Return outcome as 'win', 'tie', or 'lose'."""
#     if user_choice == computer_choice:
#         return 'tie'
#     # user wins conditions
#     if ((user_choice == 'scissor' and computer_choice == 'paper') or
#         (user_choice == 'paper'   and computer_choice == 'rock') or
#         (user_choice == 'rock'    and computer_choice == 'scissor')):
#         return 'win'
#     return 'lose'

# def play_round():
#     user_input = input("Enter your choice (rock, paper, scissor): ").strip().lower()
#     if user_input not in ('rock', 'paper', 'scissor'):
#         print("Invalid choice. Please choose rock, paper, or scissor.")
#         return None
#     computer_choice = get_computer_choice()
#     result = decide_winner(user_input, computer_choice)
    
#     print(f"Computer chooses {computer_choice}")
#     if result == 'win':
#         print("You Won!")
#     elif result == 'tie':
#         print("It's a TIE")
#     else:
#         print("Computer Won")
#     return result

# def main():
#     print("=== Rock, Paper, Scissor Game ===")
#     user_score = 0
#     computer_score = 0
    
#     while True:
#         result = play_round()
#         if result == 'win':
#             user_score += 1
#         elif result == 'lose':
#             computer_score += 1
        
#         print(f"Score — You: {user_score}, Computer: {computer_score}\n")
        
#         again = input("Play again? (yes/no): ").strip().lower()
#         if again not in ('yes', 'y'):
#             print("Thanks for playing!")
#             break

# if __name__ == '__main__':
#     main()

import random

def play_game():
    choices = ('rock', 'paper', 'scissor')

    while True:
        userInput = input("Enter your choice (rock/paper/scissor): ").strip().lower()
        
        if not userInput:
            print("⚠️ Take a proper guess.")
            continue

        if userInput not in choices:
            print("⚠️ Invalid choice. Please choose rock, paper, or scissor.")
            continue

        computerChoice = random.choice(choices)

        print(f"Computer chooses: {computerChoice}")

        if userInput == computerChoice:
            print("🤝 It's a TIE")
        elif (
            (userInput == 'scissor' and computerChoice == 'paper') or
            (userInput == 'paper' and computerChoice == 'rock') or
            (userInput == 'rock' and computerChoice == 'scissor')
        ):
            print("🎉 You Won!")
        else:
            print("💻 Computer Won!")

        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

# # Run the game
# play_game()