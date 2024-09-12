# 1. List of all 52 cards.

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

# at some point change the DISPLAYED value of 10, 11, 12, and 13 index values so it just displays "King of hearts" etc. while still retaining 
# its value so it can be used in logic operations and math

#-------------------------------------------------------------------------------------------------------------------------------------------

# 2. Random sorting of the cards (player should not be able to see the result).

import random # imports the random function I guess?? Ask about this
random.shuffle(cards) # randomly shuffles the elements inside the full_deck list
#print(full_deck)

#-------------------------------------------------------------------------------------------------------------------------------------------

# 3. Dividing the randomly sorted cards into 2 new groups/lists/dicts - 1 for the player and 1 for the program - 26 random cards each.

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
program_deck_B = [] # lists for won cards. empty as of now, but is filled with the winning cards after each round.

#-------------------------------------------------------------------------------------------------------------------------------------------

# 4. The player cannot see their cards, only how many cards they have left in their deck.

print(f"There are {len(player_deck_A)} cards left in you deck.")

#-------------------------------------------------------------------------------------------------------------------------------------------

# 5. The player is prompted to draw a card, "press enter to draw a card".

while (player_deck_A or program_deck_A): # This code might need to change, but it seems to work as of now. Just loops whats indented below.
# all the way down to and including # 8.
    input("Press 'Enter' to draw a card.")

#-------------------------------------------------------------------------------------------------------------------------------------------

# 6. When enter is pressed, the first card from each deck (players and the programs) is printed out.

    print(f"You drew {player_deck_A[0]}.")
    player_drawn_card = (player_deck_A[0])
    print(f"The computer drew {program_deck_A[0]}.")
    program_drawn_card = (program_deck_A[0]) # storing the drawn cards in variables so we can do logic operations with them

#-------------------------------------------------------------------------------------------------------------------------------------------

# 7. The program checks which of the 2 drawn cards has the highest value, and declares the winner.

    if (player_drawn_card > program_drawn_card):
        print("You drew the highest card. You win this round!")
    elif (player_drawn_card < program_drawn_card):
        print("You drew the lowest card. You lose this round.")
    elif (player_drawn_card == program_drawn_card):
        print("You both drew cards of equal value.")
    else:
        print("Something really weird must have happened for this to come up.")

#-------------------------------------------------------------------------------------------------------------------------------------------

# 8. Both cards are then added to a new deck - the winners deck.

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

#-------------------------------------------------------------------------------------------------------------------------------------------

# 9. cards are drawn until one or both players run out of cards in their first deck.

# This is the "while loop" in # 5.

#-------------------------------------------------------------------------------------------------------------------------------------------

# 11. When this happens the winning deck goes into the rotation, and cards start being drawn from there.

