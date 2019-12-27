import card


class Hand(list):
    def __init__(self, name):
        self.name = name
    def draw_card(self, deck):
        self.append(deck.pop())
    
    def display_hand(self):
        print('{}\'s Hand:'.format(self.name))
        for card in self:
            print("  " + str(card))