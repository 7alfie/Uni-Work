# Lists in one dimension

# Lists are muteable and passed by reference
# Arrays have a fixed number of items in the same data type and are static.
array = [32,33,34,35,36.37] # All the same data type and fixed number of items.

# Record mixed data types
records = ["cheese", True, 345, 4.655] # Mixed data types
# Lists are dynamic,
listx =[234,546,3245] # Things can be repeatedly added or taken away from a list

# Items shouldn't be able to be added or removed from an Array

# All of these are lists but can be categorised differently between an array, record and a list.

# List methods
# Add a item to the end
listx.append(234324)
print(listx)

# Make a copy
new=listx.copy()
print(new)

# Extend the list
listx.extend([12,13,14,15])

# Return the index of an item
print(listx)
print(listx.index(14)) # Will print the index of the item in the list

# Sorting the list in ascending order
listx.sort()

# Sorting in reversing order
listx.reverse()

# Popping and pushing a list, pop removes an item at a given index, and pushing adds an item.
listx.pop(3)
print(listx)

# Remove deletes an item given
listx.remove(12)
print(listx)

# Inserting an item into a certain place
listx.insert(2,2435435345) # Index number, then item.
print(listx)

# Iterating through a list

for item in listx :
    print(item)
# Prints out each item in the list

# If index value
for index in range(len(listx)) :
    print(index, listx[index])
# Prints the index then the item at the given index.

for index, item in enumerate(listx) :
    print(index, item)

