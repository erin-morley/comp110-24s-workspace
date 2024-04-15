"""Dictionary."""
__author__ = "730670116"


def invert(dict1: dict[str, str]) -> dict[str, str]:
    """Invert Function."""
    inverted_dict: dict[str, str] = {}
    for key in dict1: 
        value = dict1[key]
        if value in inverted_dict: 
            raise KeyError("Duplicate error.") 
        inverted_dict[value] = key
    return inverted_dict
    

def favorite_color(dict1: dict[str, str]) -> str:
    """Favorite color function."""
    color_count: dict[str, int] = {}
    for elem in dict1: 
        y = dict1[elem] 
        if y in color_count:
            color_count[y] += 1
        else: 
            color_count[y] = 1
    max: int = 0
    most_popular_color: str = "" 
    for elem in color_count: 
        if color_count[elem] > max: 
            most_popular_color = elem
            max = color_count[elem]
    return most_popular_color


def count(input_list: list[str]) -> dict[str, int]:
    """Count function."""
    result_dict: dict[str, int] = {}
    for elem in input_list:
        if elem in result_dict:
            result_dict[elem] += 1
        else:
            result_dict[elem] = 1   
    return result_dict


def alphabetizer(word_list: list[str]) -> dict[str, list[str]]:
    """Alphabetizer function."""
    alpha_dict: dict[str, list[str]] = {}
    for elem in word_list:
        first_letter = elem[0].lower()
        if first_letter.isalpha():
            if first_letter not in alpha_dict:
                alpha_dict[first_letter] = []
            alpha_dict[first_letter].append(elem)
    return alpha_dict


def update_attendance(attendance_log: dict[str, list[str]], day_str: str, student_str: str) -> None:
    """Update attendance function."""
    if day_str in attendance_log and student_str not in attendance_log[day_str]:
        attendance_log[day_str].append(student_str)
    else:
        attendance_log[day_str] = [student_str]