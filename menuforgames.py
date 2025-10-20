import time
import random
def menu():
    print("""
    Select a program to run
    1. Alphabet 
    2. Cat Convertor 
    3. Circle Calculator
    """ )
    choice = input("Enter your number")
    if choice == '1':
        alphabet()
    elif choice == '2' :
        catconverter()
    elif choice == '3' :
        circlecalc()
    else:
        print('Invalid')
    
def alphabet() :
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    player = str(input("Enter the alphabet in one word"))
    if player != alphabet:
                 print("You typed this wrong please try again")
    else:
        print("You completed this in x seconds")
    pass
    menu()

def catconverter():
    age = int(input("Enter your cats age in human years "))
    if age == 1:
        humanage= 15
    elif age == 2:
        humanage = 24
    else:
        humanage = 24 + 4 * (age - 2)
    if age < 0.5:
        print("Your cat is in the kitten stage of its life.")
    elif age <= 2:
        print("Your cat is in the junior stage of its life.")
    elif age <= 6:
        print("Your cat is in the prime stage of its life.")
    elif age <= 10:
        print("Your cat is in the mature stage of its life.")
    elif age <= 14:
        print("Your cat is in the senior stage of its life.")
    elif age <= 20:
        print("Your cat is in the geriatric stage of its life.") 
    else: 
        print("Your cat is in the geriatric stage of its life.")


def circlecalc():
    diameter = float(input("Enter the diameter of the circle"))
    theta = int(input("Enter the angle of the arc"))
    radius = diameter / 2
    area = radius * radius * 3.14
    circ = round(diameter * 3.14)
    arclength = round(circ * theta) / 360
    print("Your radius is" , radius , "Your area is" , area , "Your circumference is" , circ , "And your arc length is" , arclength)
    
menu()