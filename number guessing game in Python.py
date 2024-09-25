# Simple game in Python

print("Welcome to the number guessing game!")

# Generate a random number between 1 and 100
import random
number = random.randint(1, 100)

# Loop to allow the player to make multiple guesses
guessed = False
while not guessed:
    # Get the player's guess
    guess = int(input("Enter your guess: "))
    
    # Check if the guess is correct
    if guess == number:
        print("Congratulations! You guessed the right number.")
        guessed = True
    elif guess < number:
        print("The number is higher.")
    else:
        print("The number is lower.")

print("Thanks for playing!")
