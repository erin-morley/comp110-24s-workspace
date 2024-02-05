row_counter: int = 1

while row_counter <= grid:
    emoji_str: str = ""
    column_counter: int = 1

    while column_counter <= grid:
        if user_row_guess == row_counter and user_column_guess == column_counter:
            # correct result box
            emoji_str += RED_BOX
        else:
            # wrong result box
            emoji_str += WHITE_BOX
        column_counter += 1

    # print emoji string and change the loop to avoid an infinite while loop
    print(emoji_str)
    row_counter += 1