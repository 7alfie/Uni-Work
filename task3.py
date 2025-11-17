dictionary = {
    "Jeff": 34,
    "Badger": 36,
    "Dave": 90
}

def linearsearch(data, targetkey, targetvalue):
    index = 0
    keys = list(data.keys())
    found = False

    while index < len(keys) and found == False:
        key = keys[index]
        value = data[key]

        if key == targetkey and value == targetvalue:
            found = True
        else:
            index = index + 1

    if found == True:
        return key, value
    else:
        return None

