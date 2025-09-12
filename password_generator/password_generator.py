import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

choices = []
i = 0

#print(random.choice(letters))

while i < nr_letters:
    choices.extend(random.choice(letters))
    i += 1

i = 0
while i < nr_symbols:
    choices.extend(random.choice(symbols))
    i += 1

i = 0
while i < nr_numbers:
    choices.extend(random.choice(numbers))
    i += 1

#print(choices)

password = ""
i = 0
passl = len(choices)

while i < passl:
    random_index = random.randrange(len(choices))
    password = password + choices.pop(random_index)
    i += 1

print(f"Your password is: {password}")


