from files.game import *
from files.ai import *
from files.gui import *

def game_one_player_first(game):
    """run game with one player and one computer
    when the player starts"""
    game.two_ai = False
    game.player1_type = PLAYER
    game.player2_type = AI
    game.ai_is_first = False
    game.enable_button = True
    game.player_vs_computer = True

def game_one_player_second(game):
    """run game with one player, and one computer
    when the computer starts"""
    game.two_ai = False
    game.player1_type = AI
    game.player2_type = PLAYER
    game.ai_is_first = True
    game.enable_button = False
    game.player_vs_computer = True

def two_computers(game):
    """run a game with two computers"""
    game.two_ai = True
    game.player1_type = AI
    game.player2_type = AI
    game.ai_is_first = True
    game.enable_button = False
    game.player_vs_computer = False

def two_players_game(game):
    """this function runs a game with two players."""
    game.two_ai = False
    game.player1_type = PLAYER
    game.player2_type = PLAYER
    game.ai_is_first = False
    game.enable_button = True
    game.player_vs_computer = False

def main():
    """main function of the game"""
    # calling constructor
    game = Game()

    # activate the first menu
    my_gui = Opening_menu()
    user_select = my_gui.user_select
    if user_select == NO_CHOICE:
        raise Exception("No game type selected!")
    else:
        if user_select == ONE_PLYER_FIRST:
            game_one_player_first(game)

        elif user_select == ONE_PLYER_SECOND:
            game_one_player_second(game)

        elif user_select == TWO_PLAYERS:
            two_players_game(game)

        elif user_select ==TWO_COMPUTRES:
            two_computers(game)

    my_gui = Game_menu(game)
    my_gui.run_game()






if __name__ == '__main__':
    main()