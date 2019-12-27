from enum import Enum


class Color(Enum):
    RED = 1
    BLUE = 2
    YELLOW = 3
    GREEN = 4

    def __gt__(self, other):
        if other == None:
            return False
        return self.value > other.value

    def __lt__(self, other):
        if other == None:
            return True
        return self.value < other.value
    

class Card:
    def __init__(self, value, color):
        self.color = color
        self.value = value

    def play_card(self):
        return True

    def can_play_card(self, last_played):
        return self.color == last_played.color or self.value == last_played.value

    def __str__(self):
        return "{:<8} {:<15}".format(self.color.name, self.value)

    def __gt__(self, other):
        if self.color == other.color:
            return self.value > other.value
        return self.color > other.color

    def __lt__(self, other):
        if self.color == other.color:
            return self.value < other.value
        return self.color < other.color


class Skip(Card):
    def __init__(self, color):
        super().__init__(-1, color)
    
    def __str__(self):
        return "{:<8} SKIP".format(self.color.name)


class Reverse(Card):
    def __init__(self, color):
        super().__init__(-1, color)

    def __str__(self):
        return "{:<8} REVERSE".format(self.color.name)


class PlusTwo(Card):
    def __init__(self, color):
        super().__init__(-1, color)

    def __str__(self):
        return "{:<8} PLUS TWO".format(self.color.name)


class Wild(Card):
    def __init__(self):
        super().__init__(-1, Color.RED)

    def play_card(self):
        color_choice = input("Enter a color for the wild card (R/G/B/Y): ").lower()
        if color_choice == 'r':
            self.color = Color.RED
        elif color_choice == 'g':
            self.color = Color.GREEN
        elif color_choice == 'b':
            self.color = Color.BLUE
        elif color_choice == 'y':
            self.color = Color.YELLOW
        else:
            print("You're pretty stupid.")

    def can_play_card(self, last_played):
        return True

    def __str__(self):
        return "WILD"


class WildPlusFour(Wild):
    def __str__(self):
        return "WILD PLUS 4"
