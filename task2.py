users = [["Jeff", 34],
         ["Badger", 36],
          ["Dave", 90]]

def search(users, target):
    index = 0
    found = False

    while index < len(users) and not found:
        if users[index][0] == target:
            found = True
        else:
            index += 1

    if found:
        print(f"The username is {users[index][0]}, and their level is {users[index][1]}")
    else:
        print("User not found")

target = input("Enter a name to search for")
search(users, target)




# Search by user and show their username and level

