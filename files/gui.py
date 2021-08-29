import tkinter
from PIL import Image, ImageTk
from functools import partial
from .game import *
from .ai import *
import os

NO_CHOICE = 0
ONE_PLYER_FIRST = 1
ONE_PLYER_SECOND =2
TWO_PLAYERS = 3
TWO_COMPUTRES = 4
ROW = 6
COL = 7
PLAYER1 = 1
PLAYER2 = 2
WINNING = 3

#Game_menu images
EMPTY_IMAGE ="/icecube.png"
ARROW = "/arrow.png"
PLAYER1_IMAGE = "/penguin2.png"
PLAYER2_IMAGE = "/bear1.png"
PLAYER1_WIN = "/plyer1win.png"
PLAYER2_WIN= "/player2win.png"
GAME_OVER= "/gameover.png"
WINNER_IMAGE ="/winner1.png"

#Opening_menu images
COMP_VS_COMP_PIC = "/compvscomp.png"
COMP_VS_PLAYER_PIC = "/compvsplayer.png"
PLAYER_VS_COMP_PIC = "/playervscomp.png"
TWO_PLAYERS_PIC = "/2players.png"
GAME_TITLE ="/gametitle.png"



class Opening_menu:
    """this class run the opening menu for game"""

    def __init__(self):
        """initialize the gui"""
        root = tkinter.Tk()
        self.master = root
        self.user_select = NO_CHOICE
        self.master.geometry('330x420')
        frame_up = tkinter.Frame(self.master)
        frame_up.pack(side="top")
        frame_down = tkinter.Frame(self.master)
        frame_down.pack(side="bottom")

        self.dir_path = os.path.dirname(os.path.realpath(__file__))

        self.pic0 = ImageTk.PhotoImage(Image.open(self.dir_path + GAME_TITLE))
        self.pic1 = ImageTk.PhotoImage(Image.open(self.dir_path + COMP_VS_COMP_PIC))
        self.pic2 = ImageTk.PhotoImage(Image.open(self.dir_path + COMP_VS_PLAYER_PIC))
        self.pic3 = ImageTk.PhotoImage(Image.open(self.dir_path + PLAYER_VS_COMP_PIC))
        self.pic4 = ImageTk.PhotoImage(Image.open(self.dir_path + TWO_PLAYERS_PIC))

        self.master.configure(background='#8080FF')
        lable = tkinter.Label(frame_up, image = self.pic0)
        lable1 = tkinter.Label(frame_up, text = "welcome to four in a row game!" + "\n" +
                                                  " please choose game configuration")
        lable.pack()
        lable1.pack()
        #lable.grid(row=0, column=1)

        button1 = tkinter.Button(self.master,image=self.pic4,command =self.two_players_click)
        button1.pack(side = "top")
        #button1.grid(row=2, column = 0)

        button2 = tkinter.Button(self.master, image=self.pic2,
                                 command=self.one_player_second_click)
        button2.pack(side = "top")
        #button2.grid(row=2,column = 1)

        button3 = tkinter.Button(self.master, image=self.pic3,
                                 command=self.one_player_first_click)
        button3.pack(side = "top")
        #button3.grid(row=2, column=2)

        button4 = tkinter.Button(self.master, image=self.pic1,
                                 command=self.two_computers_click)
        button4.pack(side = "top")
        #button4.grid(row=2, column=3)

        self.master.mainloop()

    def two_players_click(self):
        """run the game with two players"""
        self.user_select = TWO_PLAYERS
        self.master.destroy()

    def one_player_second_click(self):
        """run the game with two players"""
        self.user_select = ONE_PLYER_SECOND
        self.master.destroy()

    def one_player_first_click(self):
        """run the game with one player only"""
        self.user_select = ONE_PLYER_FIRST
        self.master.destroy()

    def two_computers_click(self):
        """run the game with two computers"""
        self.user_select = TWO_COMPUTRES
        self.master.destroy()

