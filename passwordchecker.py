import random # Imported libraries to pause the console, choose random special characters, and to pause the console for user experience.
import string
import time

specialchar = '!£$%^&*#@'
#  Defining functions before program begins, mainly chose to define them first so I could see if something broke immediately and they seemed like the sections I would spend the most amount of time on. """

def userinfo():
    """Collects user information and restarts if input is in the wrong format, without lists or shorthand functions."""
    while True:  # Keeps looping until all inputs are valid, took a lot of time to figure out but worked well.
        print("Welcome to the password generator/ checker, please answer the following questions ")
        time.sleep(1)  # Decided on pausing the console so the user can read the output.

        surname = input("Enter your surname (e.g. McPhee): ").lower() # Getting my family to test I noticed that they were using spaces by default before typing, so decided to strip spaces from any user input.
        year = input("Enter your year of entry (e.g. 25 for 2025): ").strip()
        dob = input("Enter your date of birth (DD/MM/YYYY): ").strip()
        postcode = input("Enter your postcode (e.g. WA11 9BP): ").strip()

        valid = True  # Placeholder to see whether the password generation is correct with inputs from the user.

        if not surname.isalpha():
            print("Surname was entered incorrecly, please only use letters.")
            valid = False

        if not (year.isdigit() and len(year) == 2):
            print("Please enter the last two digits of your entry year (e.g. 25 for 2025).")
            valid = False

        if not (len(dob) == 10 and dob[2] == '/' and dob[5] == '/' and dob.replace('/', '').isdigit()): # Used the square brackets to mark when there would be a / in the DOB.
            print(" Date of birth was entered incorrectly, please input in the form DD/MM/YYYY") # Ensured that each section of a DOB had the correct amount of characters, eg the DD section should at maximum have 2 numbers, so ensured that only 2 numbers were present.
            valid = False

        has_letter = False
        has_number = False

        for character in postcode:
            if character.isalpha():
                has_letter = True
            if character.isdigit():
                has_number = True

        if len(postcode.replace(" ", "")) < 5 or has_letter == False or has_number == False:
            print("Please use a valid format (e.g. WA11 9DW).")
            valid = False

        if not valid:
            print("One of your inputs were invalid, please try again.")
            time.sleep(1)
            continue

        dob = dob.replace("/", "")
        postcode = postcode.replace(" ", "").lower()

        return surname, year, dob, postcode


def generate_password(surname, year, dob, postcode, length=12): # Assignment rule states to use a standardised length of password, chose 12 as it's the most secure without being too long.
    characters = surname + year + dob + postcode + string.ascii_letters + string.digits + specialchar # Realised that the default string library had all alphanumerical characters built in as an option, so decided to use them rather than creating a list of the whole alphabet and numbers.
    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"\nYour generated password is: {password}\n") # Decided for user experience to have the password print on a new line, f strings were used mainly just for readability.
    return password


def check_password(password): # Decided on a scoring system for a password for ease of access for a user rather than a blanket statement telling them their password was either strong enough or not.
    if password.strip() == "":
        print("Please enter a valid password.")
        return
    score = 0
    if len(password) >= 8:
        score += 1

    for character in password:
        if character.islower():
            score += 1
            break

    for character in password:
        if character.isupper():
            score += 1
            break

    for character in password:
        if character.isdigit():
            score += 1
            break

    for character in password:
        if character in "!£$%^&*#@":
            score += 1
            break

    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    print(f"\nPassword strength: {strength}")
    print(f"Score: {score}/5\n")

    if strength == "Weak":
        newpassword = input("Would you like to generate a stronger password? (yes/no) ").lower()
        if newpassword == "yes":
            surname, year, dob, postcode = userinfo()
            generate_password(surname, year, dob, postcode)


def menu():
    while True:
        print("\n Password Checker/Generator ")
        print("1. Generate a password")
        print("2. Check a password")
        print("3. Exit")

        choice = input("Choose an option (1-3) ").strip()

        if choice == "1":
            surname, year, dob, postcode = userinfo()
            generate_password(surname, year, dob, postcode)
        elif choice == "2":
            password = input("Enter the password you want to check ")
            check_password(password)
        elif choice == "3":
            print("Exiting program")
            time.sleep(1)
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

menu()
