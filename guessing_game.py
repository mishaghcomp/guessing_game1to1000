"""
Guessing Game (1–1000)
----------------------
A simple Python game where the computer picks a random number between 1 and 1000.
The player keeps guessing until they get it right.

This program demonstrates:
- Variables
- While loops
- Conditional statements
- User input
- Random number generation
"""

import random  # Import the random module

print("🎯 Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 1000...")

# Generate a random secret number between 1 and 1000
secret_number = random.randint(1, 1000)
guess = None  # Initialize the guess variable

# Keep asking until the user guesses correctly
while guess != secret_number:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("❌ Please enter a valid number.")
        continue

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"🎉 Congratulations! You guessed it right: {secret_number}")
