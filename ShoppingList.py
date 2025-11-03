shoppinglist = []
itemquantity =[]
itemavailability=['beans', 'eggs', 'sausages', 'milk', 'chocolate']

def menu():
    print('''Select an option
1. Add an item to your list
2. View your list
3. Remove an item from your list
4. Check an item in your list
5. Is my item available?''')

    choice = input("Enter your choice: ")
    if choice == "1":
        additem()
    elif choice == "2":
        viewitem()
    elif choice == "3":
        removeitem()
    elif choice == "4":
        checkitem()
    elif choice == "5":
        itemavailable()
        menu()
    else:
        print("Invalid choice")
        menu()

def additem():
    item = input("Enter an item to add to your list: ")
    shoppinglist.append(item)
    again = input("Would you like to add another item? yes/no ")
    if again == "yes":
        additem()
    elif again == "no":
        menu()
    else:
        print("Invalid choice")
        menu()

def viewitem():
    for number, item in enumerate(shoppinglist, start=1):
        print(f"{number}. {item}")


def removeitem():
    item = input("Enter an item to remove from your list: ")
    if item in shoppinglist:
        shoppinglist.remove(item)
        print(f"{item} removed.")
    else:
        print("That item is not in your list.")
    again = input("Would you like to remove another item? (yes/no): ").lower()
    if again == "yes":
        removeitem()
    elif again == "no":
        menu()
    else:
        print("Invalid choice")
    pass

def checkitem():
    itemchecked= input("Enter an item to check: ")
    if itemchecked in shoppinglist:
        print(f"{itemchecked} is in your list and is at index {shoppinglist.index(itemchecked)} ")
    else:
        print("Your item is not in the shopping list")
        pass

def itemavailable():
    itemchecked= input("Enter an item to check the availability of: ")
    if itemchecked in itemavailability:
        print("Your item is available")
    else:
        print("Your item is not available")
    pass
menu()