"""Demonstrate Basic List Syntax"""

# list_name: ;ist[item type] = list()
grocery_list: list[str] = list() # list() is a constructor
grocery_list: list[str] = [] # <- called literal

str() # constructor
[] # literal

print("Empty list: ")
print(grocery_list)

# adding an item to a list
# list_name.append(item)
grocery_list.append("frosted flakes")
grocery_list.append("milk")
grocery_list.append("pizza")
print("after adding groceries")
print(grocery_list)

 # initializing an already populated list
grocery_list2: list[str] = ["frosted flakes", "milk", "pizza"]
print("Already popualted list: ")
print(grocery_list2)
print("add another thing: ")
grocery_list2.append("whipped cream")
print(grocery_list2)

# indexing
print("printing one item: ")
print(grocery_list[2])

# modifying by index
print("Modifying: ")
x: list[str] = ["c", "a", "r"]
print(x)
x[2] = "t"
print(x)

grocery_list[0] = "cinnamon toast cruch"
print(grocery_list)

# length of a list
print("Length: ")
print(len(grocery_list))

# removing an item from a list
print("Remove an item: ")
grocery_list.pop(2) # use pop
print(grocery_list)

# functions with lists 
def display(my_list: list[str]):
    print(my_list)
display(grocery_list)

def create(word1: str, word2:str) -> list[str]:
    new_list: list[str] = [word1, word2]
    return new_list

print(create("Hello", "world"))
