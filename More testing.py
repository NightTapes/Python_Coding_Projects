# 1. List or dict of all 52 cards

h = "of Hearts"
c = "of Clubs"
d = "of Diamonds"
s = "of Spades"

class cards:
    def __init__(self, value, type):
        self.value = value
        self.type = type

    def __str__(self):
        return f"{self.value} {self.type}"

card = []

card += [cards(value, type) for value, type in [
    (1,h), (2,h), (3,h), (4,h), (5,h), (6,h), (7,h), (8,h), (9,h), (10,h), (11,h), (12,h), (13,h),
    (1,c), (2,c), (3,c), (4,c), (5,c), (6,c), (7,c), (8,c), (9,c), (10,c), (11,c), (12,c), (13,c),
    (1,d), (2,d), (3,d), (4,d), (5,d), (6,d), (7,d), (8,d), (9,d), (10,d), (11,d), (12,d), (13,d),
    (1,s), (2,s), (3,s), (4,s), (5,s), (6,s), (7,s), (8,s), (9,s), (10,s), (11,s), (12,s), (13,s)
]]

for obj in card:
    print(obj.value, obj.type, sep=' ')

# 2. Random sorting of the cards (player should not be able to see the result)

import random
random.shuffle(card)
print(card)

# 3. Dividing the randomly sorted cards into 2 new groups/lists/dicts - 1 for the player and 1 for the program - 26 random cards each

