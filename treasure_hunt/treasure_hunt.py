def treasure_hunt():
    print(r'''
    *******************************************************************************
              |                   |                  |                     |
     _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
              |                `"=._o`"=._      _`"=._                     |
     _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
              |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
     _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
    |                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/_____ /
    *******************************************************************************
    ''')
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")
    print("You reach a fork in your path. Do you turn left or right?")
    direction = input("Type 'left' if you want to go left or type 'right' if you want to go right:\n")

    if direction == "right":
        print("You fall into a hidden pit and die. Game Over.")
        exit(0)
    elif direction == "left":
        print("You reach a large lake with no way to go around it. You can try to swim across or wait for a boat")
        lake = input("Type 'swim' if you want to swim across or type 'wait' to wait for a boat to come\n").lower()

        if lake == "swim":
            print("The lake is bigger than you thought. Halfway across the lake, your arms and legs give out and you drown. Game Over.")
            exit(0)
        elif lake == "wait":
            print("A mysterious man in a boat eventually appears and offers you a ride across. You get in.")
            print("After dropping you off on the other side, you walk down the trail until you reach three closed doors.")
            print("The three doors are red, blue, and yellow")
            door = input("Type 'red' to choose the red door or 'blue' for the blue door or 'yellow' for the yellow door:\n").lower()
            if door == "red":
                print("The moment you open the red door, a troll jumps out and wallops you on the head with a club. You died. Gave Over.")
                exit(0)
            elif door == "blue":
                print("The moment you open the blue door, a hidden bomb trap is detonated, killing you instantly. Game Over")
                exit(0)
            elif door == "yellow":
                print("You open the yellow door and peer inside. You see a large treasure chest.")
                print("CONGRATS! You have found the treasure!!!!")
                exit(0)

    print("You did not enter correctly. Game Over")
exit(0)


