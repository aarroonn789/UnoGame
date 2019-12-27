import gameController
import card

# controller = gameController.GameController(4)

# controller.setup_game()
# controller.display_hands()

yellow_five = card.Card(5, card.Color.YELLOW)
red_five = card.Card(5, card.Color.RED)
yellow_six = card.Card(6, card.Color.YELLOW)
blue_one = card.Card(1, card.Color.BLUE)
wild = card.WildPlusFour()

wild.action()
