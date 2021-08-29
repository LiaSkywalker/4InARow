PLAYER_A = "1"
PLAYER_B = "2"
EMPTY_COL = "_"
PLAYER_A_INT = 1
PLAYER_B_INT = 2
REMAINING_PART = 3
WIN_LENGTH = 4
STANDOFF = 0
GAME_NOT_END = None
BOARD_ROW_SIZE = 6
BOARD_COLUMN_SIZE = 7
AI = "ai"
PLAYER = "player"

class Game:

    def __init__(self):
        """initialize the game class"""

        #const and variables
        self.board_row_size = BOARD_ROW_SIZE
        self.board_column_size = BOARD_COLUMN_SIZE
        self.bord = []
        self.win_discs =[]
        self.reset_bord()
        self.player_1_discs = []
        self.player_2_discs = []
        self.current_player = PLAYER_A_INT

        #variables of game properties:
        self.two_ai = False
        self.player_vs_computer = False
        self.player1_type = AI
        self.player2_type = AI
        self.ai_is_first = False
        self.enable_button = True

    #####board managing####

    def reset_bord(self):
        """reset board"""
        for i in range(self.board_row_size):
            self.bord.append([EMPTY_COL, EMPTY_COL, EMPTY_COL, EMPTY_COL,
                              EMPTY_COL, EMPTY_COL, EMPTY_COL])

    def update_board(self):
        """this function update the board. used while printing the board"""
        for disc_loc in self.player_1_discs:
            self.bord[disc_loc[0]][disc_loc[1]] = PLAYER_A

        for disc_loc in self.player_2_discs:
            self.bord[disc_loc[0]][disc_loc[1]] = PLAYER_B

    def print_board(self):
        """function to print the board in the terminal"""
        self.update_board()
        # transform the bord to string
        str_for_printing = ""
        for i in range(self.board_row_size):
            str_for_printing += " ".join(self.bord[i]) + "\n"
        return(str_for_printing)

    def add_disc_to_board(self,player,coordinate):
        """add disc to board due to the given params."""
        players = {PLAYER_A_INT: PLAYER_A,PLAYER_B_INT:PLAYER_B}
        if player == PLAYER_A_INT:
            self.player_1_discs.append(coordinate)
        elif player == PLAYER_B_INT:
            self.player_2_discs.append(coordinate)
        self.update_board()

    def find_cell_to_place(self,column):
        """get the column choice and return the cell to place in it."""
        for row in range(self.board_row_size -1,-1,-1):
            if self.is_cell_empty((row,column)):
                # the cell is empty!
                return(row,column)
        return(None)

    def is_cell_empty(self,coordinate):
        """check if cell is empty return false if not empty, and true else"""
        if coordinate in self.player_1_discs:
            return(False)
        if coordinate in self.player_2_discs:
            return (False)
        return(True)

    ######game managing####

    def change_player(self):
        """change the current player"""
        if self.current_player == PLAYER_A_INT:
            self.current_player = PLAYER_B_INT
        elif self.current_player == PLAYER_B_INT:
            self.current_player = PLAYER_A_INT

    def is_board_full(self):
        """check if the board is full and return true if so.
        if the board in not full- returns false"""
        for row in range(self.board_row_size):
            for col in range(self.board_column_size):
                if self.bord[row][col] == EMPTY_COL:
                    return False
        return True

    def is_winner(self,player):
        """check if sequence of disc are exist in the game"""
        if self.horizon(player) or self.vertical(player) or \
                self.diagonal_down(player) or self.diagnoal_up(player):
            return True
        return False


    #####check winner####
    def horizon(self,player):
        """check winner horizontally"""
        for row in range(self.board_row_size):
            for col in range(self.board_column_size - 3):
                if (self.bord[row][col] == player) and (self.bord[row][col + 1] == player) and \
                        (self.bord[row][col+2] ==player) and (self.bord[row][col+3] == player):
                    #winner found!
                    self.win_discs =[(row,col),(row,col+1),(row,col+2),(row,col+3)]
                    return True
        return False

    def vertical(self,player):
        """check winner vertically"""
        for col in range(self.board_column_size):
            for row in range(self.board_row_size - 3):
                if (self.bord[row][col] == player) and (self.bord[row + 1][col] == player) and \
                    (self.bord[row + 2][col] == player) and (self.bord[row + 3][col] == player):
                    #winner found!
                    self.win_discs =[(row,col),(row +1,col),(row+2,col),(row+3,col)]
                    return True
        return False

    def diagonal_down(self,player):
        """check winner diagonal down"""
        for row in range(self.board_row_size - 3):
            for col in range(self.board_column_size - 3):
                if (self.bord[row][col] == player) and (self.bord[row+1][col+1] ==player) and \
                        (self.bord[row + 2][col + 2] == player) and \
                        (self.bord[row + 3][col + 3] == player):
                    #winner found!
                    self.win_discs =[(row,col),(row+1,col+1),(row+2,col+2),(row+3,col+3)]
                    return True
        return False

    def diagnoal_up(self,player):
        """check winner diagonal up"""
        for row in range(self.board_row_size - 1, 2, -1):
            for col in range(self.board_column_size - 3):
                # print(row,col)
                if (self.bord[row][col]==player) and (self.bord[row -1][col +1] == player) and \
                    (self.bord[row - 2][col + 2] == player) and \
                        (self.bord[row - 3][col + 3] == player):
                    #winner found!
                    self.win_discs = [(row,col),(row -1,col+1),(row-2,col+2),(row-3,col+3)]
                    return True
        return False

    ########API function########

    def make_move(self, column):
        """get a column and add the bottom line that empty"""
        add_to_cell = self.find_cell_to_place(column)

        # check if the move is legal
        if (column >= BOARD_COLUMN_SIZE) or (column < 0):
            raise Exception("illegal move")
        if add_to_cell == None:
            #it is not legal to place disc in the given column
            raise Exception("illegal move")

        self.add_disc_to_board(self.current_player,add_to_cell)
        self.change_player()

    def get_winner(self):
        """this function check if the game ends- full board, or four in a row.
        returns 1 if player_a won, 2 if player_b won, 0 if standoff,
         and None if the game did not over yet. """

        if self.is_board_full():
            return STANDOFF
        if self.is_winner(PLAYER_A):
            return PLAYER_A_INT
        if self.is_winner(PLAYER_B):
            return PLAYER_B_INT
        return None

    def get_player_at(self, row, col):
        """returns the player which the disc in the given location belongs to him"""
        #check if the locatoin is legal
        if (row > self.board_row_size) or (col > self.board_column_size):
            raise Exception("illegal location.")
        #check the player
        if self.bord[row][col] == PLAYER_A:
            return 1
        if self.bord[row][col] == PLAYER_B:
            return 2
        return None

    def get_current_player(self):
        return self.current_player
