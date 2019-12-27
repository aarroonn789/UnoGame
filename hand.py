import card

# Hand is subclass of List. Used to store cards for players
class Hand(list):
    def __init__(self, name):
        self.name = name

    # Removes top card of deck and adds it to the hand
    def draw_card(self, deck):
        self.append(deck.pop())

    def display_hand(self):
        print("{}'s Hand:".format(self.name))
        for card in self:
            print("  " + str(card))
