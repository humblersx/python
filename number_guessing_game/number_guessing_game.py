import random

logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""
print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

answer = random.randint(1, 100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
    guesses = 10
    print("You have 10 attempts remaining to guess the number.")
elif difficulty == "hard":
    guesses = 5
    print("You have 5 attempts remaining to guess the number.")
else:
    exit("You have entered an incorrect entry.")

guess = int(input("Make a guess: "))

while guesses > 1:
    guesses -= 1
    if guess > answer:
        print(f"Too high.\nGuess again.\nYou have {guesses} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
    elif guess < answer:
        print(f"Too low.\nGuess again.\nYou have {guesses} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
    else:
        print(f"You got it! The answer was {answer}")
        exit()


print("You have run out of guesses. Refresh the page to run again.")




