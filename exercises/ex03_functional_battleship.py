"""EX03 - Functional Battleship."""
__author__ = "730670116"

import random 


def input_guess(grid_size: int, row_or_column: str) -> int:
    """Input Guess Function."""
    assert row_or_column == "row" or row_or_column == "column"
    guess = int(input(f"Guess a {row_or_column}: "))
    while guess > grid_size or guess < 1:
        guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
    return guess


BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"


def print_grid(grid_size: int, row_guess: int, column_guess: int, correct_guess: bool) -> None:
    """Print Grid Function."""
    row_counter: int = 1   # create row counter
    while row_counter <= grid_size:   # while loops and printing boxes
        emoji_str: str = ""
        column_counter: int = 1
        while column_counter <= grid_size:
            if row_guess == row_counter and column_guess == column_counter:
                if correct_guess is True:
                    emoji_str += RED_BOX   # correct result box
                else:
                    emoji_str += WHITE_BOX   # incorrect result box
            else:
                emoji_str += BLUE_BOX   # print the blue boxes for the rest of the grid
            column_counter += 1
        print(emoji_str)   # print emoji string
        row_counter += 1   # avoid infinite while loop


def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:
    """Correct Guess Function."""
    if (secret_row == row_guess) and (secret_column == column_guess):
        return True
    else:
        return False


def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """Main Function."""
    turns_available: int = 5
    turn: int = 1
    while turn <= turns_available:
        print(f"=== Turn {turn}/{turns_available} ===")
        row_guess: int = input_guess(grid_size, "row")
        column_guess: int = input_guess(grid_size, "column")
        yes_its_correct: bool = correct_guess(secret_row, secret_column, row_guess, column_guess)
        print_grid(grid_size, row_guess, column_guess, yes_its_correct)
        if yes_its_correct is True:
            print("Hit!") 
            print(f"You won in {turn}/5 turns!")
            return
        else:
            print("Miss!")
        turn += 1
    print("X/5 - Better luck next time!")


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))