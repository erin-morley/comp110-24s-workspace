"""Some functions for my garden plan!"""
__author__ = "730670116"

plant: str = "daisy"
plant_kind: str = "flower"


def add_by_kind(plants_by_kind: dict[str, list[str]], plant_kind: str, plant: str) -> None:
    """Add by kind function."""
    if plant_kind in plants_by_kind:  # if key "plant_kind" is in "plants by kind"
        plants_by_kind[plant_kind].append(plant)
    else:  # if key "plant_kind" is NOT in "plant_by_kind"
        plants_by_kind[plant_kind] = []
        plants_by_kind[plant_kind].append(plant)
        
        
by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
by_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots", "zinnias"]}


def add_by_date(plants_by_date: dict[str, list[str]], month: str, plant: str) -> None:
    """Add by date function."""
    if month in plants_by_date: 
        plants_by_date[month].append(plant)
    else: 
        plants_by_date[month] = []
        plants_by_date[month].append(plant)


def lookup_by_kind_and_date(plants_by_kind: dict[str, list[str]], plants_by_date: dict[str, list[str]], plant_kind: str, month: str) -> str:
    """Look up by kind and date function."""
    assert plant_kind in plants_by_kind
    assert month in plants_by_date

    list_of_plants_by_kind: list[str] = plants_by_kind[plant_kind]
    list_of_plants_by_date: list[str] = plants_by_date[month]
    combined: list[str] = []
    for plant in list_of_plants_by_kind:
        for other_plant in list_of_plants_by_date:
            if other_plant in list_of_plants_by_date:
                if other_plant == plant: 
                    combined.append(other_plant)
    if len(combined) > 0:
        return f"{plant_kind}s to plant in {month}: {combined}"
    else:
        return f"No {plant_kind} to plant in {month}"