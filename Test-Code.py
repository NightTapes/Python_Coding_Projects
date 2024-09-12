h = "of Hearts"
c = "of Clubs"
d = "of Diamonds"
s = "of Spades" # variables which can be added to the ints of the card numbers so they can be used in math

cards = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
]

import random # imports the random function I guess?? Ask about this
random.shuffle(cards)

player_deck_A = [
    cards[0], cards[1], cards[2], cards[3], cards[4], cards[5], cards[6], cards[7], cards[8], cards[9], 
    cards[10], cards[11], cards[12], cards[13], cards[14], cards[15], cards[16], cards[17], cards[18],  
    cards[19], cards[20], cards[21], cards[22], cards[23], cards[24], cards[25]
]

program_deck_A = [
    cards[26], cards[27], cards[28], cards[29], cards[30], cards[31], cards[32], cards[33], cards[34],  
    cards[35], cards[36], cards[37], cards[38], cards[39], cards[40], cards[41], cards[42], cards[43],   
    cards[44], cards[45], cards[46], cards[47], cards[48], cards[49], cards[50], cards[51]
]

player_deck_B = []
program_deck_B = []

print(f"There are {len(player_deck_A)} cards left in you deck.")

while (player_deck_A or program_deck_A):

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
    print(f"There are {len(program_deck_B)} cards in the programs winning deck.")

