cards = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
]

h = "of Hearts"
c = "of Clubs"
d = "of Diamonds"
s = "of Spades"

import random
random.shuffle(cards)

player_deck_A = (cards[0:26])
program_deck_A = (cards[26:52])
print(player_deck_A)
print(len(player_deck_A))
print(program_deck_A)
print(len(program_deck_A))


while listlength<len(player_deck_A) or listlength<len(program_deck_A):

    input("Press 'Enter' to draw a card.")

    print(f"You drew {player_deck_A[0]}.")
    player_drawn_card = (player_deck_A[0])
    print(f"The computer drew {program_deck_A[0]}.")
    program_drawn_card = (program_deck_A[0])

    if (player_drawn_card > program_drawn_card):
        print("You drew the highest card. You win this round!")
    elif (player_drawn_card < program_drawn_card):
        print("You drew the lowest card. You lose this round.")
    elif (player_drawn_card == program_drawn_card):
        print("You both drew cards of equal value.")
    else:
        print("Something really weird must have happened for this to come up.")

    input("Press 'Enter' to continue.")

    if (player_drawn_card > program_drawn_card):
        player_deck_B.insert(0, player_drawn_card)
        player_deck_B.insert(0, program_drawn_card)
        player_deck_A.pop(0)
        program_deck_A.pop(0)
        print("Both cards have been added to your winning deck.")
    elif (player_drawn_card < program_drawn_card):
        program_deck_B.insert(0, player_drawn_card)
        program_deck_B.insert(0, program_drawn_card)
        player_deck_A.pop(0)
        program_deck_A.pop(0)
        print("Both cards have been added to the programs winning deck.")
    elif (player_drawn_card == program_drawn_card):
        random.shuffle(player_deck_A)
        random.shuffle(program_deck_A)
        print("Both decks have been re-shuffled. Try again.")
    else:
        print("Something really weird must have happened for this to come up.")
        exit()

    print(f"There are {len(player_deck_A)} cards left in you deck.")
    print(f"There are {len(program_deck_A)} cards left in the programs deck.")
    print(f"There are {len(player_deck_B)} cards in your winning deck.")
    print(f"There are {len(program_deck_B)} cards in the programs winning deck.") # these need to be added to if statements

print("Your main deck is empty. You are now using your winning deck.")

while listlength<len(player_deck_B) or listlength<len(program_deck_B):
    
    input("Press 'Enter' to draw a card.")

    print(f"You drew {player_deck_B[0]}.")
    player_drawn_card = (player_deck_B[0])
    print(f"The computer drew {program_deck_B[0]}.")
    program_drawn_card = (program_deck_B[0])

    if (player_drawn_card > program_drawn_card):
        print("You drew the highest card. You win this round!")
    elif (player_drawn_card < program_drawn_card):
        print("You drew the lowest card. You lose this round.")
    elif (player_drawn_card == program_drawn_card):
        print("You both drew cards of equal value.")
    else:
        print("Something really weird must have happened for this to come up.")

    input("Press 'Enter' to continue.")

    if (player_drawn_card > program_drawn_card):
        player_deck_A.insert(0, player_drawn_card)
        player_deck_A.insert(0, program_drawn_card)
        player_deck_B.pop(0)
        program_deck_B.pop(0)
        print("Both cards have been added to your winning deck.")
    elif (player_drawn_card < program_drawn_card):
        program_deck_A.insert(0, player_drawn_card)
        program_deck_A.insert(0, program_drawn_card)
        player_deck_B.pop(0)
        program_deck_B.pop(0)
        print("Both cards have been added to the programs winning deck.")
    elif (player_drawn_card == program_drawn_card):
        random.shuffle(player_deck_B)
        random.shuffle(program_deck_B)
        print("Both decks have been re-shuffled. Try again.")
    else:
        print("Something really weird must have happened for this to come up.")
        exit()

    print(f"There are {len(player_deck_B)} cards left in you deck.")
    print(f"There are {len(program_deck_B)} cards left in the programs deck.")
    print(f"There are {len(player_deck_A)} cards in your winning deck.")
    print(f"There are {len(program_deck_A)} cards in the programs winning deck.")

# the program now stops when either the player or the computer runs out of cards. Not when they've actually won.
