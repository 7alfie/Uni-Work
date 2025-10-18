"""
Python Error Practice
---------------------
Each section below contains one or more errors.
Run the code, read the error message, and debug it.
Add comments in the boxes saying what the error was,
what was wrong and how you fixed it.
"""

# ----------------------------------------------------
# 
# ----------------------------------------------------


print("I want this to appear on the screen")


# ----------------------------------------------------
# The bracket was never closed, Syntax Error, fixed by adding bracket to the end.
# ----------------------------------------------------

string = "A word" 
print(string[3]) 


# ----------------------------------------------------
# The string doesn't have twelve characters to find an index, fixed by changing index.
# ----------------------------------------------------

something = 'Hi there!'
print(something)


# ----------------------------------------------------
# Variable is declared after the print statement, fixed by swapping them around. NameError
# ----------------------------------------------------

result = 10 / 2
print(result)

# ----------------------------------------------------
# Impossible to divide by 0 as it is undefined. ZeroDivisionError, fixed by dividing by another number that isn't 0
# ----------------------------------------------------

# Find the sum of three numbers
a, b, c = 4, 6, 8
total = (a + b + c) 
print("Sum ", total)

# ----------------------------------------------------
# Logic error, the sum would be the total of all 3, doesn't need to be divided by 2. Fixed by changing to add all 3 and removing divide.
# ----------------------------------------------------


total = 5 + 10 
print(total)

# ----------------------------------------------------
# TypeError: Can't add a string onto an integer, fixed by removing " either side.
# ----------------------------------------------------

x = 'a'
print(x.upper())

# ----------------------------------------------------
# Can't find the upper case of a number, changed to be a character/string, and no print statement of letter/string.
# ----------------------------------------------------

num = int("4")  
print(num)

# num is equal to a string, which is not an integer, changed to be an integer

"""
Try and Except Practice
-----------------------
Task:

Uncomment the code parts 

Complete the code to prevent the program from crashing.

"""

# ----------------------------------------------------
# Example — Basic try/except
# ----------------------------------------------------
#print("Handling a ValueError")

#try:
  #  number = int(input("Enter a number: "))
 #   print("You entered:", number)
      
#except ValueError:
#    print("That’s not a valid number! Please enter digits only.") 


# ----------------------------------------------------
# Task 1 — Divide by zero
# ----------------------------------------------------
#print("Handle ZeroDivisionError")

# Add a try/except block around the code below
# so the program prints a message instead of crashing.

#try:
   # number = int(input("Enter a number to divide 10 by "))
    #result = 10 / number
#except ZeroDivisionError:
 #   print("You entered something wrong, please try again")

#print(f"Result is {result}")


# ----------------------------------------------------
# Task 2 — Handle any ValueError when converting to int
# ----------------------------------------------------
print("Task 2: Handle ValueError")

# Add a try/except block to catch the error when the user
# enters something that isn’t a number
try:
 age = int(input("Enter your age: "))
 print("Next year you’ll be", age + 1)

except ValueError:
    print("That's not a valid input, try again")
# ----------------------------------------------------
# Task 3 — Multiple except blocks
# ----------------------------------------------------
print("Handle different errors")

# Add multiple except blocks for:
#   - ZeroDivisionError
#   - ValueError
# The code should print a different message for each error type.

# number = int(input("Enter a number: "))
# result = 100 / number
# print("Answer ", result)


# ----------------------------------------------------
# Task 4 — Using else and finally
# ----------------------------------------------------
print("Add else and finally blocks")

#  Complete the code so that:
#   - If no error happens, it prints “No errors! Result = ...”
#   - The finally block prints “Finished calculation.” no matter what.

# try:
#     number = int(input("Enter a number: "))
#     result = 10 / number
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# ADD else and finally here



