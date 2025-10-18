# ----------------------------------------------------
# Task 3 — Multiple except blocks
# ----------------------------------------------------
print("Handle different errors")

# Add multiple except blocks for:
#   - ZeroDivisionError
#   - ValueError
# The code should print a different message for each error type.
try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print("Answer ", result)
 
except ZeroDivisionError:
     print("We can't divide by 0 please try again")
except ValueError:
        print("This isn't a number please try again")


