

# keep them as only int values 
# list so can have duplicates of values up to 13
# assign the "of hearts" after a card is drawn, so can do logic

h = "of Hearts"
c = "of Clubs"
d = "of Diamonds"
s = "of Spades"

cards = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
]

print(cards)

import random
random.shuffle(cards)

print(cards)

player_deck = [
    cards[0], cards[1], cards[2], cards[3], cards[4], cards[5], cards[6], cards[7], cards[8], cards[9], 
    cards[10], cards[11], cards[12], cards[13], cards[14], cards[15], cards[16], cards[17], cards[18],  
    cards[19], cards[20], cards[21], cards[22], cards[23], cards[24], cards[25]
]

program_deck = [
    cards[26], cards[27], cards[28], cards[29], cards[30], cards[31], cards[32], cards[33], cards[34],  
    cards[35], cards[36], cards[37], cards[38], cards[39], cards[40], cards[41], cards[42], cards[43],   
    cards[44], cards[45], cards[46], cards[47], cards[48], cards[49], cards[50], cards[51]
]

print(player_deck)
print(program_deck)
print(type(player_deck[0]))
print(type(program_deck[0]))

print(f"There are {len(player_deck)} cards left in you deck.")

input("Press 'Enter' to draw a card.")

print(f"You drew {player_deck[0]}.")
player_drawn_card = (player_deck[0])
print(f"The computer drew {program_deck[0]}.")
program_drawn_card = (program_deck[0])

print(type(player_drawn_card))
print(type(program_drawn_card))

if (player_drawn_card > program_drawn_card):
    print("You drew the highest card. You win this round!")
elif (player_drawn_card < program_drawn_card):
    print("You drew the lowest card. You lose this round.")
elif (player_drawn_card == program_drawn_card):
    print("Both drew cards of equal value. Try again.")
else:
    print("Something really weird must have happened for this to come up.")

