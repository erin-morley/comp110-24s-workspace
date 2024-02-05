"""Number Guessing Game"""
from random import randint

SECRET: int = randint(1, 10)
correct: bool = False

while not correct: # could also say "while correct == False"
    guess: int = int(input("Guess a number: "))
    if guess == SECRET:
        print(f"Correct! {guess} is the number!")
        # to help us exit the loop
        correct == True
    elif guess > SECRET:
        print("Too high!")