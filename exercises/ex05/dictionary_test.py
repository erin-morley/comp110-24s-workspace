"""Dictionary test."""
__author__ = "730670116"

from exercises.ex05.dictionary import invert
from exercises.ex05.dictionary import favorite_color
from exercises.ex05.dictionary import count
from exercises.ex05.dictionary import alphabetizer
from exercises.ex05.dictionary import update_attendance
import pytest


def test_invert1() -> None: 
    """Invert the letters in a list."""
    invert({'e': 'r', 'i': 'n'})
    assert {'n': 'i', 'r': 'e'}


def test_invert2() -> None: 
    """Invert the words in a list."""
    invert({'cat': 'dog', 'fish': 'bird'})
    assert {'bird': 'fish', 'dog': 'cat'}


def test_inverterror() -> None: 
    """Test the invert function with a KeyError."""
    with pytest.raises(KeyError):
        my_dictionary = {'Erin': 'Morley', 'James': 'Morley'}
        invert(my_dictionary)


def test_favorite_color1() -> None: 
    """Find the favorite color of a group of names."""
    favorite_color({"Erin": "pink", "James": "blue", "Brenna": "purple", "Siobhan": "purple"})
    assert {"purple"}


def test_favorite_color2() -> None: 
    """Tie for the favorite color of a group of names."""
    favorite_color({"Erin": "pink", "James": "ppink", "Brenna": "purple", "Siobhan": "purple"})
    assert {"pink", "purple"}


def test_favorite_color3() -> None:
    """No favorite color of a group of names."""
    favorite_color({"Erin": "pink", "James": "blue", "Brenna": "purple", "Siobhan": "green"})
    assert {"pink", "blue", "purple", "green"}


def test_count1() -> None:
    """Normal use of count function."""
    count(["dog", "dog", "dog", "cat", "cat"])
    assert {"dog": 3, "cat": 2}


def test_count2() -> None:
    """Uniqute list of items for count function."""
    count(["dog", "cat", "bird", "fish"])
    assert {"dog": 1, "cat": 1, "bird": 1, "fish": 1}


def test_countempty() -> None:
    """Empty List."""
    count([])
    assert {"": 0}


def test_alphabetizer1() -> None:
    """Normal use of alphabetizer function."""
    alphabetizer(["cat", "bird", "dog", "fish", "boy"])
    assert {'c': ['cat'], 'b': ['bird', 'boy'], 'd': ['dog'], 'f': ['fish']}


def test_alphabetizer2() -> None:
    """Another use of alphabetizer function with capital letters."""
    alphabetizer(["Erin", "elmo", "James", "jargon"])
    assert {'e': ['Erin', 'elmo'], 'j': ['James', 'jargon']}


def test_alphabetizerempty() -> None: 
    """Empty list."""
    alphabetizer([])
    assert {'': []}


def test_update_attendance1() -> None: 
    """Normal use of update attendance function."""
    attendance_log: dict = {"Monday": ["Erin", "James"], "Tuesday": ["Brenna"]}
    update_attendance(attendance_log, "Tuesday", "Siobhan")
    assert attendance_log == {"Monday": ["Erin", "James"], "Tuesday": ["Brenna", "Siobhan"]}


def test_update_attendance2() -> None: 
    """Another use of update attendance function."""
    attendance_log: dict = {"Monday": ["Erin", "Erin"], "Tuesday": ["James"], "Wednesday": ["Brenna"], "Thursday": ["Siobhan"]}
    update_attendance(attendance_log, "Tuesday", "Jim")
    assert attendance_log == {"Monday": ["Erin"], "Tuesday": ["James", "Jim"], "Wednesday": ["Brenna"], "Thursday": ["Siobhan"]}


def test_update_attendance3() -> None: 
    """Empty attendance list."""
    attendance_log: dict = {}
    update_attendance(attendance_log, "Monday", "Erin")
    assert attendance_log == {"Monday": ["Erin"]}