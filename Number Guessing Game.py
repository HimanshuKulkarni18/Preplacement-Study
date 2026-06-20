#Number Guessing Game

import random

def start_guessing_game():
    print("=== Welcome to the Number Guessing Game! ===")
    print("I have picked a secret number between 1 and 100.")
    print("Can you guess what it is?\n")
    
    # Generate a random integer between 1 and 100 inclusive
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        user_input = input("Enter your guess: ")
        
        # Validate that the user entered a valid number
        try:
            guess = int(user_input)
        except ValueError:
            print("❌ Invalid input! Please enter a valid whole number.")
            continue
            
        attempts += 1
        
        # Evaluate the player's guess
        if guess < secret_number:
            print("📈 Too low! Try a higher number.")
        elif guess > secret_number:
            print("📉 Too high! Try a lower number.")
        else:
            print(f"\n🎉 Correct! You found the secret number {secret_number}!")
            print(f"🏆 It took you a total of {attempts} attempts.")
            break

if __name__ == "__main__":
    start_guessing_game()
