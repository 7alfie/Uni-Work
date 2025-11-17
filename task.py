def SearchOfList(list, target):
    index = 0
    found = False
    while index < len(list) and found == False:
        print("Checking index", index, "value", list[index])
        if list[index] == target:
            found = True
        else:
            index = index + 1

    if found == True:
        print("The item is present in the list")
    else:
        print("The item is not present in the list")


