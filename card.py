from enum import Enum

# Enumerator to store color value
class Color(Enum):
    RED = 1
    BLUE = 2
    YELLOW = 3
    GREEN = 4

    # Greater than and less than compare the Color Enumerator value
    def __gt__(self, other):
        if other == None:
            return False
        return self.value > other.value

    def __lt__(self, other):
        if other == None:
            return True
        return self.value < other.value


# Card is basic uno playing card
class Card:
    def __init__(self, value, color):
        # Color and value (number) of card
        self.color = color
        self.value = value

    # Action is called whenever the card is played. Handles special actions for cards like Wild card and Skip cards. Returns dict of attributes to update.
    def action(self):
        return True

    def __str__(self):
        return "{:<8} {:<15}".format(self.color.name, self.value)

    # Greater than and less than compare by color first then by value.
    def __gt__(self, other):
        if self.color == other.color:
            return self.value > other.value
        return self.color > other.color

    def __lt__(self, other):
        if self.color == other.color:
            return self.value < other.value
        return self.color < other.color


# Skip card
class Skip(Card):
    def __init__(self, color):
        super().__init__(-1, color)

    # Inform the game controller to skip the next turn
    def action(self):
        return {"skip_next_player": True}

    def __str__(self):
        return "{:<8} SKIP".format(self.color.name)


# Reverse card
class Reverse(Card):
    def __init__(self, color):
        super().__init__(-1, color)

    # Inform the game controller to reverse the direction of play
    def action(self):
        return {"reverse_direction_of_play": True}

    def __str__(self):
        return "{:<8} REVERSE".format(self.color.name)


class PlusTwo(Card):
    def __init__(self, color):
        super().__init__(-1, color)

    # Inform game controller to skip the next player and have the next player draw 2 cards
    def action(self):
        return {"skip_next_player": True, "draw_next_player": 2}

    def __str__(self):
        return "{:<8} PLUS TWO".format(self.color.name)


class Wild(Card):
    def __init__(self):
        super().__init__(-1, Color.RED)

    # Prompt user to set color for wild card
    def _set_color_(self):
        self.color = None
        print(self.color)
        while self.color == None:
            color_choice = input("Enter a color for the wild card (R/G/B/Y): ").lower()
            if color_choice == "r":
                self.color = Color.RED
            elif color_choice == "g":
                self.color = Color.GREEN
            elif color_choice == "b":
                self.color = Color.BLUE
            elif color_choice == "y":
                self.color = Color.YELLOW

    # Have user set the color of the Wild card
    def action(self):
        self._set_color_()
        return {}

    def __str__(self):
        return "WILD"


class WildPlusFour(Wild):
    def __str__(self):
        return "WILD PLUS 4"

    # Set color and inform game controller to have the next player draw 4 cards
    def action(self):
        self._set_color_()
        return {"draw_next_player": 4}
