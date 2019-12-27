import card

from random import shuffle

# Deck is subclass of List and holds cards that are not in a hand
class Deck(list):

    # Fills the deck with the standard 108 uno cards
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

    # Randomly shuffles the deck
    def shuffle(self):
        shuffle(self)

