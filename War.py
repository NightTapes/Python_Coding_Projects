# 1. List or dict of all 52 cards

h = "of Hearts"
c = "of Clubs"
d = "of Diamonds"
s = "of Spades" # variables which can be added to the ints of the card numbers so they can be used in math

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

full_deck = [
    (f"{cards[0]}, {h}"), (f"{cards[1]}, {h}"), (f"{cards[2]}, {h}"), (f"{cards[3]}, {h}"), (f"{cards[4]}, {h}"), (f"{cards[5]}, {h}"), (f"{cards[6]}, {h}"),
    (f"{cards[7]}, {h}"), (f"{cards[8]}, {h}"), (f"{cards[9]}, {h}"), (f"{cards[10]}, {h}"), (f"{cards[11]}, {h}"), (f"{cards[12]}, {h}"),
    (f"{cards[0]}, {c}"), (f"{cards[1]}, {c}"), (f"{cards[2]}, {c}"), (f"{cards[3]}, {c}"), (f"{cards[4]}, {c}"), (f"{cards[5]}, {c}"), (f"{cards[6]}, {c}"),
    (f"{cards[7]}, {c}"), (f"{cards[8]}, {c}"), (f"{cards[9]}, {c}"), (f"{cards[10]}, {c}"), (f"{cards[11]}, {c}"), (f"{cards[12]}, {c}"),
    (f"{cards[0]}, {d}"), (f"{cards[1]}, {d}"), (f"{cards[2]}, {d}"), (f"{cards[3]}, {d}"), (f"{cards[4]}, {d}"), (f"{cards[5]}, {d}"), (f"{cards[6]}, {d}"),
    (f"{cards[7]}, {d}"), (f"{cards[8]}, {d}"), (f"{cards[9]}, {d}"), (f"{cards[10]}, {d}"), (f"{cards[11]}, {d}"), (f"{cards[12]}, {d}"),
    (f"{cards[0]}, {s}"), (f"{cards[1]}, {s}"), (f"{cards[2]}, {s}"), (f"{cards[3]}, {s}"), (f"{cards[4]}, {s}"), (f"{cards[5]}, {s}"), (f"{cards[6]}, {s}"),
    (f"{cards[7]}, {s}"), (f"{cards[8]}, {s}"), (f"{cards[9]}, {s}"), (f"{cards[10]}, {s}"), (f"{cards[11]}, {s}"), (f"{cards[12]}, {s}"),
]
#print(full_deck)
# at some point change the DISPLAYED value of 10, 11, 12, and 13 index values so it just displays "King of hearts" etc. while still retaining 
# its value so it can be used in logic operations and math
#print(len(full_deck)) # can see we now have our 52 playing cards
#print(full_deck[51]) # prints the correct card - an int plus its string

#-------------------------------------------------------------------------------------------------------------------------------------------

# 2. Random sorting of the cards (player should not be able to see the result)

import random # imports the random function I guess?? Ask about this
random.shuffle(full_deck) # randomly shuffles the elements inside the full_deck list
#print(full_deck)

#-------------------------------------------------------------------------------------------------------------------------------------------

# 3. Dividing the randomly sorted cards into 2 new groups/lists/dicts - 1 for the player and 1 for the program - 26 random cards each

player_deck = [
    full_deck[0], full_deck[1], full_deck[2], full_deck[3], full_deck[4], full_deck[5], full_deck[6], full_deck[7], full_deck[8], full_deck[9], 
    full_deck[10], full_deck[11], full_deck[12], full_deck[13], full_deck[14], full_deck[15], full_deck[16], full_deck[17], full_deck[18],  
    full_deck[19], full_deck[20], full_deck[21], full_deck[22], full_deck[23], full_deck[24], full_deck[25]
    ]

program_deck = [
    full_deck[26], full_deck[27], full_deck[28], full_deck[29], full_deck[30], full_deck[31], full_deck[32], full_deck[33], full_deck[34],  
    full_deck[35], full_deck[36], full_deck[37], full_deck[38], full_deck[39], full_deck[40], full_deck[41], full_deck[42], full_deck[43],   
    full_deck[44], full_deck[45], full_deck[46], full_deck[47], full_deck[48], full_deck[49], full_deck[50], full_deck[51]
    ]

print(type(player_deck[0])) # from the full_deck to here it all becomes a string. Gotta fix that.
#print(program_deck)

#-------------------------------------------------------------------------------------------------------------------------------------------

# 4. The player cannot see their cards, only how many cards they have left in their deck

print(f"There are {len(player_deck)} cards left in you deck.")
#player_deck.remove(player_deck[4])
#print(f"There are {len(player_deck)} cards left in you deck.") # Checking if everything works.

#-------------------------------------------------------------------------------------------------------------------------------------------

# 5. The player is prompted to draw a card, "press enter to draw a card"

input("Press 'Enter' to draw a card.")

#-------------------------------------------------------------------------------------------------------------------------------------------

# 6. When enter is pressed, the first card from each deck (players and the programs) is printed out

print(f"You drew {player_deck[0]}.")
player_drawn_card = (player_deck[0])
print(f"The computer drew {program_deck[0]}.")
program_drawn_card = (program_deck[0]) # storing the drawn cards in variables so we can do logic operations with them



import re
int(re.search(r'\d+', player_drawn_card).group())
int(re.search(r'\d+', program_drawn_card).group())
print(type(player_drawn_card))
print(type(program_drawn_card))
#-------------------------------------------------------------------------------------------------------------------------------------------

# 7. The program checks which of the 2 drawn cards has the highest value, and declares the winner

if (player_drawn_card > program_drawn_card):
    print("You drew the highest card. You win this round!")
elif (player_drawn_card < program_drawn_card):
    print("You drew the lowest card. You lose this round.")
elif (player_drawn_card == program_drawn_card):
    print("Both drew cards of equal value. Try again.")
else:
    print("Something really weird must have happened for this to come up.")

# gotta figure out what to do when the card values are equal