"""EX01 - Simple Battleship - A cute step towards Battleship."""
__author__ = "730670116"

# player 1 is prompted to pick a number

user1_input: str = input("Pick a secret boat location between 1 and 4: ")
user1_number: int = int(user1_input)

if user1_number <= 0:
    print(f"Error! {user1_number} too low!")
    exit()

if user1_number > 4:
    print(f"Error! {user1_number} too high!")
    exit()

# player 2 is prompted to guess a number
    
user2_input: str = input("Guess a number between 1 and 4: ")
user2_number: int = int(user2_input)

if user2_number <= 0:
    print(f"Error! {user2_number} too low!")
    exit()

if user2_number > 4:
    print(f"Error! {user2_number} too high!")
    exit()

# emoji list
    
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

# printing boxes if user2 guessed correctly

if user2_number == user1_number == 1:
    print(RED_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX)
if user2_number == user1_number == 2:
    print(BLUE_BOX + RED_BOX + BLUE_BOX + BLUE_BOX)
if user2_number == user1_number == 3:
    print(BLUE_BOX + BLUE_BOX + RED_BOX + BLUE_BOX)
if user2_number == user1_number == 4:
    print(BLUE_BOX + BLUE_BOX + BLUE_BOX + RED_BOX)

# printing boxes if user2 guessed incorrectly

if user2_number == 1 != user1_number:
    print(WHITE_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX)
if user2_number == 2 != user1_number:
    print(BLUE_BOX + WHITE_BOX + BLUE_BOX + BLUE_BOX)
if user2_number == 3 != user1_number:
    print(BLUE_BOX + BLUE_BOX + WHITE_BOX + BLUE_BOX)
if user2_number == 4 != user1_number:
    print(BLUE_BOX + BLUE_BOX + BLUE_BOX + WHITE_BOX)

# printing if response is equal to the correct number
    
if user2_number == user1_number:
    print("Correct! You hit the ship.")

if user2_number != user1_number:
    print("Incorrect! You missed the ship.")

