items = ["Alabama", "California", "Delaware", "Florida", "Georgia", "Texas", "Ohio", "Nebraska", "Idaho"]
itemtofind = input("Enter the state to find ")

found = False
first = 0
last = len(items)-1

while first <= last and found == False:
    midpoint = (first+last)//2
    if items[midpoint] == itemtofind:
        found = True
    else:
        if items[midpoint] < itemtofind:
            first = midpoint + 1
        else:
            last = midpoint - 1


if found == True:
    print(f"Item found at position, {midpoint}")
else:
    print(f"Item not found at position, {last}")

# When we find the midpoint we check to see if that's what we're looking for.