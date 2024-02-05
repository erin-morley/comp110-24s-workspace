"""EX01 - One Shot Battleship."""
__author__ = "730670116"

# size of grid, secret row and column
grid: int = 4
secret_row: int = 3
secret_column: int = 2

# prompt the user to guess a row
user_row_guess: int = int(input("Guess a row: "))
# while loop for row
while int(user_row_guess) > 4 or int(user_row_guess) < 1:
    user_row_guess = int(input(f"The grid is only {grid} by {grid}. Try again: "))

# prompt the user to guess a column
user_column_guess: int = int(input("Guess a column: "))
# while loop for column
while int(user_column_guess) > 4 or int(user_column_guess) < 1:
    user_column_guess = int(input(f"The grid is only {grid} by {grid}. Try again: "))


# GRID EMOJIS
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

# create counter variables
row_counter: int = 1

# WHILE LOOPS AND PRINTING BOXES 
while row_counter <= grid:
    emoji_str: str = ""
    column_counter: int = 1

    while column_counter <= grid:
        if user_row_guess == row_counter == 3 and user_column_guess == column_counter == 2:
            # correct result box
            emoji_str += RED_BOX
        elif (user_row_guess == row_counter and user_column_guess == column_counter) and (row_counter != 3 or column_counter != 2):
            # incorrect result box
            emoji_str += WHITE_BOX
        else:
            # how to print the blue boxes for the rest of the grid
            emoji_str += BLUE_BOX
        column_counter += 1
    # print emoji string and change the loop to avoid an infinite while loop
    print(emoji_str)
    row_counter += 1

# ending statements and hints for the user
if int(user_row_guess) == 3 and int(user_column_guess) == 2:
    print("Hit!")
if user_row_guess == 3 and user_column_guess != 2:
        print("Close! Correct row, wrong column.")
if user_column_guess == 2 and user_row_guess != 3:
        print("Close! Correct column, wrong row.")
if user_row_guess != 3 and user_column_guess != 2:
        print("Miss!")