class Game_menu:
    """this class run the game gui"""

    def __init__(self,game):
        """init the game window"""
        self.game= game
        self.master = tkinter.Tk()
        self.master.configure(background='#66B3FF')
        self.cell_list = []
        self.button_list =[None] * COL
        self.master.geometry('400x530')

        self.frame0 = tkinter.Frame(self.master)
        self.frame0.pack(side="top")

        self.frame1 = tkinter.Frame(self.master)
        self.frame1.pack(side ="top")

        self.frame2 = tkinter.Frame(self.master)
        self.frame2.pack(side="top")
        self.frame2.configure(background='#66B3FF')

        self.dir_path = os.path.dirname(os.path.realpath(__file__))

        self.photo1 = ImageTk.PhotoImage(Image.open(self.dir_path + ARROW))
        self.photo = ImageTk.PhotoImage(Image.open(self.dir_path + EMPTY_IMAGE))
        self.photo2 = ImageTk.PhotoImage(Image.open(self.dir_path + PLAYER1_IMAGE))
        self.photo3 = ImageTk.PhotoImage(Image.open(self.dir_path + PLAYER2_IMAGE))
        self.photo4 = ImageTk.PhotoImage(Image.open(self.dir_path + PLAYER1_WIN))
        self.photo5 = ImageTk.PhotoImage(Image.open(self.dir_path + PLAYER2_WIN))
        self.photo6 = ImageTk.PhotoImage(Image.open(self.dir_path + GAME_OVER))
        self.photo7 = ImageTk.PhotoImage(Image.open(self.dir_path + WINNER_IMAGE))
        self.photo8 = ImageTk.PhotoImage(Image.open(self.dir_path + GAME_TITLE))

        self.title = tkinter.Label(self.frame0,image = self.photo8)
        self.title.photo = self.photo8
        self.title.pack()

        self.create_first_row()
        self.create_board()


    def create_board(self):
        """create the game table"""
        for i in range(ROW):
            temporary_list = []
            for j in range(COL):
                lable = tkinter.Label(self.frame2, image=self.photo,
                                      width="50", height="50", bg='#66B3FF')
                lable.photo = self.photo
                lable.grid(row=i, column =j)

                temporary_list.append(lable)
            self.cell_list.append(temporary_list)

    def create_first_row(self):
        """create arrows in the first line"""
        for num in range(COL):

            btn = tkinter.Button(self.frame1)
            btn.config(image=self.photo1, width="50", height="50", bg='#3B55FF',
                       command=partial(self.btn_clicked, num))
            btn.grid(row=0,column=num)

    def btn_clicked(self,num):
        if self.game.enable_button: #check if pressing is allowed now
            cur_player = self.game.get_current_player()
            if (cur_player == PLAYER_A_INT and self.game.player1_type == PLAYER) or \
                    (cur_player == PLAYER_B_INT and self.game.player2_type == PLAYER):

                coor = self.game.find_cell_to_place(num)

                self.game.make_move(num)
                self.game.update_board()

                self.place_in_col(coor,cur_player)
                self.check_winner()
                #self.game.change_player()

                if self.game.player_vs_computer == True:
                    cur_player = self.game.get_current_player()
                    self.game.enable_button = False
                    self.master.after(1000, self.run_ai)

    def check_winner(self):
        """check if the game was ended"""
        win = self.game.get_winner()
        if win == STANDOFF:
            #"stand off"
            self.update_after_win()
            self.game.enable_button = False
            self.title.config(image=self.photo6)
            return True

        elif win == PLAYER_A_INT:
            #"player 1 win"
            self.update_after_win()
            self.title.config(image=self.photo4)
            self.game.enable_button = False
            return True

        elif win == PLAYER_B_INT:
            #"player 2 win"
            self.update_after_win()
            self.title.config(image = self.photo5)
            self.game.enable_button = False
            return True
        else:
            return False

    def update_after_win(self):
        """update the picture of the winning discs"""
        for disc_tup in self.game.win_discs:
            self.update_photo(disc_tup[0],disc_tup[1],WINNING)

    def place_in_col(self,coor,player):
        """get leagal col to place disc in it, and returns the leagal row)"""
        self.update_photo(coor[0],coor[1],player)
        return

    def run_ai(self):
        """runs ai """

        cur_player = self.game.get_current_player()
        if (cur_player == PLAYER_A_INT and self.game.player1_type == AI) or \
                (cur_player == PLAYER_B_INT and self.game.player2_type == AI):
            ai = AI(self.game, cur_player)
            move = ai.find_legal_move()
            coor = self.game.find_cell_to_place(move)

            self.game.make_move(move)
            self.game.update_board()

            self.place_in_col(coor, cur_player)

            win_status = self.check_winner()

            if win_status == True:
                return

            if self.game.player_vs_computer == True:
                self.game.enable_button = True

            if self.game.two_ai == True:
                self.master.after(1000, self.run_ai)

    def run_game(self):
        """run game"""
        if self.game.ai_is_first == True:
            self.master.after(10, self.run_ai)
        self.master.mainloop()

    def update_photo(self,row,col,player):
        """update the grid column, in the given coordinates"""
        if player== PLAYER1:
            self.cell_list[row][col].config(image=self.photo2,width="50", height="50")
        if player == PLAYER2:
            self.cell_list[row][col].config(image=self.photo3,width="50", height="50")
        if player == WINNING:
            self.cell_list[row][col].config(image=self.photo7, width="50", height="50")
