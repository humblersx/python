from game_data import data
import random

logo = r"""
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = r"""
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""




print(logo)



correct = True
score = 0
personB = random.choice(data)

while correct:
    # Select A and B persons and print initial comparison. A and B must be different
    personA = personB.copy()
    personB = random.choice(data)

    while personA["name"] == personB["name"]:
        personB = random.choice(data)

    print(f"Compare A: {personA["name"]}, {personA["description"]}, from {personA["country"]}")
    print(vs)
    print(f"Against B: {personB["name"]}, {personB["description"]}, from {personB["country"]}")

    # Ask who has more followers and assign to variable
    answer = input("Who has more followers? Type 'A' or 'B': ").upper()

    if answer != 'A' and answer != 'B':
        exit("You have entered an invalid answer.")

    if answer == 'A':
        if personA["follower_count"] > personB["follower_count"]:
            correct = True
            score += 1
            print(f"You're right! Current Score: {score}")

        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            correct = False
    elif answer == 'B':
        if personB["follower_count"] > personA["follower_count"]:
            correct = True
            score += 1
            print(f"You're right! Current Score: {score}")

        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            correct = False





