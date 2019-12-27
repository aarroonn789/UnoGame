from deck import Deck
from hand import Hand

class GameController():
    def __init__(self, player_count):
        self.game_deck = Deck()
        self.game_deck.fill_deck()
        self.game_deck.shuffle()

        self.discard_deck = Deck()

        self.player_hands = []

        for _ in range(player_count):
            self.player_hands.append(Hand(input("Enter name of player: ")))

    def setup_game(self):
        for _ in range(7):
            for hand in self.player_hands:
                hand.draw_card(self.game_deck)

    def display_hands(self):
        for hand in self.player_hands:
            hand.display_hand()