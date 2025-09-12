
import random
import emoji

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

playing = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")

def ace_to_one(cardlist):
    for i in range(len(cardlist)):
        if cardlist[i] == 11:
            cardlist[i] = 1
            return cardlist



while playing == 'y':
    print("\n" * 20)
    print(logo)

    my_cards = []
    comp_cards = []

    # First Card
    my_cards.append(random.choice(cards))
    #my_cards.append(11)
    # Second card
    my_cards.append(random.choice(cards))

    # Computer first card
    comp_cards.append(random.choice(cards))
    #comp_cards.append(11)
    # Computer second card
    comp_cards.append(random.choice(cards))
    #comp_cards.append(11)
    #print(f"DEBUG: comp_cards = {comp_cards}")
    comp_score = comp_cards[0] + comp_cards[1]
    current_score = my_cards[0] + my_cards[1]

    if comp_score == 21:
        print("Opponent has Blackjack! Opponent wins \U0001F624")
        playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        continue
    elif current_score == 21:
        print("You have Blackjack! You win \U0001F604")
        playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        continue

    if current_score > 21 and 11 in my_cards:
        my_cards = ace_to_one(my_cards)
        current_score = my_cards[0] + my_cards[1]
    if comp_score > 21 and 11 in comp_cards:
        comp_cards = ace_to_one(comp_cards)
        comp_score = comp_cards[0] + comp_cards[1]


    #print(f"DEBUG: current_score: {current_score}, comp_score: {comp_score}")
    print(f"Your cards: {my_cards}, current score: {current_score}")
    print(f"Computer's first card: {comp_cards[0]}")
    hit_me = input("Type 'y' to get another card, type 'n' to pass: ")
    # counter for my_cards
    n = 2
    # Hit me on cards until I pass or bust
    while hit_me == 'y':
        my_cards.append(random.choice(cards))
        current_score += my_cards[n]

        if current_score > 21 and 11 in my_cards:
           # if 11 in my_cards:
            my_cards = ace_to_one(my_cards)
            current_score = 0
            for each in my_cards:
                current_score += each
            print(f"Your cards: {my_cards}, current score: {current_score}")
            print(f"Computer's first card: {comp_cards[0]}")
            n += 1
            hit_me = input("Type 'y' to get another card, type 'n' to pass: ")
        elif current_score > 21:
            print(f"Your final hand: {my_cards}, final score: {current_score}")
            print(f"Computer's final hand: {comp_cards[0]}, final score: {comp_cards[0]}")
            print("You went over. You lose \U0001F622")
            hit_me = 'n'
            playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
            break
        else:
            print(f"Your cards: {my_cards}, current score: {current_score}")
            print(f"Computer's first card: {comp_cards[0]}")
            n += 1
            hit_me = input("Type 'y' to get another card, type 'n' to pass: ")
    if current_score > 21:
        continue
    # counter for comp_cards
    c = 2
    while comp_score < 17:
        comp_cards.append(random.choice(cards))
        comp_score += comp_cards[c]
        if comp_score > 21 and 11 in comp_cards:
            comp_cards = ace_to_one(comp_cards)
            comp_score = 0
            for each in comp_cards:
                comp_score += each

        elif comp_score> 21:
            print(f"Your final hand: {my_cards}, final score: {current_score}")
            print(f"Computer's final hand: {comp_cards}, final score: {comp_score}")
            print("Opponent went over. You win \U0001F604")
            playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
            break
        c += 1

    if comp_score > 21:
        continue

    print(f"Your final hand: {my_cards}, final score: {current_score}")
    print(f"Computer's final hand: {comp_cards}, final score: {comp_score}")
    if 21 >= current_score > comp_score:
        print("You win \U0001F604")
    elif current_score == comp_score:
        print("Draw \U0001F643")
    elif 21 >= comp_score > current_score :
        print("Opponent wins \U0001F624")

    playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")






