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

player_deck_A = (cards[0:26])
program_deck_A = (cards[26:52])

player_deck_B = []
program_deck_B = []

print("Welcome to War! You will be playing against the computer.")
print(f"There are {len(player_deck_A)} cards left in you deck.")
print(f"There are {len(program_deck_A)} cards left in the programs deck.")

listlength = 0

while (listlength<len(player_deck_A) or listlength<len(player_deck_B)) or (listlength<len(program_deck_A) or listlength<len(program_deck_B)):

    input("Press 'Enter' to draw a card.")

    if (listlength!=len(player_deck_A)) == True:
        print(f"You drew {player_deck_A[0]}.")
        player_drawn_card = (player_deck_A[0])
    if (listlength!=len(program_deck_A)) == True:
        print(f"The computer drew {program_deck_A[0]}.")
        program_drawn_card = (program_deck_A[0])
    if (listlength!=len(player_deck_B)) == True:
        print(f"You drew {player_deck_B[0]}.")
        player_drawn_card = (player_deck_B[0])
    if (listlength!=len(program_deck_B)) == True:
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

    if (player_drawn_card > program_drawn_card) and listlength!=len(player_deck_A): # decks A
        player_deck_B.insert(0, player_drawn_card)
        player_deck_B.insert(0, program_drawn_card) 
        player_deck_A.pop(0)
        program_deck_A.pop(0) # these might cause problems
        print("Both cards have been added to your winning deck.")
    elif (player_drawn_card < program_drawn_card) and listlength!=len(program_deck_A): # decks A
        program_deck_B.insert(0, player_drawn_card)
        program_deck_B.insert(0, program_drawn_card)
        program_deck_A.pop(0)
        player_deck_A.pop(0) # these might cause problems
        print("Both cards have been added to the programs winning deck.")
    elif (player_drawn_card > program_drawn_card) and listlength!=len(player_deck_B): # decks B
        player_deck_A.insert(0, player_drawn_card)
        player_deck_A.insert(0, program_drawn_card) 
        player_deck_B.pop(0)
        program_deck_B.pop(0) # these might cause problems
        print("Both cards have been added to your winning deck.")
    elif (player_drawn_card < program_drawn_card) and listlength!=len(program_deck_B): # decks B
        program_deck_A.insert(0, player_drawn_card)
        program_deck_A.insert(0, program_drawn_card)
        program_deck_B.pop(0)
        player_deck_A.pop(0) # these might cause problems
        print("Both cards have been added to the programs winning deck.")
    elif (player_drawn_card == program_drawn_card):
        random.shuffle(player_deck_A)
        random.shuffle(program_deck_A)
        print("Both decks have been re-shuffled. Try again.")
    else:
        print("Something really weird must have happened for this to come up.")
        exit()

    if listlength==len(player_deck_B):
        print(f"There are now {len(player_deck_A)} cards left in you deck.")
        print(f"There are now {len(player_deck_B)} cards in your winning deck.")
    if listlength==len(program_deck_B):
        print(f"There are now {len(program_deck_A)} cards left in the programs deck.")
        print(f"There are now {len(program_deck_B)} cards in the programs winning deck.")
    if listlength==len(player_deck_A):
        print(f"There are now {len(player_deck_B)} cards left in you deck.")
        print(f"There are now {len(player_deck_A)} cards in your winning deck.")
    if listlength==len(program_deck_A):
        print(f"There are now {len(program_deck_B)} cards left in the programs deck.")
        print(f"There are now {len(program_deck_A)} cards in the programs winning deck.")



if listlength==len(player_deck_A) and listlength==len(player_deck_B):
    print("You Lost!")
    exit()
if listlength==len(program_deck_A) and listlength==len(program_deck_B):
    print("You won!")
    exit()