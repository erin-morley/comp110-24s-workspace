"""Demonstrates range in a for loop"""

names: list[str] = ["Alyssa", "Janet", "Vrinda"]

for index in range (0, len(names)):
    # 0th index is Alyssa
    print(f"{index}:{names[index]}")