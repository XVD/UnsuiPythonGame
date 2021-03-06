#----- Base Python imports ------#

#----- Unsui imports ------#
import user_input
from GameInstance import GameInstance

player_game = GameInstance()

def upper_main(player_game, input=raw_input):
    """
    This loop should never exit.
    Exception: if the player specifies to exit
    """
    user_input.opening_setup(player_game,input)
    while True:
        user_action = user_input.request_action(player_game,input)
        player_game.take_action(user_action)



#------- Game Operation --------#
upper_main(player_game)
