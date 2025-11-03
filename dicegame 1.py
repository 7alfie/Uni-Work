import random
print("Welcome to the dice game")
die1 = random.randint(1,6)
die2 = random.randint(1,6)
die3 = random.randint(1,6)
print(f"Die1: {die1}")
print(f"Die2: {die2}")
print(f"Die3: {die3}")

if die1 == die2 and die2 == die3 :
    print("Three of a kind")
    score = 100
    print(f"Your score is {score}")

elif die1 == die2 or die2 == die3 or die1==die3 :
    print("One Pair")
    score = 25
    print(f"Your score is {score}")

elif die1 == 2 or die1 == 4 or die1 == 6 and die2 == 2 or die2 == 4 or die2 == 6 and die3 == 2 or die3 == 4 or die3 == 6 :
    print("All even")
    score = 10
    print(f"Your score is {score}")

elif die1 == 1 or die1 == 3 or die1 == 5 and die2 == 1 or die2 == 3 or die2 == 5 and die3 == 1 or die3 == 3 or die3 == 5 :
    print("All odd")
    score = 10
    print(f"Your score is {score}")
else: print("Better luck next time") 