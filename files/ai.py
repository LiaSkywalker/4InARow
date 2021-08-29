import random
BOARD_ROW_SIZE = 6
BOARD_COLUMN_SIZE = 7
class AI:

    def __init__(self, game, player):
        """inputs: game- object from Game class
                   player- in type of int. 1-player 1 or 2-player 2"""
        self.game = game
        self.player = player
        pass

    def find_legal_move(self):
        """search for legal column to insert discs into it,
        and returns it"""
        possible_col=list(range(BOARD_ROW_SIZE ,-1,-1))

        if self.game.get_winner() is not None:
            raise Exception("No possible AI moves")
        while possible_col:
            col = random.choice(possible_col)
            if self.game.get_player_at(0,col) is None:
                return col
            else:
                possible_col.remove(col)
        raise Exception("No possible AI moves")