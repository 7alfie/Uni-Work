name = ['Dave', 'Jeff', 'Mike']
age = [34, 53, 52]
cutlery = ['Fork', 'Spoon', 'Knife']

username = input("Enter your name: ")
userage = int(input("Enter your age: "))
usercutlery = input("Enter your favourite cutlery: ")

name.append(username)
age.append(userage)
cutlery.append(usercutlery)

average_age = sum(age) / len(age)

print("\nList of people and their favourite cutlery:")
for index in range(len(name)):
    print(f"{name[index]} is {age[index]} and likes {cutlery[index]}.")

print(f"The average age is {average_age:.1f}.")
