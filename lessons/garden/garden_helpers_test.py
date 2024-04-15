"""Test my garden functions."""
__author__ = "730670116"

from lessons.garden.garden_helpers import add_by_kind
from lessons.garden.garden_helpers import add_by_date
from lessons.garden.garden_helpers import lookup_by_kind_and_date


def test_add_by_kind1() -> None: 
    """Add by kind should add a kind of plant to a plant group."""
    by_kind: dict[str, list[str]] = {'flowers': ['rose', 'tulip'], 'fruit': ['banana', 'pear']}
    add_by_kind(by_kind, 'flowers', 'lily')
    assert by_kind['flowers'] == ['rose', 'tulip', 'lily']


def test_add_by_kind2() -> None: 
    """Add by kind should add a new kind of plant to a new plant group."""
    by_kind: dict[str, list[str]] = {}
    add_by_kind(by_kind, 'trees', 'oak')
    assert by_kind == {'trees': ['oak']}


def test_add_by_date() -> None: 
    """Add by date should add a plant to a certain month."""
    by_date: dict[str, list[str]] = {'May': ['rose', 'banana'], 'July': ['tulip', 'pear']}
    add_by_date(by_date, 'July', 'sunflower')
    assert by_date['July'] == ['tulip', 'pear', 'sunflower']


def test_add_by_date2() -> None: 
    """Add by date should add a new plant to a new month."""
    by_date: dict[str, list[str]] = {}
    add_by_date(by_date, 'January', 'carnation')
    assert by_date == {'January': ['carnation']}


def test_lookup_by_kind_and_date() -> None: 
    """Look up by kind and date should return a month and type if list includes them."""
    by_kind: dict[str, list[str]] = {'flowers': ['rose', 'tulip'], 'fruit': ['banana', 'pear']}
    by_date: dict[str, list[str]] = {'May': ['rose', 'banana'], 'July': ['tulip', 'banana']}

    lookup_by_kind_and_date(by_kind, by_date, "flowers", "May")
    assert "flowers to plant in May: ['rose']"


def test_lookup_by_kind_and_date2() -> None: 
    """Look up by kind and date should return nothing if list doesn't include them."""
    by_kind: dict[str, list[str]] = {'flowers': ['rose', 'tulip'], 'fruit': ['banana', 'pear']}
    by_date: dict[str, list[str]] = {'May': ['rose'], 'July': ['tulip', 'banana']}

    lookup_by_kind_and_date(by_kind, by_date, "fruit", "May")
    assert "No fruit to plant in May"