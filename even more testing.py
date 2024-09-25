cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

suffix = ["of Hearts", "of Clubs", "of Diamonds", "of Spades"]

for war in cards:
    for complete_cards in suffix:
        print(war, complete_cards)

# with this nested loop i can combine the card values with the suffixes. 