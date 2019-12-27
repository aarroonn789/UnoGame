import card

from random import shuffle


class Deck(list):
    def fill_deck(self):

        for color in card.Color:
            # One zero, wild, and wild +4
            self.append(card.Card(0, color))
            self.append(card.Wild())
            self.append(card.WildPlusFour())

            # Two of each number, +2, reverse, and skip cards
            for _ in range(2):
                self.append(card.PlusTwo(color))
                self.append(card.Reverse(color))
                self.append(card.Skip(color))

                for number in range(1, 10):
                    self.append(card.Card(number, color))
    
    def shuffle(self):
        shuffle(self)
        