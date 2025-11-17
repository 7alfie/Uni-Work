# Linear Searches

items = ["Alabama", "California", "Delaware", "Florida", "Georgia", "Texas", "Ohio", "Nebraska", "Idaho"]
itemtofind = input("Enter the state to find ")

index = 0
found = False

while found == False and index < len(items):
    if items[index] == itemtofind:
        found = True
    else:
        index = index + 1

if found == True:
    print(f"Item found, at index {index}")
else:
    print("Item not found")

