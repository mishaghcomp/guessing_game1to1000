import random

print("Welcome to the guessing game!")
secret_number = random.randint(1, 1000)
guess = None

while guess != secret_number:
    guess = int(input("Guess a number between 1 and 1000: "))
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"🎉 Congratulations! You guessed it right: {secret_number}")
