# sorry_controller
# This is the controller for a multi-player game of SORRY!

import random
import time
from sorry_cards import *
from sorry_model import *
from sorry_view import *

PAUSE = 2
SHORT_PAUSE = 0.5
LONG_PAUSE = 3

class player():
    """
    Class player represents a player with a color name in a game of SORRY!
    """
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

class sorryController():
    def __init__(self, model, view, num_players):
        self.model = model
        self.view = view
        self.num_players = 4
        if num_players == 2 or num_players == 3 or num_players == 4:
            self.num_players = num_players
        else:
            #print('Invalid number of players. Players = 4.')
            self.num_players = 4
        self.player1_turn = False
        self.player2_turn = False
        self.player3_turn = False
        self.player4_turn = False
        self.player1 = None
        self.player2 = None
        self.player3 = None
        self.player4 = None
        self.game_over = False
        self.set_up_players()
        self.view.display_yellow_start(len(self.model.yellow_start))
        self.view.display_green_start(len(self.model.green_start))
        self.view.display_red_start(len(self.model.red_start))
        self.view.display_blue_start(len(self.model.blue_start))

    def set_up_players(self):
        if self.num_players == 2:
            goes_first = random.randint(1, 2)
            player1_color = random.randint(1, 2)
            if player1_color == 1:
                self.player1 = player('yellow')
                self.player2 = player('red')
            elif player1_color == 2:
                self.player1 = player('red')
                self.player2 = player('yellow')
            # set player to go first
            if goes_first == 1:
                self.player1_turn = True
            elif goes_first == 2:
                self.player2_turn = True
        elif self.num_players == 3:
            goes_first = random.randint(1, 3)
            player1_color = random.randint(1, 3)
            if player1_color == 1:
                self.player1 = player('yellow')
                self.player2 = player('green')
                self.player3 = player('blue')
            elif player1_color == 2:
                self.player1 = player('green')
                self.player2 = player('blue')
                self.player3 = player('yellow')
            elif player1_color == 3:
                self.player1 = player('blue')
                self.player2 = player('yellow')
                self.player3 = player('green')
            # set player to go first
            if goes_first == 1:
                self.player1_turn = True
            elif goes_first == 2:
                self.player2_turn = True
            elif goes_first == 3:
                self.player3_turn = True
        elif self.num_players == 4:
            goes_first = random.randint(1, 4)
            player1_color = random.randint(1, 4)
            if player1_color == 1:
                self.player1 = player('yellow')
                self.player2 = player('green')
                self.player3 = player('red')
                self.player4 = player('blue')
            elif player1_color == 2:
                self.player1 = player('green')
                self.player2 = player('red')
                self.player3 = player('blue')
                self.player4 = player('yellow')
            elif player1_color == 3:
                self.player1 = player('red')
                self.player2 = player('blue')
                self.player3 = player('yellow')
                self.player4 = player('green')
            elif player1_color == 4:
                self.player1 = player('blue')
                self.player2 = player('yellow')
                self.player3 = player('green')
                self.player4 = player('red')
            # set player to go first
            if goes_first == 1:
                self.player1_turn = True
            elif goes_first == 2:
                self.player2_turn = True
            elif goes_first == 3:
                self.player3_turn = True
            elif goes_first == 4:
                self.player4_turn = True

    def change_player(self):
        """
        Does: changes player to next player according to self.num_players
        """
        if self.num_players == 2:
            if self.player1_turn == True:
                self.player1_turn = False
                self.player2_turn = True
            elif self.player2_turn == True:
                self.player2_turn = False
                self.player1_turn = True
        elif self.num_players == 3:
            if self.player1_turn == True:
                self.player1_turn = False
                self.player2_turn = True
            elif self.player2_turn == True:
                self.player2_turn = False
                self.player3_turn = True
            elif self.player3_turn == True:
                self.player3_turn = False
                self.player1_turn = True
        elif self.num_players == 4:
            if self.player1_turn == True:
                self.player1_turn = False
                self.player2_turn = True
            elif self.player2_turn == True:
                self.player2_turn = False
                self.player3_turn = True
            elif self.player3_turn == True:
                self.player3_turn = False
                self.player4_turn = True
            elif self.player4_turn == True:
                self.player4_turn = False
                self.player1_turn = True

    def play_player1_turn(self):
        """
        Does: runs player1 (user) turn, calls appropriate helper functions
        according to what card has been drawn
        """
        if self.model.deck.is_empty():
            self.model.deck = deck()
            self.view.undraw_discard_pile()
            self.view.display_text("Shuffling....")
            time.sleep(PAUSE)
            self.view.display_draw_pile()
        self.view.display_text('Click to draw a \n card.')
        block = 1000
        while block != 500:
            click_point = self.view.win.getMouse()
            x = click_point.getX()
            y = click_point.getY()
            block = self.view.get_block(x, y)
        self.draw_card()
        if isinstance(self.model.discard[-1], oneCard):
            self.one_card_player1()
        elif isinstance(self.model.discard[-1], twoCard):
            self.two_card_player1()
        elif isinstance(self.model.discard[-1], threeCard):
            self.three_card_player1()
        elif isinstance(self.model.discard[-1], fourCard):
            self.four_card_player1()
        elif isinstance(self.model.discard[-1], fiveCard):
            self.five_card_player1()
        elif isinstance(self.model.discard[-1], sevenCard):
            self.seven_card_player1()
        elif isinstance(self.model.discard[-1], eightCard):
            self.eight_card_player1()
        elif isinstance(self.model.discard[-1], tenCard):
            self.ten_card_player1()
        elif isinstance(self.model.discard[-1], elevenCard):
            self.eleven_card_player1()
        elif isinstance(self.model.discard[-1], twelveCard):
            self.twelve_card_player1()
        elif isinstance(self.model.discard[-1], sorryCard):
            self.sorry_card_player1()

    def get_list_and_square_from_model(self, block):
        """
        Does: translates block number to list and square
        Returns: model list and square
        """
        if 0 <= block <= 59:
            return self.model.main_board, block
        elif 100 <= block <= 105:
            return self.model.yellow_safety, block - 100
        elif 200 <= block <= 205:
            return self.model.green_safety, block - 200
        elif 300 <= block <= 305:
            return self.model.red_safety, block - 300
        elif 400 <= block <= 405:
            return self.model.blue_safety, block - 400
        elif block == 106:
            return self.model.yellow_start, 0
        elif block == 206:
            return self.model.green_start, 0
        elif block == 306:
            return self.model.red_start, 0
        elif block == 406:
            return self.model.blue_start, 0

    def get_list_and_square_from_view(self, block):
        """
        Does: translates block number to list and square
        Returns: view list and square
        """
        if 0 <= block <= 59:
            return self.view.main_board, block
        elif 100 <= block <= 105:
            return self.view.yellow_safety, block - 100
        elif 200 <= block <= 205:
            return self.view.green_safety, block - 200
        elif 300 <= block <= 305:
            return self.view.red_safety, block - 300
        elif 400 <= block <= 405:
            return self.view.blue_safety, block - 400
        elif block == 106:
            return self.view.yellow_start, 0
        elif block == 206:
            return self.view.green_start, 0
        elif block == 306:
            return self.view.red_start, 0
        elif block == 406:
            return self.view.blue_start, 0

    def one_card_move_exists(self, color):
        """
        Does: checks if one_card move is possible
        Returns: True if move is possible, False if not
        """
        # one_card move is always possible as long as game is not over
        if self.game_over:
            return False
        return True

    def two_card_move_exists(self, color):
        """
        Does: checks if any piece can move 2 or move out from start
        Returns: True if move is possible, False if not
        """
        if color == 'yellow':
            if self.model.yellow_start:
                # if a single piece is in start then move 2 is possible
                return True
            # check safety_zone
            if self.model.yellow_safety[3].is_occupied():
                return True
            for i in range(3):
                if self.model.yellow_safety[i].is_occupied():
                    if not self.model.yellow_safety[i + 2].is_occupied():
                        # from square + 2 is unoccupied
                        return True
            # check main_board
            for i in range(60):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        if self.model.main_board[(i + 2) % 60].is_occupied():
                            if self.model.main_board[(i + 2) % 60].get_color() != color:
                                return True
                        else:
                            # from square + 2 is unoccupied
                            return True
            return False
        elif color == 'green':
            if self.model.green_start:
                # if a single piece is in start then move 2 is possible
                return True
            # check safety_zone
            if self.model.green_safety[3].is_occupied():
                return True
            for i in range(3):
                if self.model.green_safety[i].is_occupied():
                    if not self.model.green_safety[i + 2].is_occupied():
                        # from square + 2 is unoccupied
                        return True
            # check main_board
            for i in range(60):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        if self.model.main_board[(i + 2) % 60].is_occupied():
                            if self.model.main_board[(i + 2) % 60].get_color() != color:
                                return True
                        else:
                            # from square + 2 is unoccupied
                            return True
            return False
        elif color == 'red':
            if self.model.red_start:
                # if a single piece is in start then move 2 is possible
                return True
            # check safety_zone
            if self.model.red_safety[3].is_occupied():
                return True
            for i in range(3):
                if self.model.red_safety[i].is_occupied():
                    if not self.model.red_safety[i + 2].is_occupied():
                        # from square + 2 is unoccupied
                        return True
            # check main_board
            for i in range(60):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        if self.model.main_board[(i + 2) % 60].is_occupied():
                            if self.model.main_board[(i + 2) % 60].get_color() != color:
                                return True
                        else:
                            # from square + 2 is unoccupied
                            return True
            return False
        elif color == 'blue':
            if self.model.blue_start:
                # if a single piece is in start then move 2 is possible
                return True
            # check safety_zone
            if self.model.blue_safety[3].is_occupied():
                return True
            for i in range(3):
                if self.model.blue_safety[i].is_occupied():
                    if not self.model.blue_safety[i + 2].is_occupied():
                        # from square + 2 is unoccupied
                        return True
            # check main_board
            for i in range(60):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        if self.model.main_board[(i + 2) % 60].is_occupied():
                            if self.model.main_board[(i + 2) % 60].get_color() != color:
                                return True
                        else:
                            # from square + 2 is unoccupied
                            return True
            return False
        

    def three_card_move_exists(self, color):
        """
        Does: checks if any piece can move 3
        Returns: True if move is possible, False if not
        """
        if color == 'yellow':
            # check safety_zone
            if self.model.yellow_safety[2].is_occupied():
                return True
            for i in range(2):
                if self.model.yellow_safety[i].is_occupied():
                    if not self.model.yellow_safety[i + 3].is_occupied():
                        return True
            # check main_board
            for i in range(60):
                if 56 <= i <= 58:
                    if self.model.main_board[i].is_occupied():
                        if self.model.main_board[i].get_color() == color:
                            if not self.model.yellow_safety[(i + 3) % 59].is_occupied():
                                return True
                else:
                    if self.model.main_board[i].is_occupied():
                        if self.model.main_board[i].get_color() == color:
                            if self.model.main_board[(i + 3) % 60].is_occupied():
                                if self.model.main_board[(i + 3) % 60].get_color() != color:
                                    return True
                            else:
                                # from square + 3 is unoccupied
                                return True
            return False
        elif color == 'green':
            # check safety_zone
            if self.model.green_safety[2].is_occupied():
                return True
            for i in range(2):
                if self.model.green_safety[i].is_occupied():
                    if not self.model.green_safety[i + 3].is_occupied():
                        return True
            # check main_board
            for i in range(60):
                if 11 <= i <= 13:
                    if self.model.main_board[i].is_occupied():
                        if self.model.main_board[i].get_color() == color:
                            if not self.model.green_safety[(i + 3) % 14].is_occupied():
                                return True
                else:
                    if self.model.main_board[i].is_occupied():
                        if self.model.main_board[i].get_color() == color:
                            if self.model.main_board[(i + 3) % 60].is_occupied():
                                if self.model.main_board[(i + 3) % 60].get_color() != color:
                                    return True
                            else:
                                # from square + 3 is unoccupied
                                return True
            return False
        elif color == 'red':
            # check safety_zone
            if self.model.red_safety[2].is_occupied():
                return True
            for i in range(2):
                if self.model.red_safety[i].is_occupied():
                    if not self.model.red_safety[i + 3].is_occupied():
                        return True
            # check main_board
            for i in range(60):
                if 26 <= i <= 28:
                    if self.model.main_board[i].is_occupied():
                        if self.model.main_board[i].get_color() == color:
                            if not self.model.red_safety[(i + 3) % 29].is_occupied():
                                return True
                else:
                    if self.model.main_board[i].is_occupied():
                        if self.model.main_board[i].get_color() == color:
                            if self.model.main_board[(i + 3) % 60].is_occupied():
                                if self.model.main_board[(i + 3) % 60].get_color() != color:
                                    return True
                            else:
                                # from square + 3 is unoccupied
                                return True
            return False
        elif color == 'blue':
            # check safety_zone
            if self.model.blue_safety[2].is_occupied():
                return True
            for i in range(2):
                if self.model.blue_safety[i].is_occupied():
                    if not self.model.blue_safety[i + 3].is_occupied():
                        return True
            # check main_board
            for i in range(60):
                if 41 <= i <= 43:
                    if self.model.main_board[i].is_occupied():
                        if self.model.main_board[i].get_color() == color:
                            if not self.model.blue_safety[(i + 3) % 44].is_occupied():
                                return True
                else:
                    if self.model.main_board[i].is_occupied():
                        if self.model.main_board[i].get_color() == color:
                            if self.model.main_board[(i + 3) % 60].is_occupied():
                                if self.model.main_board[(i + 3) % 60].get_color() != color:
                                    return True
                            else:
                                # from square + 3 is unoccupied
                                return True
            return False

    def four_card_move_exists(self, color):
        """
        Does: checks if four backward move exists
        Return: True if move is possible, False if not
        """
        if color == 'yellow':
            for i in range(5):
                if self.model.yellow_safety[i].is_occupied():
                    return True
            for i in range(60):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        return True
            return False
        elif color == 'green':
            for i in range(5):
                if self.model.green_safety[i].is_occupied():
                    return True
            for i in range(60):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        return True
            return False
        elif color == 'red':
            for i in range(5):
                if self.model.red_safety[i].is_occupied():
                    return True
            for i in range(60):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        return True
            return False
        elif color == 'blue':
            for i in range(5):
                if self.model.blue_safety[i].is_occupied():
                    return True
            for i in range(60):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        return True
            return False

    def five_card_move_exists(self, color):
        """
        Does: checks if any piece can move 5 spaces forward
        Returns: True if move is possible, False if not
        """
        if color == 'yellow':
            # check safety_zone
            if self.model.yellow_safety[0].is_occupied():
                return True
            # check main_board
            for i in range(60):
                if 54 <= i <= 58:
                    if self.model.main_board[i].is_occupied():
                        if self.model.main_board[i].get_color() == color:
                            if not self.model.yellow_safety[(i + 5) % 59].is_occupied():
                                return True
                else:
                    if self.model.main_board[i].is_occupied():
                        if self.model.main_board[i].get_color() == color:
                            if self.model.main_board[(i + 5) % 60].is_occupied():
                                if self.model.main_board[(i + 5) % 60].get_color() != color:
                                    return True
                            else:
                                # from square + 5 is unoccupied
                                return True
            return False
        elif color == 'green':
            # check safety_zone
            if self.model.green_safety[0].is_occupied():
                return True
            # check main_board
            for i in range(60):
                if 9 <= i <= 13:
                    if self.model.main_board[i].is_occupied():
                        if self.model.main_board[i].get_color() == color:
                            if not self.model.green_safety[(i + 5) % 14].is_occupied():
                                return True
                else:
                    if self.model.main_board[i].is_occupied():
                        if self.model.main_board[i].get_color() == color:
                            if self.model.main_board[(i + 5) % 60].is_occupied():
                                if self.model.main_board[(i + 5) % 60].get_color() != color:
                                    return True
                            else:
                                # from square + 5 is unoccupied
                                return True
            return False
        elif color == 'red':
            # check safety_zone
            if self.model.red_safety[0].is_occupied():
                return True
            # check main_board
            for i in range(60):
                if 24 <= i <= 28:
                    if self.model.main_board[i].is_occupied():
                        if self.model.main_board[i].get_color() == color:
                            if not self.model.red_safety[(i + 5) % 29].is_occupied():
                                return True
                else:
                    if self.model.main_board[i].is_occupied():
                        if self.model.main_board[i].get_color() == color:
                            if self.model.main_board[(i + 5) % 60].is_occupied():
                                if self.model.main_board[(i + 5) % 60].get_color() != color:
                                    return True
                            else:
                                # from square + 5 is unoccupied
                                return True
            return False
        elif color == 'blue':
            # check safety_zone
            if self.model.blue_safety[0].is_occupied():
                return True
            # check main_board
            for i in range(60):
                if 39 <= i <= 43:
                    if self.model.main_board[i].is_occupied():
                        if self.model.main_board[i].get_color() == color:
                            if not self.model.blue_safety[(i + 5) % 44].is_occupied():
                                return True
                else:
                    if self.model.main_board[i].is_occupied():
                        if self.model.main_board[i].get_color() == color:
                            if self.model.main_board[(i + 5) % 60].is_occupied():
                                if self.model.main_board[(i + 5) % 60].get_color() != color:
                                    return True
                            else:
                                # from square + 5 is unoccupied
                                return True
            return False

    def seven_card_move_exists(self, color):
        """
        Does: checks if any possible 7 card moves exist
        Returns: True if move is possible, False if not
        """
        if color == 'yellow':
            # check if all pieces are home first
            if self.model.yellow_start:
                if len(self.model.yellow_start) == 4:
                    return False
            # check the whole board for all possible split moves
            for i in range(65):
                for j in range(65):
                    if i == j:
                        nothing = True
                    else:
                        for k in range(1, 8):
                            l = 7 - k
                            piece1_move = False
                            piece2_move = False
                            if i >= 60:
                                # check safety_zone
                                if self.model.yellow_safety[i - 60].is_occupied():
                                    if self.model.yellow_safety[i - 60 + k].is_valid():
                                        if self.model.yellow_safety[i - 60 + k].is_home():
                                            piece1_move = True
                                        else:
                                            # not home
                                            if not self.model.yellow_safety[i - 60 + k].is_occupied():
                                                piece1_move = True
                            else:
                                # check main_board
                                if i <= 58 and i + k > 58:
                                    # must check for occupied in safety_zone
                                    if self.model.main_board[i].is_occupied():
                                        if self.model.main_board[i].get_color() == color:
                                            if self.model.yellow_safety[(i + k) % 59].is_valid():
                                                if self.model.yellow_safety[(i + k) % 59].is_home():
                                                    piece1_move = True
                                                else:
                                                    if not self.model.yellow_safety[(i + k) % 59].is_occupied():
                                                        piece1_move = True
                                else:
                                    # check main_board only
                                    if self.model.main_board[i].is_occupied():
                                        if self.model.main_board[i].get_color() == color:
                                            if self.model.main_board[(i + k) % 60].is_occupied():
                                                if self.model.main_board[(i + k) % 60].get_color() != color:
                                                    piece1_move = True
                                            else:
                                                # from square + k is unoccupied
                                                piece1_move = True
                            if l == 0:
                                piece2_move = True
                            else:
                                if j >= 60:
                                    # check safety_zone
                                    if self.model.yellow_safety[j - 60].is_occupied():
                                        if self.model.yellow_safety[j - 60 + l].is_valid():
                                            if self.model.yellow_safety[j - 60 + l].is_home():
                                                piece2_move = True
                                            else:
                                                # not home
                                                if not self.model.yellow_safety[j - 60 + l].is_occupied():
                                                    piece2_move = True
                                else:
                                    # check main_board
                                    if j <= 58 and j + l > 58:
                                        # must check for occupied in safety_zone
                                        if self.model.main_board[j].is_occupied():
                                            if self.model.main_board[j].get_color() == color:
                                                if self.model.yellow_safety[(j + l) % 59].is_valid():
                                                    if self.model.yellow_safety[(j + l) % 59].is_home():
                                                        piece2_move = True
                                                    else:
                                                        if not self.model.yellow_safety[(j + l) % 59].is_occupied():
                                                            piece2_move = True
                                    else:
                                        # check main_board only
                                        if self.model.main_board[j].is_occupied():
                                            if self.model.main_board[j].get_color() == color:
                                                if self.model.main_board[(j + l) % 60].is_occupied():
                                                    if self.model.main_board[(j + l) % 60].get_color() != color:
                                                        piece2_move = True
                                                else:
                                                    # from square + l is unoccupied
                                                    piece2_move = True
                            # check if both pieces' moves are good
                            if piece1_move and piece2_move:
                                return True
            return False
        elif color == 'green':
            # check if all pieces are home first
            if self.model.green_start:
                if len(self.model.green_start) == 4:
                    return False
            # check the whole board for all possible split moves
            for i in range(65):
                for j in range(65):
                    if i == j:
                        nothing = True
                    else:
                        for k in range(1, 8):
                            l = 7 - k
                            piece1_move = False
                            piece2_move = False
                            if i >= 60:
                                # check safety_zone
                                if self.model.green_safety[i - 60].is_occupied():
                                    if self.model.green_safety[i - 60 + k].is_valid():
                                        if self.model.green_safety[i - 60 + k].is_home():
                                            piece1_move = True
                                        else:
                                            # not home
                                            if not self.model.green_safety[i - 60 + k].is_occupied():
                                                piece1_move = True
                            else:
                                # check main_board
                                if i <= 13 and i + k > 13:
                                    # must check for occupied in safety_zone
                                    if self.model.main_board[i].is_occupied():
                                        if self.model.main_board[i].get_color() == color:
                                            if self.model.green_safety[(i + k) % 14].is_valid():
                                                if self.model.green_safety[(i + k) % 14].is_home():
                                                    piece1_move = True
                                                else:
                                                    if not self.model.green_safety[(i + k) % 14].is_occupied():
                                                        piece1_move = True
                                else:
                                    # check main_board only
                                    if self.model.main_board[i].is_occupied():
                                        if self.model.main_board[i].get_color() == color:
                                            if self.model.main_board[(i + k) % 60].is_occupied():
                                                if self.model.main_board[(i + k) % 60].get_color() != color:
                                                    piece1_move = True
                                            else:
                                                # from square + k is unoccupied
                                                piece1_move = True
                            if l == 0:
                                piece2_move = True
                            else:
                                if j >= 60:
                                    # check safety_zone
                                    if self.model.green_safety[j - 60].is_occupied():
                                        if self.model.green_safety[j - 60 + l].is_valid():
                                            if self.model.green_safety[j - 60 + l].is_home():
                                                piece2_move = True
                                            else:
                                                # not home
                                                if not self.model.green_safety[j - 60 + l].is_occupied():
                                                    piece2_move = True
                                else:
                                    # check main_board
                                    if j <= 13 and j + l > 13:
                                        # must check for occupied in safety_zone
                                        if self.model.main_board[j].is_occupied():
                                            if self.model.main_board[j].get_color() == color:
                                                if self.model.green_safety[(j + l) % 14].is_valid():
                                                    if self.model.green_safety[(j + l) % 14].is_home():
                                                        piece2_move = True
                                                    else:
                                                        if not self.model.green_safety[(j + l) % 14].is_occupied():
                                                            piece2_move = True
                                    else:
                                        # check main_board only
                                        if self.model.main_board[j].is_occupied():
                                            if self.model.main_board[j].get_color() == color:
                                                if self.model.main_board[(j + l) % 60].is_occupied():
                                                    if self.model.main_board[(j + l) % 60].get_color() != color:
                                                        piece2_move = True
                                                else:
                                                    # from square + l is unoccupied
                                                    piece2_move = True
                            # check if both pieces' moves are good
                            if piece1_move and piece2_move:
                                return True
            return False
        elif color == 'red':
            # check if all pieces are home first
            if self.model.red_start:
                if len(self.model.red_start) == 4:
                    return False
            # check the whole board for all possible split moves
            for i in range(65):
                for j in range(65):
                    if i == j:
                        nothing = True
                    else:
                        for k in range(1, 8):
                            l = 7 - k
                            piece1_move = False
                            piece2_move = False
                            if i >= 60:
                                # check safety_zone
                                if self.model.red_safety[i - 60].is_occupied():
                                    if self.model.red_safety[i - 60 + k].is_valid():
                                        if self.model.red_safety[i - 60 + k].is_home():
                                            piece1_move = True
                                        else:
                                            # not home
                                            if not self.model.red_safety[i - 60 + k].is_occupied():
                                                piece1_move = True
                            else:
                                # check main_board
                                if i <= 28 and i + k > 28:
                                    # must check for occupied in safety_zone
                                    if self.model.main_board[i].is_occupied():
                                        if self.model.main_board[i].get_color() == color:
                                            if self.model.red_safety[(i + k) % 29].is_valid():
                                                if self.model.red_safety[(i + k) % 29].is_home():
                                                    piece1_move = True
                                                else:
                                                    if not self.model.red_safety[(i + k) % 29].is_occupied():
                                                        piece1_move = True
                                else:
                                    # check main_board only
                                    if self.model.main_board[i].is_occupied():
                                        if self.model.main_board[i].get_color() == color:
                                            if self.model.main_board[(i + k) % 60].is_occupied():
                                                if self.model.main_board[(i + k) % 60].get_color() != color:
                                                    piece1_move = True
                                            else:
                                                # from square + k is unoccupied
                                                piece1_move = True
                            if l == 0:
                                piece2_move = True
                            else:
                                if j >= 60:
                                    # check safety_zone
                                    if self.model.red_safety[j - 60].is_occupied():
                                        if self.model.red_safety[j - 60 + l].is_valid():
                                            if self.model.red_safety[j - 60 + l].is_home():
                                                piece2_move = True
                                            else:
                                                # not home
                                                if not self.model.red_safety[j - 60 + l].is_occupied():
                                                    piece2_move = True
                                else:
                                    # check main_board
                                    if j <= 28 and j + l > 28:
                                        # must check for occupied in safety_zone
                                        if self.model.main_board[j].is_occupied():
                                            if self.model.main_board[j].get_color() == color:
                                                if self.model.red_safety[(j + l) % 29].is_valid():
                                                    if self.model.red_safety[(j + l) % 29].is_home():
                                                        piece2_move = True
                                                    else:
                                                        if not self.model.red_safety[(j + l) % 29].is_occupied():
                                                            piece2_move = True
                                    else:
                                        # check main_board only
                                        if self.model.main_board[j].is_occupied():
                                            if self.model.main_board[j].get_color() == color:
                                                if self.model.main_board[(j + l) % 60].is_occupied():
                                                    if self.model.main_board[(j + l) % 60].get_color() != color:
                                                        piece2_move = True
                                                else:
                                                    # from square + l is unoccupied
                                                    piece2_move = True
                            # check if both pieces' moves are good
                            if piece1_move and piece2_move:
                                return True
            return False
        elif color == 'blue':
            # check if all pieces are home first
            if self.model.blue_start:
                if len(self.model.blue_start) == 4:
                    return False
            # check the whole board for all possible split moves
            for i in range(65):
                for j in range(65):
                    if i == j:
                        nothing = True
                    else:
                        for k in range(1, 8):
                            l = 7 - k
                            piece1_move = False
                            piece2_move = False
                            if i >= 60:
                                # check safety_zone
                                if self.model.blue_safety[i - 60].is_occupied():
                                    if self.model.blue_safety[i - 60 + k].is_valid():
                                        if self.model.blue_safety[i - 60 + k].is_home():
                                            piece1_move = True
                                        else:
                                            # not home
                                            if not self.model.blue_safety[i - 60 + k].is_occupied():
                                                piece1_move = True
                            else:
                                # check main_board
                                if i <= 43 and i + k > 43:
                                    # must check for occupied in safety_zone
                                    if self.model.main_board[i].is_occupied():
                                        if self.model.main_board[i].get_color() == color:
                                            if self.model.blue_safety[(i + k) % 44].is_valid():
                                                if self.model.blue_safety[(i + k) % 44].is_home():
                                                    piece1_move = True
                                                else:
                                                    if not self.model.blue_safety[(i + k) % 44].is_occupied():
                                                        piece1_move = True
                                else:
                                    # check main_board only
                                    if self.model.main_board[i].is_occupied():
                                        if self.model.main_board[i].get_color() == color:
                                            if self.model.main_board[(i + k) % 60].is_occupied():
                                                if self.model.main_board[(i + k) % 60].get_color() != color:
                                                    piece1_move = True
                                            else:
                                                # from square + k is unoccupied
                                                piece1_move = True
                            if l == 0:
                                piece2_move = True
                            else:
                                if j >= 60:
                                    # check safety_zone
                                    if self.model.blue_safety[j - 60].is_occupied():
                                        if self.model.blue_safety[j - 60 + l].is_valid():
                                            if self.model.blue_safety[j - 60 + l].is_home():
                                                piece2_move = True
                                            else:
                                                # not home
                                                if not self.model.blue_safety[j - 60 + l].is_occupied():
                                                    piece2_move = True
                                else:
                                    # check main_board
                                    if j <= 43 and j + l > 43:
                                        # must check for occupied in safety_zone
                                        if self.model.main_board[j].is_occupied():
                                            if self.model.main_board[j].get_color() == color:
                                                if self.model.blue_safety[(j + l) % 44].is_valid():
                                                    if self.model.blue_safety[(j + l) % 44].is_home():
                                                        piece2_move = True
                                                    else:
                                                        if not self.model.blue_safety[(j + l) % 44].is_occupied():
                                                            piece2_move = True
                                    else:
                                        # check main_board only
                                        if self.model.main_board[j].is_occupied():
                                            if self.model.main_board[j].get_color() == color:
                                                if self.model.main_board[(j + l) % 60].is_occupied():
                                                    if self.model.main_board[(j + l) % 60].get_color() != color:
                                                        piece2_move = True
                                                else:
                                                    # from square + l is unoccupied
                                                    piece2_move = True
                            # check if both pieces' moves are good
                            if piece1_move and piece2_move:
                                return True
            return False

    def eight_card_move_exists(self, color):
        """
        Does: checks if 8 space move is possible
        Returns: True if move is possible, False if not
        """
        if color == 'yellow':
            # check if all pieces are home first
            if self.model.yellow_start:
                if len(self.model.yellow_start) == 4:
                    return False
            # check main_board
            for i in range(60):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        if i <= 58 and i + 8 > 58:
                            # check safety zone
                            if self.model.yellow_safety[(i + 8) % 59].is_valid():
                                if self.model.yellow_safety[(i + 8) % 59].is_home():
                                    return True
                                else:
                                    if not self.model.yellow_safety[(i + 8) % 59].is_occupied():
                                        return True
                        else:
                            # continue checking main_board
                            if self.model.main_board[(i + 8) % 60].is_occupied():
                                if self.model.main_board[(i + 8) % 60].get_color() != color:
                                    return True
                            else:
                                # from square + 8 is unoccupied
                                return True
            return False
        elif color == 'green':
            # check if all pieces are home first
            if self.model.green_start:
                if len(self.model.green_start) == 4:
                    return False
            # check main_board
            for i in range(60):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        if i <= 13 and i + 8 > 13:
                            # check safety zone
                            if self.model.green_safety[(i + 8) % 14].is_valid():
                                if self.model.green_safety[(i + 8) % 14].is_home():
                                    return True
                                else:
                                    if not self.model.green_safety[(i + 8) % 14].is_occupied():
                                        return True
                        else:
                            # continue checking main_board
                            if self.model.main_board[(i + 8) % 60].is_occupied():
                                if self.model.main_board[(i + 8) % 60].get_color() != color:
                                    return True
                            else:
                                # from square + 8 is unoccupied
                                return True
            return False
        elif color == 'red':
            # check if all pieces are home first
            if self.model.red_start:
                if len(self.model.red_start) == 4:
                    return False
            # check main_board
            for i in range(60):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        if i <= 28 and i + 8 > 28:
                            # check safety zone
                            if self.model.red_safety[(i + 8) % 29].is_valid():
                                if self.model.red_safety[(i + 8) % 29].is_home():
                                    return True
                                else:
                                    if not self.model.red_safety[(i + 8) % 29].is_occupied():
                                        return True
                        else:
                            # continue checking main_board
                            if self.model.main_board[(i + 8) % 60].is_occupied():
                                if self.model.main_board[(i + 8) % 60].get_color() != color:
                                    return True
                            else:
                                # from square + 8 is unoccupied
                                return True
            return False
        elif color == 'blue':
            # check if all pieces are home first
            if self.model.blue_start:
                if len(self.model.blue_start) == 4:
                    return False
            # check main_board
            for i in range(60):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        if i <= 43 and i + 8 > 43:
                            # check safety zone
                            if self.model.blue_safety[(i + 8) % 44].is_valid():
                                if self.model.blue_safety[(i + 8) % 44].is_home():
                                    return True
                                else:
                                    if not self.model.blue_safety[(i + 8) % 44].is_occupied():
                                        return True
                        else:
                            # continue checking main_board
                            if self.model.main_board[(i + 8) % 60].is_occupied():
                                if self.model.main_board[(i + 8) % 60].get_color() != color:
                                    return True
                            else:
                                # from square + 8 is unoccupied
                                return True
            return False

    def ten_card_move_exists(self, color):
        """
        Does: checks if 10 forward or 1 backward is possible for some piece
        Returns: True if move is possible, False if not
        """
        if color == 'yellow':
            # check if all pieces are in start
            if self.model.yellow_start:
                if len(self.model.yellow_start) == 4:
                    return False
            # check safety zone
            for i in range(5):
                if self.model.yellow_safety[i].is_occupied():
                    return True
            # check main_board
            for i in range(60):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        return True
            return False
        elif color == 'green':
            # check if all pieces are in start
            if self.model.green_start:
                if len(self.model.green_start) == 4:
                    return False
            # check safety zone
            for i in range(5):
                if self.model.green_safety[i].is_occupied():
                    return True
            # check main_board
            for i in range(60):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        return True
            return False
        elif color == 'red':
            # check if all pieces are in start
            if self.model.red_start:
                if len(self.model.red_start) == 4:
                    return False
            # check safety zone
            for i in range(5):
                if self.model.red_safety[i].is_occupied():
                    return True
            # check main_board
            for i in range(60):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        return True
            return False
        elif color == 'blue':
            # check if all pieces are in start
            if self.model.blue_start:
                if len(self.model.blue_start) == 4:
                    return False
            # check safety zone
            for i in range(5):
                if self.model.blue_safety[i].is_occupied():
                    return True
            # check main_board
            for i in range(60):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        return True
            return False

    def eleven_card_move_exists(self, color):
        """
        Does: checks if trading places is possible, and checks for moving forward 11 is possible
        Returns: True if move is possible, False if not
        """
        if color == 'yellow':
            # check if all pieces are in start
            if self.model.yellow_start:
                if len(self.model.yellow_start) == 4:
                    return False
            # check for switching pieces on main_board
            piece1 = False
            piece2 = False
            for i in range(60):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        piece1 = True
            for i in range(60):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() != color:
                        piece2 = True
            if piece1 and piece2:
                return True
            # check for forward move of 11
            for i in range(60):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        if i <= 58 and i + 11 > 58:
                            # check safety zone
                            if self.model.yellow_safety[(i + 11) % 59].is_valid():
                                if self.model.yellow_safety[(i + 11) % 59].is_home():
                                    return True
                                else:
                                    # regular space
                                    if not self.model.yellow_safety[(i + 11) % 59].is_occupied():
                                        return True
                        else:
                            # check main_board
                            if self.model.main_board[(i + 11) % 60].is_occupied():
                                if self.model.main_board[(i + 11) % 60].get_color() != color:
                                    return True
                            else:
                                # from square + 11 is unoccupied
                                return True
            return False
        elif color == 'green':
            # check if all pieces are in start
            if self.model.green_start:
                if len(self.model.green_start) == 4:
                    return False
            # check for switching pieces on main_board
            piece1 = False
            piece2 = False
            for i in range(60):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        piece1 = True
            for i in range(60):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() != color:
                        piece2 = True
            if piece1 and piece2:
                return True
            # check for forward move of 11
            for i in range(60):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        if i <= 13 and i + 11 > 13:
                            # check safety zone
                            if self.model.green_safety[(i + 11) % 14].is_valid():
                                if self.model.green_safety[(i + 11) % 14].is_home():
                                    return True
                                else:
                                    # regular space
                                    if not self.model.green_safety[(i + 11) % 14].is_occupied():
                                        return True
                        else:
                            # check main_board
                            if self.model.main_board[(i + 11) % 60].is_occupied():
                                if self.model.main_board[(i + 11) % 60].get_color() != color:
                                    return True
                            else:
                                # from square + 11 is unoccupied
                                return True
            return False
        elif color == 'red':
            # check if all pieces are in start
            if self.model.red_start:
                if len(self.model.red_start) == 4:
                    return False
            # check for switching pieces on main_board
            piece1 = False
            piece2 = False
            for i in range(60):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        piece1 = True
            for i in range(60):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() != color:
                        piece2 = True
            if piece1 and piece2:
                return True
            # check for forward move of 11
            for i in range(60):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        if i <= 28 and i + 11 > 28:
                            # check safety zone
                            if self.model.red_safety[(i + 11) % 29].is_valid():
                                if self.model.red_safety[(i + 11) % 29].is_home():
                                    return True
                                else:
                                    # regular space
                                    if not self.model.red_safety[(i + 11) % 29].is_occupied():
                                        return True
                        else:
                            # check main_board
                            if self.model.main_board[(i + 11) % 60].is_occupied():
                                if self.model.main_board[(i + 11) % 60].get_color() != color:
                                    return True
                            else:
                                # from square + 11 is unoccupied
                                return True
            return False
        elif color == 'blue':
            # check if all pieces are in start
            if self.model.blue_start:
                if len(self.model.blue_start) == 4:
                    return False
            # check for switching pieces on main_board
            piece1 = False
            piece2 = False
            for i in range(60):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        piece1 = True
            for i in range(60):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() != color:
                        piece2 = True
            if piece1 and piece2:
                return True
            # check for forward move of 11
            for i in range(60):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        if i <= 43 and i + 11 > 43:
                            # check safety zone
                            if self.model.blue_safety[(i + 11) % 44].is_valid():
                                if self.model.blue_safety[(i + 11) % 44].is_home():
                                    return True
                                else:
                                    # regular space
                                    if not self.model.blue_safety[(i + 11) % 44].is_occupied():
                                        return True
                        else:
                            # check main_board
                            if self.model.main_board[(i + 11) % 60].is_occupied():
                                if self.model.main_board[(i + 11) % 60].get_color() != color:
                                    return True
                            else:
                                # from square + 11 is unoccupied
                                return True
            return False

    def twelve_card_move_exists(self, color):
        """
        Does: checks main_board for possible move of 12 spaces
        Returns: True if move exists, False if not
        """
        if color == 'yellow':
            # first checks if start is full
            if self.model.yellow_start:
                if len(self.model.yellow_start) == 4:
                    return False
            # check main board for move of 12
            for i in range(60):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        if i <= 58 and i + 12 > 58:
                            # check safety zone
                            if self.model.yellow_safety[(i + 12) % 59].is_valid():
                                if self.model.yellow_safety[(i + 12) % 59].is_home():
                                    return True
                                else:
                                    # regular space
                                    if not self.model.yellow_safety[(i + 12) % 59].is_occupied():
                                        return True
                        else:
                            # check main_board
                            if self.model.main_board[(i + 12) % 60].is_occupied():
                                if self.model.main_board[(i + 12) % 60].get_color() != color:
                                    return True
                            else:
                                # from square + 12 is unoccupied
                                return True
            return False
        elif color == 'green':
            # first checks if start is full
            if self.model.green_start:
                if len(self.model.green_start) == 4:
                    return False
            # check main board for move of 12
            for i in range(60):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        if i <= 13 and i + 12 > 13:
                            # check safety zone
                            if self.model.green_safety[(i + 12) % 14].is_valid():
                                if self.model.green_safety[(i + 12) % 14].is_home():
                                    return True
                                else:
                                    # regular space
                                    if not self.model.green_safety[(i + 12) % 14].is_occupied():
                                        return True
                        else:
                            # check main_board
                            if self.model.main_board[(i + 12) % 60].is_occupied():
                                if self.model.main_board[(i + 12) % 60].get_color() != color:
                                    return True
                            else:
                                # from square + 12 is unoccupied
                                return True
            return False
        elif color == 'red':
            # first checks if start is full
            if self.model.red_start:
                if len(self.model.red_start) == 4:
                    return False
            # check main board for move of 12
            for i in range(60):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        if i <= 28 and i + 12 > 28:
                            # check safety zone
                            if self.model.red_safety[(i + 12) % 29].is_valid():
                                if self.model.red_safety[(i + 12) % 29].is_home():
                                    return True
                                else:
                                    # regular space
                                    if not self.model.red_safety[(i + 12) % 29].is_occupied():
                                        return True
                        else:
                            # check main_board
                            if self.model.main_board[(i + 12) % 60].is_occupied():
                                if self.model.main_board[(i + 12) % 60].get_color() != color:
                                    return True
                            else:
                                # from square + 12 is unoccupied
                                return True
            return False
        elif color == 'blue':
            # first checks if start is full
            if self.model.blue_start:
                if len(self.model.blue_start) == 4:
                    return False
            # check main board for move of 12
            for i in range(60):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        if i <= 43 and i + 12 > 43:
                            # check safety zone
                            if self.model.blue_safety[(i + 12) % 44].is_valid():
                                if self.model.blue_safety[(i + 12) % 44].is_home():
                                    return True
                                else:
                                    # regular space
                                    if not self.model.blue_safety[(i + 12) % 44].is_occupied():
                                        return True
                        else:
                            # check main_board
                            if self.model.main_board[(i + 12) % 60].is_occupied():
                                if self.model.main_board[(i + 12) % 60].get_color() != color:
                                    return True
                            else:
                                # from square + 12 is unoccupied
                                return True
            return False

    def sorry_card_move_exists(self, color):
        """
        Does: checks if sorry move exists
        Returns: True if move is possible, False if not
        """
        if color == 'yellow':
            # check if start is empty
            if not self.model.yellow_start:
                return False
            # check main board for any opposing piece
            for i in range(60):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() != color:
                        return True
            return False
        elif color == 'green':
            # check if start is empty
            if not self.model.green_start:
                return False
            # check main board for any opposing piece
            for i in range(60):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() != color:
                        return True
            return False
        elif color == 'red':
            # check if start is empty
            if not self.model.red_start:
                return False
            # check main board for any opposing piece
            for i in range(60):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() != color:
                        return True
            return False
        elif color == 'blue':
            # check if start is empty
            if not self.model.blue_start:
                return False
            # check main board for any opposing piece
            for i in range(60):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() != color:
                        return True
            return False
        
    def check_legal_move(self, from_list, from_sq, to_list, to_sq, color):
        """
        Does: checks if move is legal according to model
        Returns: True if move is legal, False if not
        """
        if from_list is self.model.yellow_start:
            if color != 'yellow':
                return False
            if not self.model.yellow_start:
                return False
        elif from_list is self.model.green_start:
            if color != 'green':
                return False
            if not self.model.green_start:
                return False
        elif from_list is self.model.red_start:
            if color != 'red':
                return False
            if not self.model.red_start:
                return False
        elif from_list is self.model.blue_start:
            if color != 'blue':
                return False
            if not self.model.blue_start:
                return False
        else:
            if from_list[from_sq].is_occupied():
                if from_list[from_sq].get_color() != color:
                    return False
            else:
                return False
        # check if to_sq is invalid
        if not to_list[to_sq].is_valid():
            return False
        # check if to_sq is home
        if to_list[to_sq].is_home():
            return True
        # check that to_sq is empty or has different color
        if to_list[to_sq].is_occupied():
            if to_list[to_sq].get_color() == color:
                return False
        return True
        

    def display_all_starts(self):
        """
        Does: displays all start fields
        """
        self.view.display_yellow_start(len(self.model.yellow_start))
        self.view.display_green_start(len(self.model.green_start))
        self.view.display_red_start(len(self.model.red_start))
        self.view.display_blue_start(len(self.model.blue_start))

    def check_win(self, color):
        """
        Does: checks if color has just won and ends game
        """
        if color == 'yellow':
            if self.model.yellow_safety[5].is_occupied():
                if len(self.model.yellow_safety[5].space) == 4:
                    self.game_over = True
                    self.player1_turn = False
                    self.player2_turn = False
                    self.player3_turn = False
                    self.player4_turn = False
                    self.view.display_text('GAME OVER. YELLOW WINS!')
        elif color == 'green':
            if self.model.green_safety[5].is_occupied():
                if len(self.model.green_safety[5].space) == 4:
                    self.game_over = True
                    self.player1_turn = False
                    self.player2_turn = False
                    self.player3_turn = False
                    self.player4_turn = False
                    self.view.display_text('GAME OVER. GREEN WINS!')
        elif color == 'red':
            if self.model.red_safety[5].is_occupied():
                if len(self.model.red_safety[5].space) == 4:
                    self.game_over = True
                    self.player1_turn = False
                    self.player2_turn = False
                    self.player3_turn = False
                    self.player4_turn = False
                    self.view.display_text('GAME OVER. RED WINS!')
        elif color == 'blue':
            if self.model.blue_safety[5].is_occupied():
                if len(self.model.blue_safety[5].space) == 4:
                    self.game_over = True
                    self.player1_turn = False
                    self.player2_turn = False
                    self.player3_turn = False
                    self.player4_turn = False
                    self.view.display_text('GAME OVER. BLUE WINS!')

    def one_card_player1(self):
        """
        Does: plays out 'one card' scenario for player1
        """
        self.view.display_text('Click on start to move man out, or click \n on piece ' +
                               'to move one square.')
        if self.player1.get_color() == 'yellow':
            if self.one_card_move_exists('yellow'):
                # get click
                legal_move = False
                while legal_move == False:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    from_block = self.view.get_block(x, y)
                    # check if start
                    if from_block == 106:
                        to_block = 0
                        legal_move = self.check_legal_move(self.model.yellow_start, 0,
                                        self.model.main_board, 0, 'yellow')
                    # check if block 58
                    elif from_block == 58:
                        to_block = 100
                        legal_move = self.check_legal_move(self.model.main_board, 58,
                                            self.model.yellow_safety, 0, 'yellow')
                    # check if on main_board
                    elif 0 <= from_block <= 59:
                        to_block = (from_block + 1) % 60
                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                            self.model.main_board, to_block, 'yellow')
                    # check if in safety_zone
                    elif 100 <= from_block <= 104:
                        to_block = from_block + 1
                        legal_move = self.check_legal_move(self.model.yellow_safety,
                                            from_block - 100, self.model.yellow_safety,
                                            to_block - 100, 'yellow')
                # carry out legal move
                from_list_model, from_sq_model = self.get_list_and_square_from_model(from_block)
                to_list_model, to_sq_model = self.get_list_and_square_from_model(to_block)
                from_list_view, from_sq_view = self.get_list_and_square_from_view(from_block)
                to_list_view, to_sq_view = self.get_list_and_square_from_view(to_block)
                if from_list_model is self.model.yellow_start:
                    self.model.move_piece_from_start(from_list_model, to_sq_model)
                    self.view.move_piece_from_start(from_list_view, to_sq_view)
                    self.check_slide(to_sq_view, "yellow")
                    self.display_all_starts()
                    self.change_player()
                else:
                    self.model.move_piece(from_list_model, from_sq_model, to_list_model,
                                          to_sq_model)
                    self.view.move_piece(from_list_view, from_sq_view, to_list_view,
                                         to_sq_view)
                    if to_list_view is self.view.main_board:
                        self.check_slide(to_sq_view, "yellow")
                    if to_list_model is self.model.yellow_safety and to_sq_model == 5:
                        self.check_win('yellow')
                    self.display_all_starts()
                    self.change_player()
            else:
                # move doesn't exist: forfeit turn
                self.view.display_text("No move possible. Click draw pile \n to forfeit turn.")
                block = 1000
                while block != 500:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    block = self.view.get_block(x, y)
                self.change_player()
        elif self.player1.get_color() == 'green':
            if self.one_card_move_exists('green'):
                # get click
                legal_move = False
                while legal_move == False:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    from_block = self.view.get_block(x, y)
                    # check if start
                    if from_block == 206:
                        to_block = 15
                        legal_move = self.check_legal_move(self.model.green_start, 0,
                                        self.model.main_board, 15, 'green')
                    # check if block 13
                    elif from_block == 13:
                        to_block = 200
                        legal_move = self.check_legal_move(self.model.main_board, 13,
                                            self.model.green_safety, 0, 'green')
                    # check if on main_board
                    elif 0 <= from_block <= 59:
                        to_block = (from_block + 1) % 60
                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                            self.model.main_board, to_block, 'green')
                    # check if in safety_zone
                    elif 200 <= from_block <= 204:
                        to_block = from_block + 1
                        legal_move = self.check_legal_move(self.model.green_safety,
                                            from_block - 200, self.model.green_safety,
                                            to_block - 200, 'green')
                # carry out legal move
                from_list_model, from_sq_model = self.get_list_and_square_from_model(from_block)
                to_list_model, to_sq_model = self.get_list_and_square_from_model(to_block)
                from_list_view, from_sq_view = self.get_list_and_square_from_view(from_block)
                to_list_view, to_sq_view = self.get_list_and_square_from_view(to_block)
                if from_list_model is self.model.green_start:
                    self.model.move_piece_from_start(from_list_model, to_sq_model)
                    self.view.move_piece_from_start(from_list_view, to_sq_view)
                    self.check_slide(to_sq_view, "green")
                    self.display_all_starts()
                    self.change_player()
                else:
                    self.model.move_piece(from_list_model, from_sq_model, to_list_model,
                                          to_sq_model)
                    self.view.move_piece(from_list_view, from_sq_view, to_list_view,
                                         to_sq_view)
                    if to_list_view is self.view.main_board:
                        self.check_slide(to_sq_view, "green")
                    if to_list_model is self.model.green_safety and to_sq_model == 5:
                        self.check_win('green')
                    self.display_all_starts()
                    self.change_player()
            else:
                # move doesn't exist: forfeit turn
                self.view.display_text("No move possible. Click draw pile \n to forfeit turn.")
                block = 1000
                while block != 500:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    block = self.view.get_block(x, y)
                self.change_player()
        elif self.player1.get_color() == 'red':
            if self.one_card_move_exists('red'):
                # get click
                legal_move = False
                while legal_move == False:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    from_block = self.view.get_block(x, y)
                    # check if start
                    if from_block == 306:
                        to_block = 30
                        legal_move = self.check_legal_move(self.model.red_start, 0,
                                        self.model.main_board, 30, 'red')
                    # check if block 28
                    elif from_block == 28:
                        to_block = 300
                        legal_move = self.check_legal_move(self.model.main_board, 28,
                                            self.model.green_safety, 0, 'red')
                    # check if on main_board
                    elif 0 <= from_block <= 59:
                        to_block = (from_block + 1) % 60
                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                            self.model.main_board, to_block, 'red')
                    # check if in safety_zone
                    elif 300 <= from_block <= 304:
                        to_block = from_block + 1
                        legal_move = self.check_legal_move(self.model.red_safety,
                                            from_block - 300, self.model.red_safety,
                                            to_block - 300, 'red')
                # carry out legal move
                from_list_model, from_sq_model = self.get_list_and_square_from_model(from_block)
                to_list_model, to_sq_model = self.get_list_and_square_from_model(to_block)
                from_list_view, from_sq_view = self.get_list_and_square_from_view(from_block)
                to_list_view, to_sq_view = self.get_list_and_square_from_view(to_block)
                if from_list_model is self.model.red_start:
                    self.model.move_piece_from_start(from_list_model, to_sq_model)
                    self.view.move_piece_from_start(from_list_view, to_sq_view)
                    self.check_slide(to_sq_view, "red")
                    self.display_all_starts()
                    self.change_player()
                else:
                    self.model.move_piece(from_list_model, from_sq_model, to_list_model,
                                          to_sq_model)
                    self.view.move_piece(from_list_view, from_sq_view, to_list_view,
                                         to_sq_view)
                    if to_list_view is self.view.main_board:
                        self.check_slide(to_sq_view, "red")
                    if to_list_model is self.model.red_safety and to_sq_model == 5:
                        self.check_win('red')
                    self.display_all_starts()
                    self.change_player()
            else:
                # move doesn't exist: forfeit turn
                self.view.display_text("No move possible. Click draw pile \n to forfeit turn.")
                block = 1000
                while block != 500:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    block = self.view.get_block(x, y)
                self.change_player()
        elif self.player1.get_color() == 'blue':
            if self.one_card_move_exists('blue'):
                # get click
                legal_move = False
                while legal_move == False:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    from_block = self.view.get_block(x, y)
                    # check if start
                    if from_block == 406:
                        to_block = 45
                        legal_move = self.check_legal_move(self.model.blue_start, 0,
                                        self.model.main_board, 45, 'blue')
                    # check if block 43
                    elif from_block == 43:
                        to_block = 400
                        legal_move = self.check_legal_move(self.model.main_board, 43,
                                            self.model.green_safety, 0, 'blue')
                    # check if on main_board
                    elif 0 <= from_block <= 59:
                        to_block = (from_block + 1) % 60
                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                            self.model.main_board, to_block, 'blue')
                    # check if in safety_zone
                    elif 400 <= from_block <= 404:
                        to_block = from_block + 1
                        legal_move = self.check_legal_move(self.model.blue_safety,
                                            from_block - 400, self.model.blue_safety,
                                            to_block - 400, 'blue')
                # carry out legal move
                from_list_model, from_sq_model = self.get_list_and_square_from_model(from_block)
                to_list_model, to_sq_model = self.get_list_and_square_from_model(to_block)
                from_list_view, from_sq_view = self.get_list_and_square_from_view(from_block)
                to_list_view, to_sq_view = self.get_list_and_square_from_view(to_block)
                if from_list_model is self.model.blue_start:
                    self.model.move_piece_from_start(from_list_model, to_sq_model)
                    self.view.move_piece_from_start(from_list_view, to_sq_view)
                    self.check_slide(to_sq_view, "blue")
                    self.display_all_starts()
                    self.change_player()
                else:
                    self.model.move_piece(from_list_model, from_sq_model, to_list_model,
                                          to_sq_model)
                    self.view.move_piece(from_list_view, from_sq_view, to_list_view,
                                         to_sq_view)
                    if to_list_view is self.view.main_board:
                        self.check_slide(to_sq_view, "blue")
                    if to_list_model is self.model.blue_safety and to_sq_model == 5:
                        self.check_win('blue')
                    self.display_all_starts()
                    self.change_player()
            else:
                # move doesn't exist: forfeit turn
                self.view.display_text("No move possible. Click draw pile \n to forfeit turn.")
                block = 1000
                while block != 500:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    block = self.view.get_block(x, y)
                self.change_player()
                               

    def two_card_player1(self):
        """
        Does: plays out 'two card' scenario for player1
        """
        self.view.display_text('Click on start to move man out, or click \n on piece ' +
                               'to move two squares.')
        if self.player1.get_color() == 'yellow':
            if self.two_card_move_exists('yellow'):
                # get click
                legal_move = False
                while legal_move == False:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    from_block = self.view.get_block(x, y)
                    # check if start
                    if from_block == 106:
                        to_block = 0
                        legal_move = self.check_legal_move(self.model.yellow_start, 0,
                                        self.model.main_board, 0, 'yellow')
                    # check if block 57
                    elif from_block == 57:
                        to_block = 100
                        legal_move = self.check_legal_move(self.model.main_board, 57,
                                            self.model.yellow_safety, 0, 'yellow')
                    # check if block 58
                    elif from_block == 58:
                        to_block = 101
                        legal_move = self.check_legal_move(self.model.main_board, 58,
                                            self.model.yellow_safety, 1, 'yellow')
                    # check if on main_board
                    elif 0 <= from_block <= 59:
                        to_block = (from_block + 2) % 60
                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                            self.model.main_board, to_block, 'yellow')
                    # check if in safety_zone
                    elif 100 <= from_block <= 103:
                        to_block = from_block + 2
                        legal_move = self.check_legal_move(self.model.yellow_safety,
                                            from_block - 100, self.model.yellow_safety,
                                            to_block - 100, 'yellow')
                # carry out legal move
                from_list_model, from_sq_model = self.get_list_and_square_from_model(from_block)
                to_list_model, to_sq_model = self.get_list_and_square_from_model(to_block)
                from_list_view, from_sq_view = self.get_list_and_square_from_view(from_block)
                to_list_view, to_sq_view = self.get_list_and_square_from_view(to_block)
                if from_list_model is self.model.yellow_start:
                    self.model.move_piece_from_start(from_list_model, to_sq_model)
                    self.view.move_piece_from_start(from_list_view, to_sq_view)
                    self.check_slide(to_sq_view, "yellow")
                    self.display_all_starts()
                    self.view.display_text('Draw again.')
                    time.sleep(SHORT_PAUSE)
                else:
                    self.model.move_piece(from_list_model, from_sq_model, to_list_model,
                                          to_sq_model)
                    self.view.move_piece(from_list_view, from_sq_view, to_list_view,
                                         to_sq_view)
                    if to_list_view is self.view.main_board:
                        self.check_slide(to_sq_view, "yellow")
                    if to_list_model is self.model.yellow_safety and to_sq_model == 5:
                        self.check_win('yellow')
                    self.display_all_starts()
                    if not self.game_over:
                        self.view.display_text('Draw again.')
                        time.sleep(SHORT_PAUSE)
                    
            else:
                # move doesn't exist: forfeit turn
                self.view.display_text("No move possible. Draw again.")
                time.sleep(PAUSE)
        elif self.player1.get_color() == 'green':
            if self.two_card_move_exists('green'):
                # get click
                legal_move = False
                while legal_move == False:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    from_block = self.view.get_block(x, y)
                    # check if start
                    if from_block == 206:
                        to_block = 15
                        legal_move = self.check_legal_move(self.model.green_start, 0,
                                        self.model.main_board, 15, 'green')
                    # check if block 12
                    elif from_block == 12:
                        to_block = 200
                        legal_move = self.check_legal_move(self.model.main_board, 12,
                                            self.model.green_safety, 0, 'green')
                    # check if block 13
                    elif from_block == 13:
                        to_block = 201
                        legal_move = self.check_legal_move(self.model.main_board, 13,
                                            self.model.green_safety, 1, 'green')
                    # check if on main_board
                    elif 0 <= from_block <= 59:
                        to_block = (from_block + 2) % 60
                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                            self.model.main_board, to_block, 'green')
                    # check if in safety_zone
                    elif 200 <= from_block <= 203:
                        to_block = from_block + 2
                        legal_move = self.check_legal_move(self.model.green_safety,
                                            from_block - 200, self.model.green_safety,
                                            to_block - 200, 'green')
                # carry out legal move
                from_list_model, from_sq_model = self.get_list_and_square_from_model(from_block)
                to_list_model, to_sq_model = self.get_list_and_square_from_model(to_block)
                from_list_view, from_sq_view = self.get_list_and_square_from_view(from_block)
                to_list_view, to_sq_view = self.get_list_and_square_from_view(to_block)
                if from_list_model is self.model.green_start:
                    self.model.move_piece_from_start(from_list_model, to_sq_model)
                    self.view.move_piece_from_start(from_list_view, to_sq_view)
                    self.check_slide(to_sq_view, "green")
                    self.display_all_starts()
                    self.view.display_text('Draw again.')
                    time.sleep(SHORT_PAUSE)
                else:
                    self.model.move_piece(from_list_model, from_sq_model, to_list_model,
                                          to_sq_model)
                    self.view.move_piece(from_list_view, from_sq_view, to_list_view,
                                         to_sq_view)
                    if to_list_view is self.view.main_board:
                        self.check_slide(to_sq_view, "green")
                    if to_list_model is self.model.green_safety and to_sq_model == 5:
                        self.check_win('green')
                    self.display_all_starts()
                    if not self.game_over:
                        self.view.display_text('Draw again.')
                        time.sleep(SHORT_PAUSE)
                    
            else:
                # move doesn't exist: forfeit turn
                self.view.display_text("No move possible. Draw again.")
                time.sleep(PAUSE)
        elif self.player1.get_color() == 'red':
            if self.two_card_move_exists('red'):
                # get click
                legal_move = False
                while legal_move == False:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    from_block = self.view.get_block(x, y)
                    # check if start
                    if from_block == 306:
                        to_block = 30
                        legal_move = self.check_legal_move(self.model.red_start, 0,
                                        self.model.main_board, 30, 'red')
                    # check if block 27
                    elif from_block == 27:
                        to_block = 300
                        legal_move = self.check_legal_move(self.model.main_board, 27,
                                            self.model.red_safety, 0, 'red')
                    # check if block 28
                    elif from_block == 28:
                        to_block = 301
                        legal_move = self.check_legal_move(self.model.main_board, 28,
                                            self.model.red_safety, 1, 'red')
                    # check if on main_board
                    elif 0 <= from_block <= 59:
                        to_block = (from_block + 2) % 60
                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                            self.model.main_board, to_block, 'red')
                    # check if in safety_zone
                    elif 300 <= from_block <= 303:
                        to_block = from_block + 2
                        legal_move = self.check_legal_move(self.model.red_safety,
                                            from_block - 300, self.model.red_safety,
                                            to_block - 300, 'red')
                # carry out legal move
                from_list_model, from_sq_model = self.get_list_and_square_from_model(from_block)
                to_list_model, to_sq_model = self.get_list_and_square_from_model(to_block)
                from_list_view, from_sq_view = self.get_list_and_square_from_view(from_block)
                to_list_view, to_sq_view = self.get_list_and_square_from_view(to_block)
                if from_list_model is self.model.red_start:
                    self.model.move_piece_from_start(from_list_model, to_sq_model)
                    self.view.move_piece_from_start(from_list_view, to_sq_view)
                    self.check_slide(to_sq_view, "red")
                    self.display_all_starts()
                    self.view.display_text('Draw again.')
                    time.sleep(SHORT_PAUSE)
                else:
                    self.model.move_piece(from_list_model, from_sq_model, to_list_model,
                                          to_sq_model)
                    self.view.move_piece(from_list_view, from_sq_view, to_list_view,
                                         to_sq_view)
                    if to_list_view is self.view.main_board:
                        self.check_slide(to_sq_view, "red")
                    if to_list_model is self.model.red_safety and to_sq_model == 5:
                        self.check_win('red')
                    self.display_all_starts()
                    if not self.game_over:
                        self.view.display_text('Draw again.')
                        time.sleep(SHORT_PAUSE)
                    
            else:
                # move doesn't exist: forfeit turn
                self.view.display_text("No move possible. Draw again.")
                time.sleep(PAUSE)
        elif self.player1.get_color() == 'blue':
            if self.two_card_move_exists('blue'):
                # get click
                legal_move = False
                while legal_move == False:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    from_block = self.view.get_block(x, y)
                    # check if start
                    if from_block == 406:
                        to_block = 45
                        legal_move = self.check_legal_move(self.model.blue_start, 0,
                                        self.model.main_board, 45, 'blue')
                    # check if block 42
                    elif from_block == 42:
                        to_block = 400
                        legal_move = self.check_legal_move(self.model.main_board, 42,
                                            self.model.blue_safety, 0, 'blue')
                    # check if block 43
                    elif from_block == 43:
                        to_block = 401
                        legal_move = self.check_legal_move(self.model.main_board, 43,
                                            self.model.blue_safety, 1, 'blue')
                    # check if on main_board
                    elif 0 <= from_block <= 59:
                        to_block = (from_block + 2) % 60
                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                            self.model.main_board, to_block, 'blue')
                    # check if in safety_zone
                    elif 400 <= from_block <= 403:
                        to_block = from_block + 2
                        legal_move = self.check_legal_move(self.model.blue_safety,
                                            from_block - 400, self.model.blue_safety,
                                            to_block - 400, 'blue')
                # carry out legal move
                from_list_model, from_sq_model = self.get_list_and_square_from_model(from_block)
                to_list_model, to_sq_model = self.get_list_and_square_from_model(to_block)
                from_list_view, from_sq_view = self.get_list_and_square_from_view(from_block)
                to_list_view, to_sq_view = self.get_list_and_square_from_view(to_block)
                if from_list_model is self.model.blue_start:
                    self.model.move_piece_from_start(from_list_model, to_sq_model)
                    self.view.move_piece_from_start(from_list_view, to_sq_view)
                    self.check_slide(to_sq_view, "blue")
                    self.display_all_starts()
                    self.view.display_text('Draw again.')
                    time.sleep(SHORT_PAUSE)
                else:
                    self.model.move_piece(from_list_model, from_sq_model, to_list_model,
                                          to_sq_model)
                    self.view.move_piece(from_list_view, from_sq_view, to_list_view,
                                         to_sq_view)
                    if to_list_view is self.view.main_board:
                        self.check_slide(to_sq_view, "blue")
                    if to_list_model is self.model.blue_safety and to_sq_model == 5:
                        self.check_win('blue')
                    self.display_all_starts()
                    if not self.game_over:
                        self.view.display_text('Draw again.')
                        time.sleep(SHORT_PAUSE)
                    
            else:
                # move doesn't exist: forfeit turn
                self.view.display_text("No move possible. Draw again.")
                time.sleep(PAUSE)

    def three_card_player1(self):
        """
        Does: plays out 'three card' scenario
        """
        self.view.display_text('Click on piece to move three squares.')
        if self.player1.get_color() == 'yellow':
            if self.three_card_move_exists('yellow'):
                # get click
                legal_move = False
                while legal_move == False:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    from_block = self.view.get_block(x, y)
                    # check if entering safety zone
                    if from_block <= 58 and from_block + 3 > 58:
                        to_block = (from_block + 3) % 59 + 100
                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                            self.model.yellow_safety, to_block - 100, 'yellow')
                    
                    # check if on main_board
                    elif 0 <= from_block <= 59:
                        to_block = (from_block + 3) % 60
                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                            self.model.main_board, to_block, 'yellow')
                    # check if in safety_zone
                    elif 100 <= from_block <= 102:
                        to_block = from_block + 3
                        legal_move = self.check_legal_move(self.model.yellow_safety,
                                            from_block - 100, self.model.yellow_safety,
                                            to_block - 100, 'yellow')
                # carry out legal move
                from_list_model, from_sq_model = self.get_list_and_square_from_model(from_block)
                to_list_model, to_sq_model = self.get_list_and_square_from_model(to_block)
                from_list_view, from_sq_view = self.get_list_and_square_from_view(from_block)
                to_list_view, to_sq_view = self.get_list_and_square_from_view(to_block)
                
                self.model.move_piece(from_list_model, from_sq_model, to_list_model,
                                          to_sq_model)
                self.view.move_piece(from_list_view, from_sq_view, to_list_view,
                                         to_sq_view)
                if to_list_view is self.view.main_board:
                    self.check_slide(to_sq_view, "yellow")
                if to_list_model is self.model.yellow_safety and to_sq_model == 5:
                    self.check_win('yellow')
                self.display_all_starts()
                self.change_player()
                    
            else:
                # move doesn't exist: forfeit turn
                self.view.display_text("No move possible. Click draw pile \n to forfeit turn.")
                block = 1000
                while block != 500:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    block = self.view.get_block(x, y)
                self.change_player()
        elif self.player1.get_color() == 'green':
            if self.three_card_move_exists('green'):
                # get click
                legal_move = False
                while legal_move == False:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    from_block = self.view.get_block(x, y)
                    # check if entering safety zone
                    if from_block <= 13 and from_block + 3 > 13:
                        to_block = (from_block + 3) % 14 + 200
                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                            self.model.green_safety, to_block - 200, 'green')
                    
                    # check if on main_board
                    elif 0 <= from_block <= 59:
                        to_block = (from_block + 3) % 60
                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                            self.model.main_board, to_block, 'green')
                    # check if in safety_zone
                    elif 200 <= from_block <= 202:
                        to_block = from_block + 3
                        legal_move = self.check_legal_move(self.model.green_safety,
                                            from_block - 200, self.model.green_safety,
                                            to_block - 200, 'green')
                # carry out legal move
                from_list_model, from_sq_model = self.get_list_and_square_from_model(from_block)
                to_list_model, to_sq_model = self.get_list_and_square_from_model(to_block)
                from_list_view, from_sq_view = self.get_list_and_square_from_view(from_block)
                to_list_view, to_sq_view = self.get_list_and_square_from_view(to_block)
                
                self.model.move_piece(from_list_model, from_sq_model, to_list_model,
                                          to_sq_model)
                self.view.move_piece(from_list_view, from_sq_view, to_list_view,
                                         to_sq_view)
                if to_list_view is self.view.main_board:
                    self.check_slide(to_sq_view, "green")
                if to_list_model is self.model.green_safety and to_sq_model == 5:
                    self.check_win('green')
                self.display_all_starts()
                self.change_player()
                    
            else:
                # move doesn't exist: forfeit turn
                self.view.display_text("No move possible. Click draw pile \n to forfeit turn.")
                block = 1000
                while block != 500:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    block = self.view.get_block(x, y)
                self.change_player()
        elif self.player1.get_color() == 'red':
            if self.three_card_move_exists('red'):
                # get click
                legal_move = False
                while legal_move == False:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    from_block = self.view.get_block(x, y)
                    # check if entering safety zone
                    if from_block <= 28 and from_block + 3 > 28:
                        to_block = (from_block + 3) % 29 + 300
                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                            self.model.red_safety, to_block - 300, 'red')
                    
                    # check if on main_board
                    elif 0 <= from_block <= 59:
                        to_block = (from_block + 3) % 60
                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                            self.model.main_board, to_block, 'red')
                    # check if in safety_zone
                    elif 300 <= from_block <= 302:
                        to_block = from_block + 3
                        legal_move = self.check_legal_move(self.model.red_safety,
                                            from_block - 300, self.model.red_safety,
                                            to_block - 300, 'red')
                # carry out legal move
                from_list_model, from_sq_model = self.get_list_and_square_from_model(from_block)
                to_list_model, to_sq_model = self.get_list_and_square_from_model(to_block)
                from_list_view, from_sq_view = self.get_list_and_square_from_view(from_block)
                to_list_view, to_sq_view = self.get_list_and_square_from_view(to_block)
                
                self.model.move_piece(from_list_model, from_sq_model, to_list_model,
                                          to_sq_model)
                self.view.move_piece(from_list_view, from_sq_view, to_list_view,
                                         to_sq_view)
                if to_list_view is self.view.main_board:
                    self.check_slide(to_sq_view, "red")
                if to_list_model is self.model.red_safety and to_sq_model == 5:
                    self.check_win('red')
                self.display_all_starts()
                self.change_player()
                    
            else:
                # move doesn't exist: forfeit turn
                self.view.display_text("No move possible. Click draw pile \n to forfeit turn.")
                block = 1000
                while block != 500:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    block = self.view.get_block(x, y)
                self.change_player()
        elif self.player1.get_color() == 'blue':
            if self.three_card_move_exists('blue'):
                # get click
                legal_move = False
                while legal_move == False:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    from_block = self.view.get_block(x, y)
                    # check if entering safety zone
                    if from_block <= 43 and from_block + 3 > 43:
                        to_block = (from_block + 3) % 44 + 400
                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                            self.model.blue_safety, to_block - 400, 'blue')
                    
                    # check if on main_board
                    elif 0 <= from_block <= 59:
                        to_block = (from_block + 3) % 60
                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                            self.model.main_board, to_block, 'blue')
                    # check if in safety_zone
                    elif 400 <= from_block <= 402:
                        to_block = from_block + 3
                        legal_move = self.check_legal_move(self.model.blue_safety,
                                            from_block - 400, self.model.blue_safety,
                                            to_block - 400, 'blue')
                # carry out legal move
                from_list_model, from_sq_model = self.get_list_and_square_from_model(from_block)
                to_list_model, to_sq_model = self.get_list_and_square_from_model(to_block)
                from_list_view, from_sq_view = self.get_list_and_square_from_view(from_block)
                to_list_view, to_sq_view = self.get_list_and_square_from_view(to_block)
                
                self.model.move_piece(from_list_model, from_sq_model, to_list_model,
                                          to_sq_model)
                self.view.move_piece(from_list_view, from_sq_view, to_list_view,
                                         to_sq_view)
                if to_list_view is self.view.main_board:
                    self.check_slide(to_sq_view, "blue")
                if to_list_model is self.model.blue_safety and to_sq_model == 5:
                    self.check_win('blue')
                self.display_all_starts()
                self.change_player()
                    
            else:
                # move doesn't exist: forfeit turn
                self.view.display_text("No move possible. Click draw pile \n to forfeit turn.")
                block = 1000
                while block != 500:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    block = self.view.get_block(x, y)
                self.change_player()

    def four_card_player1(self):
        """
        Does: plays out 'four card' scenario
        """
        self.view.display_text('Click on piece to move\n backward four squares.')
        if self.player1.get_color() == 'yellow':
            if self.four_card_move_exists('yellow'):
                # get click
                legal_move = False
                while legal_move == False:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    from_block = self.view.get_block(x, y)
                    # check if on main_board
                    if 0 <= from_block <= 59:
                        to_block = (from_block + 60 - 4) % 60
                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                                self.model.main_board, to_block, 'yellow')
                    # check if in safety_zone
                    elif from_block == 104:
                        to_block = from_block - 4
                        legal_move = self.check_legal_move(self.model.yellow_safety, 4,
                                                self.model.yellow_safety, 0, 'yellow')
                    elif 100 <= from_block <= 103:
                        to_block = from_block - 100 - 4 + 59
                        legal_move = self.check_legal_move(self.model.yellow_safety, from_block - 100,
                                                self.model.main_board, to_block, 'yellow')
                # carry out legal move
                from_list_model, from_sq_model = self.get_list_and_square_from_model(from_block)
                to_list_model, to_sq_model = self.get_list_and_square_from_model(to_block)
                from_list_view, from_sq_view = self.get_list_and_square_from_view(from_block)
                to_list_view, to_sq_view = self.get_list_and_square_from_view(to_block)
                
                self.model.move_piece(from_list_model, from_sq_model, to_list_model,
                                          to_sq_model)
                self.view.move_piece(from_list_view, from_sq_view, to_list_view,
                                         to_sq_view, False)
                if to_list_view is self.view.main_board:
                    self.check_slide(to_sq_view, "yellow")
                self.display_all_starts()
                self.change_player()
            else:
                # move doesn't exist, forfeit turn
                self.view.display_text("No move possible. Click draw pile \n to forfeit turn.")
                block = 1000
                while block != 500:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    block = self.view.get_block(x, y)
                self.change_player()
        elif self.player1.get_color() == 'green':
            if self.four_card_move_exists('green'):
                # get click
                legal_move = False
                while legal_move == False:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    from_block = self.view.get_block(x, y)
                    # check if on main_board
                    if 0 <= from_block <= 59:
                        to_block = (from_block + 60 - 4) % 60
                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                                self.model.main_board, to_block, 'green')
                    # check if in safety_zone
                    elif from_block == 204:
                        to_block = from_block - 4
                        legal_move = self.check_legal_move(self.model.green_safety, 4,
                                                self.model.green_safety, 0, 'green')
                    elif 200 <= from_block <= 203:
                        to_block = from_block - 200 - 4 + 14
                        legal_move = self.check_legal_move(self.model.green_safety, from_block - 200,
                                                self.model.main_board, to_block, 'green')
                # carry out legal move
                from_list_model, from_sq_model = self.get_list_and_square_from_model(from_block)
                to_list_model, to_sq_model = self.get_list_and_square_from_model(to_block)
                from_list_view, from_sq_view = self.get_list_and_square_from_view(from_block)
                to_list_view, to_sq_view = self.get_list_and_square_from_view(to_block)
                
                self.model.move_piece(from_list_model, from_sq_model, to_list_model,
                                          to_sq_model)
                self.view.move_piece(from_list_view, from_sq_view, to_list_view,
                                         to_sq_view, False)
                if to_list_view is self.view.main_board:
                    self.check_slide(to_sq_view, "green")
                self.display_all_starts()
                self.change_player()
            else:
                # move doesn't exist, forfeit turn
                self.view.display_text("No move possible. Click draw pile \n to forfeit turn.")
                block = 1000
                while block != 500:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    block = self.view.get_block(x, y)
                self.change_player()
        elif self.player1.get_color() == 'red':
            if self.four_card_move_exists('red'):
                # get click
                legal_move = False
                while legal_move == False:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    from_block = self.view.get_block(x, y)
                    # check if on main_board
                    if 0 <= from_block <= 59:
                        to_block = (from_block + 60 - 4) % 60
                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                                self.model.main_board, to_block, 'red')
                    # check if in safety_zone
                    elif from_block == 304:
                        to_block = from_block - 4
                        legal_move = self.check_legal_move(self.model.red_safety, 4,
                                                self.model.red_safety, 0, 'red')
                    elif 300 <= from_block <= 303:
                        to_block = from_block - 300 - 4 + 29
                        legal_move = self.check_legal_move(self.model.red_safety, from_block - 300,
                                                self.model.main_board, to_block, 'red')
                # carry out legal move
                from_list_model, from_sq_model = self.get_list_and_square_from_model(from_block)
                to_list_model, to_sq_model = self.get_list_and_square_from_model(to_block)
                from_list_view, from_sq_view = self.get_list_and_square_from_view(from_block)
                to_list_view, to_sq_view = self.get_list_and_square_from_view(to_block)
                
                self.model.move_piece(from_list_model, from_sq_model, to_list_model,
                                          to_sq_model)
                self.view.move_piece(from_list_view, from_sq_view, to_list_view,
                                         to_sq_view, False)
                if to_list_view is self.view.main_board:
                    self.check_slide(to_sq_view, "red")
                self.display_all_starts()
                self.change_player()
            else:
                # move doesn't exist, forfeit turn
                self.view.display_text("No move possible. Click draw pile \n to forfeit turn.")
                block = 1000
                while block != 500:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    block = self.view.get_block(x, y)
                self.change_player()
        elif self.player1.get_color() == 'blue':
            if self.four_card_move_exists('blue'):
                # get click
                legal_move = False
                while legal_move == False:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    from_block = self.view.get_block(x, y)
                    # check if on main_board
                    if 0 <= from_block <= 59:
                        to_block = (from_block + 60 - 4) % 60
                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                                self.model.main_board, to_block, 'blue')
                    # check if in safety_zone
                    elif from_block == 404:
                        to_block = from_block - 4
                        legal_move = self.check_legal_move(self.model.blue_safety, 4,
                                                self.model.blue_safety, 0, 'blue')
                    elif 400 <= from_block <= 403:
                        to_block = from_block - 400 - 4 + 44
                        legal_move = self.check_legal_move(self.model.blue_safety, from_block - 400,
                                                self.model.main_board, to_block, 'blue')
                # carry out legal move
                from_list_model, from_sq_model = self.get_list_and_square_from_model(from_block)
                to_list_model, to_sq_model = self.get_list_and_square_from_model(to_block)
                from_list_view, from_sq_view = self.get_list_and_square_from_view(from_block)
                to_list_view, to_sq_view = self.get_list_and_square_from_view(to_block)
                
                self.model.move_piece(from_list_model, from_sq_model, to_list_model,
                                          to_sq_model)
                self.view.move_piece(from_list_view, from_sq_view, to_list_view,
                                         to_sq_view, False)
                if to_list_view is self.view.main_board:
                    self.check_slide(to_sq_view, "blue")
                self.display_all_starts()
                self.change_player()
            else:
                # move doesn't exist, forfeit turn
                self.view.display_text("No move possible. Click draw pile \n to forfeit turn.")
                block = 1000
                while block != 500:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    block = self.view.get_block(x, y)
                self.change_player()

    def five_card_player1(self):
        """
        Does: plays out 'five card' scenario
        """
        self.view.display_text('Click on piece to move five squares.')
        if self.player1.get_color() == 'yellow':
            if self.five_card_move_exists('yellow'):
                # get click
                legal_move = False
                while legal_move == False:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    from_block = self.view.get_block(x, y)
                    # check if entering safety zone
                    if from_block <= 58 and from_block + 5 > 58:
                        to_block = (from_block + 5) % 59 + 100
                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                            self.model.yellow_safety, to_block - 100, 'yellow')
                    
                    # check if on main_board
                    elif 0 <= from_block <= 59:
                        to_block = (from_block + 5) % 60
                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                            self.model.main_board, to_block, 'yellow')
                    # check if in safety_zone
                    elif from_block == 100:
                        to_block = from_block + 5
                        legal_move = self.check_legal_move(self.model.yellow_safety,
                                            from_block - 100, self.model.yellow_safety,
                                            to_block - 100, 'yellow')
                # carry out legal move
                from_list_model, from_sq_model = self.get_list_and_square_from_model(from_block)
                to_list_model, to_sq_model = self.get_list_and_square_from_model(to_block)
                from_list_view, from_sq_view = self.get_list_and_square_from_view(from_block)
                to_list_view, to_sq_view = self.get_list_and_square_from_view(to_block)
                
                self.model.move_piece(from_list_model, from_sq_model, to_list_model,
                                          to_sq_model)
                self.view.move_piece(from_list_view, from_sq_view, to_list_view,
                                         to_sq_view)
                if to_list_view is self.view.main_board:
                    self.check_slide(to_sq_view, "yellow")
                if to_list_model is self.model.yellow_safety and to_sq_model == 5:
                    self.check_win('yellow')
                self.display_all_starts()
                self.change_player()
                    
            else:
                # move doesn't exist: forfeit turn
                self.view.display_text("No move possible. Click draw pile \n to forfeit turn.")
                block = 1000
                while block != 500:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    block = self.view.get_block(x, y)
                self.change_player()
        elif self.player1.get_color() == 'green':
            if self.five_card_move_exists('green'):
                # get click
                legal_move = False
                while legal_move == False:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    from_block = self.view.get_block(x, y)
                    # check if entering safety zone
                    if from_block <= 13 and from_block + 5 > 13:
                        to_block = (from_block + 5) % 14 + 200
                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                            self.model.green_safety, to_block - 200, 'green')
                    
                    # check if on main_board
                    elif 0 <= from_block <= 59:
                        to_block = (from_block + 5) % 60
                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                            self.model.main_board, to_block, 'green')
                    # check if in safety_zone
                    elif from_block == 200:
                        to_block = from_block + 5
                        legal_move = self.check_legal_move(self.model.green_safety,
                                            from_block - 200, self.model.green_safety,
                                            to_block - 200, 'green')
                # carry out legal move
                from_list_model, from_sq_model = self.get_list_and_square_from_model(from_block)
                to_list_model, to_sq_model = self.get_list_and_square_from_model(to_block)
                from_list_view, from_sq_view = self.get_list_and_square_from_view(from_block)
                to_list_view, to_sq_view = self.get_list_and_square_from_view(to_block)
                
                self.model.move_piece(from_list_model, from_sq_model, to_list_model,
                                          to_sq_model)
                self.view.move_piece(from_list_view, from_sq_view, to_list_view,
                                         to_sq_view)
                if to_list_view is self.view.main_board:
                    self.check_slide(to_sq_view, "green")
                if to_list_model is self.model.green_safety and to_sq_model == 5:
                    self.check_win('green')
                self.display_all_starts()
                self.change_player()
                    
            else:
                # move doesn't exist: forfeit turn
                self.view.display_text("No move possible. Click draw pile \n to forfeit turn.")
                block = 1000
                while block != 500:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    block = self.view.get_block(x, y)
                self.change_player()
        elif self.player1.get_color() == 'red':
            if self.five_card_move_exists('red'):
                # get click
                legal_move = False
                while legal_move == False:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    from_block = self.view.get_block(x, y)
                    # check if entering safety zone
                    if from_block <= 28 and from_block + 5 > 28:
                        to_block = (from_block + 5) % 29 + 300
                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                            self.model.red_safety, to_block - 300, 'red')
                    
                    # check if on main_board
                    elif 0 <= from_block <= 59:
                        to_block = (from_block + 5) % 60
                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                            self.model.main_board, to_block, 'red')
                    # check if in safety_zone
                    elif from_block == 300:
                        to_block = from_block + 5
                        legal_move = self.check_legal_move(self.model.red_safety,
                                            from_block - 300, self.model.red_safety,
                                            to_block - 300, 'red')
                # carry out legal move
                from_list_model, from_sq_model = self.get_list_and_square_from_model(from_block)
                to_list_model, to_sq_model = self.get_list_and_square_from_model(to_block)
                from_list_view, from_sq_view = self.get_list_and_square_from_view(from_block)
                to_list_view, to_sq_view = self.get_list_and_square_from_view(to_block)
                
                self.model.move_piece(from_list_model, from_sq_model, to_list_model,
                                          to_sq_model)
                self.view.move_piece(from_list_view, from_sq_view, to_list_view,
                                         to_sq_view)
                if to_list_view is self.view.main_board:
                    self.check_slide(to_sq_view, "red")
                if to_list_model is self.model.red_safety and to_sq_model == 5:
                    self.check_win('red')
                self.display_all_starts()
                self.change_player()
                    
            else:
                # move doesn't exist: forfeit turn
                self.view.display_text("No move possible. Click draw pile \n to forfeit turn.")
                block = 1000
                while block != 500:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    block = self.view.get_block(x, y)
                self.change_player()
        elif self.player1.get_color() == 'blue':
            if self.five_card_move_exists('blue'):
                # get click
                legal_move = False
                while legal_move == False:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    from_block = self.view.get_block(x, y)
                    # check if entering safety zone
                    if from_block <= 43 and from_block + 5 > 43:
                        to_block = (from_block + 5) % 44 + 400
                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                            self.model.blue_safety, to_block - 400, 'blue')
                    
                    # check if on main_board
                    elif 0 <= from_block <= 59:
                        to_block = (from_block + 5) % 60
                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                            self.model.main_board, to_block, 'blue')
                    # check if in safety_zone
                    elif from_block == 400:
                        to_block = from_block + 5
                        legal_move = self.check_legal_move(self.model.blue_safety,
                                            from_block - 400, self.model.blue_safety,
                                            to_block - 400, 'blue')
                # carry out legal move
                from_list_model, from_sq_model = self.get_list_and_square_from_model(from_block)
                to_list_model, to_sq_model = self.get_list_and_square_from_model(to_block)
                from_list_view, from_sq_view = self.get_list_and_square_from_view(from_block)
                to_list_view, to_sq_view = self.get_list_and_square_from_view(to_block)
                
                self.model.move_piece(from_list_model, from_sq_model, to_list_model,
                                          to_sq_model)
                self.view.move_piece(from_list_view, from_sq_view, to_list_view,
                                         to_sq_view)
                if to_list_view is self.view.main_board:
                    self.check_slide(to_sq_view, "blue")
                if to_list_model is self.model.blue_safety and to_sq_model == 5:
                    self.check_win('blue')
                self.display_all_starts()
                self.change_player()
                    
            else:
                # move doesn't exist: forfeit turn
                self.view.display_text("No move possible. Click draw pile \n to forfeit turn.")
                block = 1000
                while block != 500:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    block = self.view.get_block(x, y)
                self.change_player()

    def count_spaces(self, from_block, to_block):
        """
        Does: counts the number of spaces traveled between blocks
        Returns: int, number of spaces
        """
        num_spaces = 0
        if from_block == to_block:
            num_spaces = 0
        elif from_block > 59 and 0 <= to_block <= 59:
            num_spaces = 0
        elif from_block > 59 and to_block > 59:
            num_spaces = to_block - from_block
            if 1 <= num_spaces <= 5:
                return num_spaces
            else:
                return 0
        elif 0 <= from_block <= 59 and 0 <= to_block <= 59:
            if to_block > from_block:
                num_spaces = to_block - from_block
            else:
                num_spaces = 60 - from_block + to_block
        elif 0 <= from_block <= 59 and to_block > 59:
            if 100 <= to_block <= 105:
                if from_block <= 58:
                    num_spaces = 58 - from_block + to_block - 99
                else:
                    num_spaces = 60 - from_block + 58 + to_block - 99
            elif 200 <= to_block <= 205:
                if from_block <= 13:
                    num_spaces = 13 - from_block + to_block - 199
                else:
                    num_spaces = 60 - from_block + 13 + to_block - 199
            elif 300 <= to_block <= 305:
                if from_block <= 28:
                    num_spaces = 28 - from_block + to_block - 299
                else:
                    num_spaces = 60 - from_block + 28 + to_block - 299
            elif 400 <= to_block <= 405:
                if from_block <= 43:
                    num_spaces = 43 - from_block + to_block - 399
                else:
                    num_spaces = 60 - from_block + 43 + to_block - 399
        return num_spaces

    def seven_card_player1(self):
        """
        Does: plays out 'seven card' scenario
        """
        if self.player1.get_color() == 'yellow':
            if self.seven_card_move_exists('yellow'):
                legal_moves = False
                while legal_moves == False:
                    first_legal_move = False
                    second_legal_move = False
                    self.view.display_text("Move may be divided by 2 pieces. \n Click on first piece.")
                    # get click for first move
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    from_block1 = self.view.get_block(x, y)
                    first_click_good = False
                    if 0 <= from_block1 <= 59:
                        if self.model.main_board[from_block1].is_occupied():
                            if self.model.main_board[from_block1].get_color() == 'yellow':
                                first_click_good = True
                    elif 100 <= from_block1 <= 104:
                        if self.model.yellow_safety[from_block1 - 100].is_occupied():
                            first_click_good = True
                    # check if first click is good
                    if first_click_good == True:
                        self.view.display_text("Click on space you want to \n move to. (Maximum 7 spaces.)")
                        # get second click
                        click_point = self.view.win.getMouse()
                        x = click_point.getX()
                        y = click_point.getY()
                        to_block1 = self.view.get_block(x, y)
                        num_spaces = self.count_spaces(from_block1, to_block1)
                        if 1 <= num_spaces <= 7:
                            if 0 <= from_block1 <= 59 and 0 <= to_block1 <= 59:
                                # check move from main board to main board
                                first_legal_move = self.check_legal_move(self.model.main_board, from_block1,
                                                                         self.model.main_board, to_block1, 'yellow')
                            elif 0 <= from_block1 <= 59 and 100 <= to_block1 <= 105:
                                # check move from main board to safety zone
                                first_legal_move = self.check_legal_move(self.model.main_board, from_block1,
                                                                         self.model.yellow_safety, to_block1 - 100, 'yellow')
                            elif 100 <= from_block1 <= 104 and 100 <= to_block1 <= 105:
                                # check move from safety zone to safety zone
                                first_legal_move = self.check_legal_move(self.model.yellow_safety, from_block1 - 100,
                                                                         self.model.yellow_safety, to_block1 - 100, 'yellow')
                            if first_legal_move:
                                remaining = 7 - num_spaces
                                if remaining == 0:
                                    second_legal_move = True
                                elif remaining > 0:
                                    self.view.display_text("Click on second piece to move \n{} spaces.".format(str(remaining)))
                                    # get click for final piece
                                    click_point = self.view.win.getMouse()
                                    x = click_point.getX()
                                    y = click_point.getY()
                                    from_block2 = self.view.get_block(x, y)
                                    good_so_far = False
                                    if 0 <= from_block2 <= 59:
                                        if self.model.main_board[from_block2].is_occupied():
                                            if self.model.main_board[from_block2].get_color() == 'yellow':
                                                good_so_far = True
                                    elif 100 <= from_block2 <= 104:
                                        if self.model.yellow_safety[from_block2 - 100].is_occupied():
                                            good_so_far = True
                                    if good_so_far:
                                        if from_block1 == from_block2:
                                            second_legal_move = False
                                        elif 100 <= from_block2 <= 104 and 100 <= from_block2 + remaining <= 105:
                                            # checking if move is in safety zone
                                            to_block2 = from_block2 + remaining
                                            # prove legal move
                                            if to_block2 == to_block1:
                                                if self.model.yellow_safety[to_block2 - 100].is_home():
                                                    second_legal_move = True
                                                else:
                                                    second_legal_move = False
                                            elif self.model.yellow_safety[to_block2 - 100].is_home():
                                                second_legal_move = True
                                            elif self.model.yellow_safety[to_block2 - 100].is_occupied():
                                                second_legal_move = False
                                            elif not self.model.yellow_safety[to_block2 - 100].is_occupied():
                                                second_legal_move = True
                                        elif from_block2 <= 58 and from_block2 + remaining > 58:
                                            # checking if entering safety zone
                                            to_block2 = (from_block2 + remaining) % 59 + 100
                                            # prove legal move
                                            if to_block1 == 50 and 50 <= from_block2 <= 54:
                                                # second piece will get knocked off on slide
                                                second_legal_move = False
                                            elif to_block2 == to_block1:
                                                if self.model.yellow_safety[to_block2 - 100].is_home():
                                                    second_legal_move = True
                                                else:
                                                    second_legal_move = False
                                            elif self.model.yellow_safety[to_block2 - 100].is_home():
                                                second_legal_move = True
                                            elif self.model.yellow_safety[to_block2 - 100].is_occupied():
                                                second_legal_move = False
                                            elif not self.model.yellow_safety[to_block2 - 100].is_occupied():
                                                second_legal_move = True
                                        elif 0 <= from_block2 <= 59 and 0 <= (from_block2 + remaining) % 60 <= 59:
                                            # checking if move is on mainboard
                                            to_block2 = (from_block2 + remaining) % 60
                                            # prove move is legal, check for sliding
                                            # first move was a slide:
                                            if to_block1 == 12:
                                                if 12 <= from_block2 <= 15:
                                                    # second piece knocked off by slide
                                                    second_legal_move = False
                                                elif to_block2 == 15:
                                                    # second piece lands on first piece after move
                                                    second_legal_move = False
                                                elif 12 <= to_block2 <= 14:
                                                    # second piece lands anywhere else on slide: legal
                                                    second_legal_move = True
                                                else:
                                                    # second piece lands elsewhere on the board
                                                    if to_block2 == from_block1:
                                                        second_legal_move = True
                                                    else:
                                                        # check legality
                                                        second_legal_move = self.check_legal_move(self.model.main_board, from_block2,
                                                            self.model.main_board, to_block2, 'yellow')
                                            elif to_block1 == 20:
                                                if 20 <= from_block2 <= 24:
                                                    # second piece knocked off by slide
                                                    second_legal_move = False
                                                elif to_block2 == 24:
                                                    # second piece lands on first piece after move
                                                    second_legal_move = False
                                                elif 20 <= to_block2 <= 23:
                                                    # second piece lands anywhere else on slide: legal
                                                    second_legal_move = True
                                                else:
                                                    # second piece lands elsewhere on the board
                                                    if to_block2 == from_block1:
                                                        second_legal_move = True
                                                    else:
                                                        # check legality
                                                        second_legal_move = self.check_legal_move(self.model.main_board, from_block2,
                                                            self.model.main_board, to_block2, 'yellow')
                                            elif to_block1 == 27:
                                                if 27 <= from_block2 <= 30:
                                                    # second piece knocked off by slide
                                                    second_legal_move = False
                                                elif to_block2 == 30:
                                                    # second piece lands on first piece after move
                                                    second_legal_move = False
                                                elif 27 <= to_block2 <= 29:
                                                    # second piece lands anywhere else on slide: legal
                                                    second_legal_move = True
                                                else:
                                                    # second piece lands elsewhere on the board
                                                    if to_block2 == from_block1:
                                                        second_legal_move = True
                                                    else:
                                                        # check legality
                                                        second_legal_move = self.check_legal_move(self.model.main_board, from_block2,
                                                            self.model.main_board, to_block2, 'yellow')
                                            elif to_block1 == 35:
                                                if 35 <= from_block2 <= 39:
                                                    # second piece knocked off by slide
                                                    second_legal_move = False
                                                elif to_block2 == 39:
                                                    # second piece lands on first piece after move
                                                    second_legal_move = False
                                                elif 35 <= to_block2 <= 38:
                                                    # second piece lands anywhere else on slide: legal
                                                    second_legal_move = True
                                                else:
                                                    # second piece lands elsewhere on the board
                                                    if to_block2 == from_block1:
                                                        second_legal_move = True
                                                    else:
                                                        # check legality
                                                        second_legal_move = self.check_legal_move(self.model.main_board, from_block2,
                                                            self.model.main_board, to_block2, 'yellow')
                                            elif to_block1 == 42:
                                                if 42 <= from_block2 <= 45:
                                                    # second piece knocked off by slide
                                                    second_legal_move = False
                                                elif to_block2 == 45:
                                                    # second piece lands on first piece after move
                                                    second_legal_move = False
                                                elif 42 <= to_block2 <= 44:
                                                    # second piece lands anywhere else on slide: legal
                                                    second_legal_move = True
                                                else:
                                                    # second piece lands elsewhere on the board
                                                    if to_block2 == from_block1:
                                                        second_legal_move = True
                                                    else:
                                                        # check legality
                                                        second_legal_move = self.check_legal_move(self.model.main_board, from_block2,
                                                            self.model.main_board, to_block2, 'yellow')
                                            elif to_block1 == 50:
                                                if 50 <= from_block2 <= 54:
                                                    # second piece knocked off by slide
                                                    second_legal_move = False
                                                elif to_block2 == 54:
                                                    # second piece lands on first piece after move
                                                    second_legal_move = False
                                                elif 50 <= to_block2 <= 53:
                                                    # second piece lands anywhere else on slide: legal
                                                    second_legal_move = True
                                                else:
                                                    # second piece lands elsewhere on the board
                                                    if to_block2 == from_block1:
                                                        second_legal_move = True
                                                    else:
                                                        # check legality
                                                        second_legal_move = self.check_legal_move(self.model.main_board, from_block2,
                                                            self.model.main_board, to_block2, 'yellow')
                                            else:
                                                # first move was not a slide
                                                if to_block1 == to_block2:
                                                    second_legal_move = False
                                                elif to_block2 == from_block1:
                                                    second_legal_move = True
                                                else:
                                                    second_legal_move = self.check_legal_move(self.model.main_board, from_block2,
                                                            self.model.main_board, to_block2, 'yellow')
                    # check if both moves are legal to exit while loop
                    if first_legal_move and second_legal_move:
                        legal_moves = True
                # carry out legal moves
                from_list_model1, from_sq_model1 = self.get_list_and_square_from_model(from_block1)
                to_list_model1, to_sq_model1 = self.get_list_and_square_from_model(to_block1)
                from_list_view1, from_sq_view1 = self.get_list_and_square_from_view(from_block1)
                to_list_view1, to_sq_view1 = self.get_list_and_square_from_view(to_block1)
                
                self.model.move_piece(from_list_model1, from_sq_model1, to_list_model1,
                                          to_sq_model1)
                self.view.move_piece(from_list_view1, from_sq_view1, to_list_view1,
                                         to_sq_view1)
                if to_list_view1 is self.view.main_board:
                    self.check_slide(to_sq_view1, "yellow")
                if to_list_model1 is self.model.yellow_safety and to_sq_model1 == 5:
                    self.check_win('yellow')
                self.display_all_starts()
                # carry out second legal move if necessary
                if remaining > 0:
                    from_list_model2, from_sq_model2 = self.get_list_and_square_from_model(from_block2)
                    to_list_model2, to_sq_model2 = self.get_list_and_square_from_model(to_block2)
                    from_list_view2, from_sq_view2 = self.get_list_and_square_from_view(from_block2)
                    to_list_view2, to_sq_view2 = self.get_list_and_square_from_view(to_block2)
                    
                    self.model.move_piece(from_list_model2, from_sq_model2, to_list_model2,
                                              to_sq_model2)
                    self.view.move_piece(from_list_view2, from_sq_view2, to_list_view2,
                                             to_sq_view2)
                    if to_list_view2 is self.view.main_board:
                        self.check_slide(to_sq_view2, "yellow")
                    if to_list_model2 is self.model.yellow_safety and to_sq_model2 == 5:
                        self.check_win('yellow')
                    self.display_all_starts()
                # change player
                self.change_player()
            else:
                # no move exists: forfeit turn
                self.view.display_text("No move possible. Click draw pile \n to forfeit turn.")
                block = 1000
                while block != 500:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    block = self.view.get_block(x, y)
                self.change_player()
        elif self.player1.get_color() == 'green':
            if self.seven_card_move_exists('green'):
                legal_moves = False
                while legal_moves == False:
                    first_legal_move = False
                    second_legal_move = False
                    self.view.display_text("Move may be divided by 2 pieces. \n Click on first piece.")
                    # get click for first move
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    from_block1 = self.view.get_block(x, y)
                    first_click_good = False
                    if 0 <= from_block1 <= 59:
                        if self.model.main_board[from_block1].is_occupied():
                            if self.model.main_board[from_block1].get_color() == 'green':
                                first_click_good = True
                    elif 200 <= from_block1 <= 204:
                        if self.model.green_safety[from_block1 - 200].is_occupied():
                            first_click_good = True
                    # check if first click is good
                    if first_click_good == True:
                        self.view.display_text("Click on space you want to \n move to. (Maximum 7 spaces.)")
                        # get second click
                        click_point = self.view.win.getMouse()
                        x = click_point.getX()
                        y = click_point.getY()
                        to_block1 = self.view.get_block(x, y)
                        num_spaces = self.count_spaces(from_block1, to_block1)
                        if 1 <= num_spaces <= 7:
                            if 0 <= from_block1 <= 59 and 0 <= to_block1 <= 59:
                                # check move from main board to main board
                                first_legal_move = self.check_legal_move(self.model.main_board, from_block1,
                                                                         self.model.main_board, to_block1, 'green')
                            elif 0 <= from_block1 <= 59 and 200 <= to_block1 <= 205:
                                # check move from main board to safety zone
                                first_legal_move = self.check_legal_move(self.model.main_board, from_block1,
                                                                         self.model.green_safety, to_block1 - 200, 'green')
                            elif 200 <= from_block1 <= 204 and 200 <= to_block1 <= 205:
                                # check move from safety zone to safety zone
                                first_legal_move = self.check_legal_move(self.model.green_safety, from_block1 - 200,
                                                                         self.model.green_safety, to_block1 - 200, 'green')
                            if first_legal_move:
                                remaining = 7 - num_spaces
                                if remaining == 0:
                                    second_legal_move = True
                                elif remaining > 0:
                                    self.view.display_text("Click on second piece to move \n{} spaces.".format(str(remaining)))
                                    # get click for final piece
                                    click_point = self.view.win.getMouse()
                                    x = click_point.getX()
                                    y = click_point.getY()
                                    from_block2 = self.view.get_block(x, y)
                                    good_so_far = False
                                    if 0 <= from_block2 <= 59:
                                        if self.model.main_board[from_block2].is_occupied():
                                            if self.model.main_board[from_block2].get_color() == 'green':
                                                good_so_far = True
                                    elif 200 <= from_block2 <= 204:
                                        if self.model.green_safety[from_block2 - 200].is_occupied():
                                            good_so_far = True
                                    if good_so_far:
                                        if from_block1 == from_block2:
                                            second_legal_move = False
                                        elif 200 <= from_block2 <= 204 and 200 <= from_block2 + remaining <= 205:
                                            # checking if move is in safety zone
                                            to_block2 = from_block2 + remaining
                                            # prove legal move
                                            if to_block2 == to_block1:
                                                if self.model.green_safety[to_block2 - 200].is_home():
                                                    second_legal_move = True
                                                else:
                                                    second_legal_move = False
                                            elif self.model.green_safety[to_block2 - 200].is_home():
                                                second_legal_move = True
                                            elif self.model.green_safety[to_block2 - 200].is_occupied():
                                                second_legal_move = False
                                            elif not self.model.green_safety[to_block2 - 200].is_occupied():
                                                second_legal_move = True
                                        elif from_block2 <= 13 and from_block2 + remaining > 13:
                                            # checking if entering safety zone
                                            to_block2 = (from_block2 + remaining) % 14 + 200
                                            # prove legal move
                                            if to_block1 == 5 and 5 <= from_block2 <= 9:
                                                # second piece will get knocked off on slide
                                                second_legal_move = False
                                            elif to_block2 == to_block1:
                                                if self.model.green_safety[to_block2 - 200].is_home():
                                                    second_legal_move = True
                                                else:
                                                    second_legal_move = False
                                            elif self.model.green_safety[to_block2 - 200].is_home():
                                                second_legal_move = True
                                            elif self.model.green_safety[to_block2 - 200].is_occupied():
                                                second_legal_move = False
                                            elif not self.model.green_safety[to_block2 - 200].is_occupied():
                                                second_legal_move = True
                                        elif 0 <= from_block2 <= 59 and 0 <= (from_block2 + remaining) % 60 <= 59:
                                            # checking if move is on mainboard
                                            to_block2 = (from_block2 + remaining) % 60
                                            # prove move is legal, check for sliding
                                            # first move was a slide:
                                            if to_block1 == 57:
                                                if 57 <= from_block2 <= 59 or from_block2 == 0:
                                                    # second piece knocked off by slide
                                                    second_legal_move = False
                                                elif to_block2 == 0:
                                                    # second piece lands on first piece after move
                                                    second_legal_move = False
                                                elif 57 <= to_block2 <= 59:
                                                    # second piece lands anywhere else on slide: legal
                                                    second_legal_move = True
                                                else:
                                                    # second piece lands elsewhere on the board
                                                    if to_block2 == from_block1:
                                                        second_legal_move = True
                                                    else:
                                                        # check legality
                                                        second_legal_move = self.check_legal_move(self.model.main_board, from_block2,
                                                            self.model.main_board, to_block2, 'green')
                                            elif to_block1 == 5:
                                                if 5 <= from_block2 <= 9:
                                                    # second piece knocked off by slide
                                                    second_legal_move = False
                                                elif to_block2 == 9:
                                                    # second piece lands on first piece after move
                                                    second_legal_move = False
                                                elif 5 <= to_block2 <= 8:
                                                    # second piece lands anywhere else on slide: legal
                                                    second_legal_move = True
                                                else:
                                                    # second piece lands elsewhere on the board
                                                    if to_block2 == from_block1:
                                                        second_legal_move = True
                                                    else:
                                                        # check legality
                                                        second_legal_move = self.check_legal_move(self.model.main_board, from_block2,
                                                            self.model.main_board, to_block2, 'green')
                                            elif to_block1 == 27:
                                                if 27 <= from_block2 <= 30:
                                                    # second piece knocked off by slide
                                                    second_legal_move = False
                                                elif to_block2 == 30:
                                                    # second piece lands on first piece after move
                                                    second_legal_move = False
                                                elif 27 <= to_block2 <= 29:
                                                    # second piece lands anywhere else on slide: legal
                                                    second_legal_move = True
                                                else:
                                                    # second piece lands elsewhere on the board
                                                    if to_block2 == from_block1:
                                                        second_legal_move = True
                                                    else:
                                                        # check legality
                                                        second_legal_move = self.check_legal_move(self.model.main_board, from_block2,
                                                            self.model.main_board, to_block2, 'green')
                                            elif to_block1 == 35:
                                                if 35 <= from_block2 <= 39:
                                                    # second piece knocked off by slide
                                                    second_legal_move = False
                                                elif to_block2 == 39:
                                                    # second piece lands on first piece after move
                                                    second_legal_move = False
                                                elif 35 <= to_block2 <= 38:
                                                    # second piece lands anywhere else on slide: legal
                                                    second_legal_move = True
                                                else:
                                                    # second piece lands elsewhere on the board
                                                    if to_block2 == from_block1:
                                                        second_legal_move = True
                                                    else:
                                                        # check legality
                                                        second_legal_move = self.check_legal_move(self.model.main_board, from_block2,
                                                            self.model.main_board, to_block2, 'green')
                                            elif to_block1 == 42:
                                                if 42 <= from_block2 <= 45:
                                                    # second piece knocked off by slide
                                                    second_legal_move = False
                                                elif to_block2 == 45:
                                                    # second piece lands on first piece after move
                                                    second_legal_move = False
                                                elif 42 <= to_block2 <= 44:
                                                    # second piece lands anywhere else on slide: legal
                                                    second_legal_move = True
                                                else:
                                                    # second piece lands elsewhere on the board
                                                    if to_block2 == from_block1:
                                                        second_legal_move = True
                                                    else:
                                                        # check legality
                                                        second_legal_move = self.check_legal_move(self.model.main_board, from_block2,
                                                            self.model.main_board, to_block2, 'green')
                                            elif to_block1 == 50:
                                                if 50 <= from_block2 <= 54:
                                                    # second piece knocked off by slide
                                                    second_legal_move = False
                                                elif to_block2 == 54:
                                                    # second piece lands on first piece after move
                                                    second_legal_move = False
                                                elif 50 <= to_block2 <= 53:
                                                    # second piece lands anywhere else on slide: legal
                                                    second_legal_move = True
                                                else:
                                                    # second piece lands elsewhere on the board
                                                    if to_block2 == from_block1:
                                                        second_legal_move = True
                                                    else:
                                                        # check legality
                                                        second_legal_move = self.check_legal_move(self.model.main_board, from_block2,
                                                            self.model.main_board, to_block2, 'green')
                                            else:
                                                # first move was not a slide
                                                if to_block1 == to_block2:
                                                    second_legal_move = False
                                                elif to_block2 == from_block1:
                                                    second_legal_move = True
                                                else:
                                                    second_legal_move = self.check_legal_move(self.model.main_board, from_block2,
                                                            self.model.main_board, to_block2, 'green')
                    # check if both moves are legal to exit while loop
                    if first_legal_move and second_legal_move:
                        legal_moves = True
                # carry out legal moves
                from_list_model1, from_sq_model1 = self.get_list_and_square_from_model(from_block1)
                to_list_model1, to_sq_model1 = self.get_list_and_square_from_model(to_block1)
                from_list_view1, from_sq_view1 = self.get_list_and_square_from_view(from_block1)
                to_list_view1, to_sq_view1 = self.get_list_and_square_from_view(to_block1)
                
                self.model.move_piece(from_list_model1, from_sq_model1, to_list_model1,
                                          to_sq_model1)
                self.view.move_piece(from_list_view1, from_sq_view1, to_list_view1,
                                         to_sq_view1)
                if to_list_view1 is self.view.main_board:
                    self.check_slide(to_sq_view1, "green")
                if to_list_model1 is self.model.green_safety and to_sq_model1 == 5:
                    self.check_win('green')
                self.display_all_starts()
                # carry out second legal move if necessary
                if remaining > 0:
                    from_list_model2, from_sq_model2 = self.get_list_and_square_from_model(from_block2)
                    to_list_model2, to_sq_model2 = self.get_list_and_square_from_model(to_block2)
                    from_list_view2, from_sq_view2 = self.get_list_and_square_from_view(from_block2)
                    to_list_view2, to_sq_view2 = self.get_list_and_square_from_view(to_block2)
                    
                    self.model.move_piece(from_list_model2, from_sq_model2, to_list_model2,
                                              to_sq_model2)
                    self.view.move_piece(from_list_view2, from_sq_view2, to_list_view2,
                                             to_sq_view2)
                    if to_list_view2 is self.view.main_board:
                        self.check_slide(to_sq_view2, "green")
                    if to_list_model2 is self.model.green_safety and to_sq_model2 == 5:
                        self.check_win('green')
                    self.display_all_starts()
                # change player
                self.change_player()
            else:
                # no move exists: forfeit turn
                self.view.display_text("No move possible. Click draw pile \n to forfeit turn.")
                block = 1000
                while block != 500:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    block = self.view.get_block(x, y)
                self.change_player()
        elif self.player1.get_color() == 'red':
            if self.seven_card_move_exists('red'):
                legal_moves = False
                while legal_moves == False:
                    first_legal_move = False
                    second_legal_move = False
                    self.view.display_text("Move may be divided by 2 pieces. \n Click on first piece.")
                    # get click for first move
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    from_block1 = self.view.get_block(x, y)
                    first_click_good = False
                    if 0 <= from_block1 <= 59:
                        if self.model.main_board[from_block1].is_occupied():
                            if self.model.main_board[from_block1].get_color() == 'red':
                                first_click_good = True
                    elif 300 <= from_block1 <= 304:
                        if self.model.red_safety[from_block1 - 300].is_occupied():
                            first_click_good = True
                    # check if first click is good
                    if first_click_good == True:
                        self.view.display_text("Click on space you want to \n move to. (Maximum 7 spaces.)")
                        # get second click
                        click_point = self.view.win.getMouse()
                        x = click_point.getX()
                        y = click_point.getY()
                        to_block1 = self.view.get_block(x, y)
                        num_spaces = self.count_spaces(from_block1, to_block1)
                        if 1 <= num_spaces <= 7:
                            if 0 <= from_block1 <= 59 and 0 <= to_block1 <= 59:
                                # check move from main board to main board
                                first_legal_move = self.check_legal_move(self.model.main_board, from_block1,
                                                                         self.model.main_board, to_block1, 'red')
                            elif 0 <= from_block1 <= 59 and 300 <= to_block1 <= 305:
                                # check move from main board to safety zone
                                first_legal_move = self.check_legal_move(self.model.main_board, from_block1,
                                                                         self.model.red_safety, to_block1 - 300, 'red')
                            elif 300 <= from_block1 <= 304 and 300 <= to_block1 <= 305:
                                # check move from safety zone to safety zone
                                first_legal_move = self.check_legal_move(self.model.red_safety, from_block1 - 300,
                                                                         self.model.red_safety, to_block1 - 300, 'red')
                            if first_legal_move:
                                remaining = 7 - num_spaces
                                if remaining == 0:
                                    second_legal_move = True
                                elif remaining > 0:
                                    self.view.display_text("Click on second piece to move \n{} spaces.".format(str(remaining)))
                                    # get click for final piece
                                    click_point = self.view.win.getMouse()
                                    x = click_point.getX()
                                    y = click_point.getY()
                                    from_block2 = self.view.get_block(x, y)
                                    good_so_far = False
                                    if 0 <= from_block2 <= 59:
                                        if self.model.main_board[from_block2].is_occupied():
                                            if self.model.main_board[from_block2].get_color() == 'red':
                                                good_so_far = True
                                    elif 300 <= from_block2 <= 304:
                                        if self.model.red_safety[from_block2 - 300].is_occupied():
                                            good_so_far = True
                                    if good_so_far:
                                        if from_block1 == from_block2:
                                            second_legal_move = False
                                        elif 300 <= from_block2 <= 304 and 300 <= from_block2 + remaining <= 305:
                                            # checking if move is in safety zone
                                            to_block2 = from_block2 + remaining
                                            # prove legal move
                                            if to_block2 == to_block1:
                                                if self.model.red_safety[to_block2 - 300].is_home():
                                                    second_legal_move = True
                                                else:
                                                    second_legal_move = False
                                            elif self.model.red_safety[to_block2 - 300].is_home():
                                                second_legal_move = True
                                            elif self.model.red_safety[to_block2 - 300].is_occupied():
                                                second_legal_move = False
                                            elif not self.model.red_safety[to_block2 - 300].is_occupied():
                                                second_legal_move = True
                                        elif from_block2 <= 28 and from_block2 + remaining > 28:
                                            # checking if entering safety zone
                                            to_block2 = (from_block2 + remaining) % 29 + 300
                                            # prove legal move
                                            if to_block1 == 20 and 20 <= from_block2 <= 24:
                                                # second piece will get knocked off on slide
                                                second_legal_move = False
                                            elif to_block2 == to_block1:
                                                if self.model.red_safety[to_block2 - 300].is_home():
                                                    second_legal_move = True
                                                else:
                                                    second_legal_move = False
                                            elif self.model.red_safety[to_block2 - 300].is_home():
                                                second_legal_move = True
                                            elif self.model.red_safety[to_block2 - 300].is_occupied():
                                                second_legal_move = False
                                            elif not self.model.red_safety[to_block2 - 300].is_occupied():
                                                second_legal_move = True
                                        elif 0 <= from_block2 <= 59 and 0 <= (from_block2 + remaining) % 60 <= 59:
                                            # checking if move is on mainboard
                                            to_block2 = (from_block2 + remaining) % 60
                                            # prove move is legal, check for sliding
                                            # first move was a slide:
                                            if to_block1 == 57:
                                                if 57 <= from_block2 <= 59 or from_block2 == 0:
                                                    # second piece knocked off by slide
                                                    second_legal_move = False
                                                elif to_block2 == 0:
                                                    # second piece lands on first piece after move
                                                    second_legal_move = False
                                                elif 57 <= to_block2 <= 59:
                                                    # second piece lands anywhere else on slide: legal
                                                    second_legal_move = True
                                                else:
                                                    # second piece lands elsewhere on the board
                                                    if to_block2 == from_block1:
                                                        second_legal_move = True
                                                    else:
                                                        # check legality
                                                        second_legal_move = self.check_legal_move(self.model.main_board, from_block2,
                                                            self.model.main_board, to_block2, 'red')
                                            elif to_block1 == 5:
                                                if 5 <= from_block2 <= 9:
                                                    # second piece knocked off by slide
                                                    second_legal_move = False
                                                elif to_block2 == 9:
                                                    # second piece lands on first piece after move
                                                    second_legal_move = False
                                                elif 5 <= to_block2 <= 8:
                                                    # second piece lands anywhere else on slide: legal
                                                    second_legal_move = True
                                                else:
                                                    # second piece lands elsewhere on the board
                                                    if to_block2 == from_block1:
                                                        second_legal_move = True
                                                    else:
                                                        # check legality
                                                        second_legal_move = self.check_legal_move(self.model.main_board, from_block2,
                                                            self.model.main_board, to_block2, 'red')
                                            elif to_block1 == 12:
                                                if 12 <= from_block2 <= 15:
                                                    # second piece knocked off by slide
                                                    second_legal_move = False
                                                elif to_block2 == 15:
                                                    # second piece lands on first piece after move
                                                    second_legal_move = False
                                                elif 12 <= to_block2 <= 14:
                                                    # second piece lands anywhere else on slide: legal
                                                    second_legal_move = True
                                                else:
                                                    # second piece lands elsewhere on the board
                                                    if to_block2 == from_block1:
                                                        second_legal_move = True
                                                    else:
                                                        # check legality
                                                        second_legal_move = self.check_legal_move(self.model.main_board, from_block2,
                                                            self.model.main_board, to_block2, 'red')
                                            elif to_block1 == 20:
                                                if 20 <= from_block2 <= 24:
                                                    # second piece knocked off by slide
                                                    second_legal_move = False
                                                elif to_block2 == 24:
                                                    # second piece lands on first piece after move
                                                    second_legal_move = False
                                                elif 20 <= to_block2 <= 23:
                                                    # second piece lands anywhere else on slide: legal
                                                    second_legal_move = True
                                                else:
                                                    # second piece lands elsewhere on the board
                                                    if to_block2 == from_block1:
                                                        second_legal_move = True
                                                    else:
                                                        # check legality
                                                        second_legal_move = self.check_legal_move(self.model.main_board, from_block2,
                                                            self.model.main_board, to_block2, 'red')
                                            elif to_block1 == 42:
                                                if 42 <= from_block2 <= 45:
                                                    # second piece knocked off by slide
                                                    second_legal_move = False
                                                elif to_block2 == 45:
                                                    # second piece lands on first piece after move
                                                    second_legal_move = False
                                                elif 42 <= to_block2 <= 44:
                                                    # second piece lands anywhere else on slide: legal
                                                    second_legal_move = True
                                                else:
                                                    # second piece lands elsewhere on the board
                                                    if to_block2 == from_block1:
                                                        second_legal_move = True
                                                    else:
                                                        # check legality
                                                        second_legal_move = self.check_legal_move(self.model.main_board, from_block2,
                                                            self.model.main_board, to_block2, 'red')
                                            elif to_block1 == 50:
                                                if 50 <= from_block2 <= 54:
                                                    # second piece knocked off by slide
                                                    second_legal_move = False
                                                elif to_block2 == 54:
                                                    # second piece lands on first piece after move
                                                    second_legal_move = False
                                                elif 50 <= to_block2 <= 53:
                                                    # second piece lands anywhere else on slide: legal
                                                    second_legal_move = True
                                                else:
                                                    # second piece lands elsewhere on the board
                                                    if to_block2 == from_block1:
                                                        second_legal_move = True
                                                    else:
                                                        # check legality
                                                        second_legal_move = self.check_legal_move(self.model.main_board, from_block2,
                                                            self.model.main_board, to_block2, 'red')
                                            else:
                                                # first move was not a slide
                                                if to_block1 == to_block2:
                                                    second_legal_move = False
                                                elif to_block2 == from_block1:
                                                    second_legal_move = True
                                                else:
                                                    second_legal_move = self.check_legal_move(self.model.main_board, from_block2,
                                                            self.model.main_board, to_block2, 'red')
                    # check if both moves are legal to exit while loop
                    if first_legal_move and second_legal_move:
                        legal_moves = True
                # carry out legal moves
                from_list_model1, from_sq_model1 = self.get_list_and_square_from_model(from_block1)
                to_list_model1, to_sq_model1 = self.get_list_and_square_from_model(to_block1)
                from_list_view1, from_sq_view1 = self.get_list_and_square_from_view(from_block1)
                to_list_view1, to_sq_view1 = self.get_list_and_square_from_view(to_block1)
                
                self.model.move_piece(from_list_model1, from_sq_model1, to_list_model1,
                                          to_sq_model1)
                self.view.move_piece(from_list_view1, from_sq_view1, to_list_view1,
                                         to_sq_view1)
                if to_list_view1 is self.view.main_board:
                    self.check_slide(to_sq_view1, "red")
                if to_list_model1 is self.model.red_safety and to_sq_model1 == 5:
                    self.check_win('red')
                self.display_all_starts()
                # carry out second legal move if necessary
                if remaining > 0:
                    from_list_model2, from_sq_model2 = self.get_list_and_square_from_model(from_block2)
                    to_list_model2, to_sq_model2 = self.get_list_and_square_from_model(to_block2)
                    from_list_view2, from_sq_view2 = self.get_list_and_square_from_view(from_block2)
                    to_list_view2, to_sq_view2 = self.get_list_and_square_from_view(to_block2)
                    
                    self.model.move_piece(from_list_model2, from_sq_model2, to_list_model2,
                                              to_sq_model2)
                    self.view.move_piece(from_list_view2, from_sq_view2, to_list_view2,
                                             to_sq_view2)
                    if to_list_view2 is self.view.main_board:
                        self.check_slide(to_sq_view2, "red")
                    if to_list_model2 is self.model.red_safety and to_sq_model2 == 5:
                        self.check_win('red')
                    self.display_all_starts()
                # change player
                self.change_player()
            else:
                # no move exists: forfeit turn
                self.view.display_text("No move possible. Click draw pile \n to forfeit turn.")
                block = 1000
                while block != 500:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    block = self.view.get_block(x, y)
                self.change_player()
        elif self.player1.get_color() == 'blue':
            if self.seven_card_move_exists('blue'):
                legal_moves = False
                while legal_moves == False:
                    first_legal_move = False
                    second_legal_move = False
                    self.view.display_text("Move may be divided by 2 pieces. \n Click on first piece.")
                    # get click for first move
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    from_block1 = self.view.get_block(x, y)
                    first_click_good = False
                    if 0 <= from_block1 <= 59:
                        if self.model.main_board[from_block1].is_occupied():
                            if self.model.main_board[from_block1].get_color() == 'blue':
                                first_click_good = True
                    elif 400 <= from_block1 <= 404:
                        if self.model.blue_safety[from_block1 - 400].is_occupied():
                            first_click_good = True
                    # check if first click is good
                    if first_click_good == True:
                        self.view.display_text("Click on space you want to \n move to. (Maximum 7 spaces.)")
                        # get second click
                        click_point = self.view.win.getMouse()
                        x = click_point.getX()
                        y = click_point.getY()
                        to_block1 = self.view.get_block(x, y)
                        num_spaces = self.count_spaces(from_block1, to_block1)
                        if 1 <= num_spaces <= 7:
                            if 0 <= from_block1 <= 59 and 0 <= to_block1 <= 59:
                                # check move from main board to main board
                                first_legal_move = self.check_legal_move(self.model.main_board, from_block1,
                                                                         self.model.main_board, to_block1, 'blue')
                            elif 0 <= from_block1 <= 59 and 400 <= to_block1 <= 405:
                                # check move from main board to safety zone
                                first_legal_move = self.check_legal_move(self.model.main_board, from_block1,
                                                                         self.model.blue_safety, to_block1 - 400, 'blue')
                            elif 400 <= from_block1 <= 404 and 400 <= to_block1 <= 405:
                                # check move from safety zone to safety zone
                                first_legal_move = self.check_legal_move(self.model.blue_safety, from_block1 - 400,
                                                                         self.model.blue_safety, to_block1 - 400, 'blue')
                            if first_legal_move:
                                remaining = 7 - num_spaces
                                if remaining == 0:
                                    second_legal_move = True
                                elif remaining > 0:
                                    self.view.display_text("Click on second piece to move \n{} spaces.".format(str(remaining)))
                                    # get click for final piece
                                    click_point = self.view.win.getMouse()
                                    x = click_point.getX()
                                    y = click_point.getY()
                                    from_block2 = self.view.get_block(x, y)
                                    good_so_far = False
                                    if 0 <= from_block2 <= 59:
                                        if self.model.main_board[from_block2].is_occupied():
                                            if self.model.main_board[from_block2].get_color() == 'blue':
                                                good_so_far = True
                                    elif 400 <= from_block2 <= 404:
                                        if self.model.blue_safety[from_block2 - 400].is_occupied():
                                            good_so_far = True
                                    if good_so_far:
                                        if from_block1 == from_block2:
                                            second_legal_move = False
                                        elif 400 <= from_block2 <= 404 and 400 <= from_block2 + remaining <= 405:
                                            # checking if move is in safety zone
                                            to_block2 = from_block2 + remaining
                                            # prove legal move
                                            if to_block2 == to_block1:
                                                if self.model.blue_safety[to_block2 - 400].is_home():
                                                    second_legal_move = True
                                                else:
                                                    second_legal_move = False
                                            elif self.model.blue_safety[to_block2 - 400].is_home():
                                                second_legal_move = True
                                            elif self.model.blue_safety[to_block2 - 400].is_occupied():
                                                second_legal_move = False
                                            elif not self.model.blue_safety[to_block2 - 400].is_occupied():
                                                second_legal_move = True
                                        elif from_block2 <= 43 and from_block2 + remaining > 43:
                                            # checking if entering safety zone
                                            to_block2 = (from_block2 + remaining) % 44 + 400
                                            # prove legal move
                                            if to_block1 == 35 and 35 <= from_block2 <= 39:
                                                # second piece will get knocked off on slide
                                                second_legal_move = False
                                            elif to_block2 == to_block1:
                                                if self.model.blue_safety[to_block2 - 400].is_home():
                                                    second_legal_move = True
                                                else:
                                                    second_legal_move = False
                                            elif self.model.blue_safety[to_block2 - 400].is_home():
                                                second_legal_move = True
                                            elif self.model.blue_safety[to_block2 - 400].is_occupied():
                                                second_legal_move = False
                                            elif not self.model.blue_safety[to_block2 - 400].is_occupied():
                                                second_legal_move = True
                                        elif 0 <= from_block2 <= 59 and 0 <= (from_block2 + remaining) % 60 <= 59:
                                            # checking if move is on mainboard
                                            to_block2 = (from_block2 + remaining) % 60
                                            # prove move is legal, check for sliding
                                            # first move was a slide:
                                            if to_block1 == 57:
                                                if 57 <= from_block2 <= 59 or from_block2 == 0:
                                                    # second piece knocked off by slide
                                                    second_legal_move = False
                                                elif to_block2 == 0:
                                                    # second piece lands on first piece after move
                                                    second_legal_move = False
                                                elif 57 <= to_block2 <= 59:
                                                    # second piece lands anywhere else on slide: legal
                                                    second_legal_move = True
                                                else:
                                                    # second piece lands elsewhere on the board
                                                    if to_block2 == from_block1:
                                                        second_legal_move = True
                                                    else:
                                                        # check legality
                                                        second_legal_move = self.check_legal_move(self.model.main_board, from_block2,
                                                            self.model.main_board, to_block2, 'blue')
                                            elif to_block1 == 5:
                                                if 5 <= from_block2 <= 9:
                                                    # second piece knocked off by slide
                                                    second_legal_move = False
                                                elif to_block2 == 9:
                                                    # second piece lands on first piece after move
                                                    second_legal_move = False
                                                elif 5 <= to_block2 <= 8:
                                                    # second piece lands anywhere else on slide: legal
                                                    second_legal_move = True
                                                else:
                                                    # second piece lands elsewhere on the board
                                                    if to_block2 == from_block1:
                                                        second_legal_move = True
                                                    else:
                                                        # check legality
                                                        second_legal_move = self.check_legal_move(self.model.main_board, from_block2,
                                                            self.model.main_board, to_block2, 'blue')
                                            elif to_block1 == 12:
                                                if 12 <= from_block2 <= 15:
                                                    # second piece knocked off by slide
                                                    second_legal_move = False
                                                elif to_block2 == 15:
                                                    # second piece lands on first piece after move
                                                    second_legal_move = False
                                                elif 12 <= to_block2 <= 14:
                                                    # second piece lands anywhere else on slide: legal
                                                    second_legal_move = True
                                                else:
                                                    # second piece lands elsewhere on the board
                                                    if to_block2 == from_block1:
                                                        second_legal_move = True
                                                    else:
                                                        # check legality
                                                        second_legal_move = self.check_legal_move(self.model.main_board, from_block2,
                                                            self.model.main_board, to_block2, 'blue')
                                            elif to_block1 == 20:
                                                if 20 <= from_block2 <= 24:
                                                    # second piece knocked off by slide
                                                    second_legal_move = False
                                                elif to_block2 == 24:
                                                    # second piece lands on first piece after move
                                                    second_legal_move = False
                                                elif 20 <= to_block2 <= 23:
                                                    # second piece lands anywhere else on slide: legal
                                                    second_legal_move = True
                                                else:
                                                    # second piece lands elsewhere on the board
                                                    if to_block2 == from_block1:
                                                        second_legal_move = True
                                                    else:
                                                        # check legality
                                                        second_legal_move = self.check_legal_move(self.model.main_board, from_block2,
                                                            self.model.main_board, to_block2, 'blue')
                                            elif to_block1 == 27:
                                                if 27 <= from_block2 <= 30:
                                                    # second piece knocked off by slide
                                                    second_legal_move = False
                                                elif to_block2 == 30:
                                                    # second piece lands on first piece after move
                                                    second_legal_move = False
                                                elif 27 <= to_block2 <= 29:
                                                    # second piece lands anywhere else on slide: legal
                                                    second_legal_move = True
                                                else:
                                                    # second piece lands elsewhere on the board
                                                    if to_block2 == from_block1:
                                                        second_legal_move = True
                                                    else:
                                                        # check legality
                                                        second_legal_move = self.check_legal_move(self.model.main_board, from_block2,
                                                            self.model.main_board, to_block2, 'blue')
                                            elif to_block1 == 35:
                                                if 35 <= from_block2 <= 39:
                                                    # second piece knocked off by slide
                                                    second_legal_move = False
                                                elif to_block2 == 39:
                                                    # second piece lands on first piece after move
                                                    second_legal_move = False
                                                elif 35 <= to_block2 <= 38:
                                                    # second piece lands anywhere else on slide: legal
                                                    second_legal_move = True
                                                else:
                                                    # second piece lands elsewhere on the board
                                                    if to_block2 == from_block1:
                                                        second_legal_move = True
                                                    else:
                                                        # check legality
                                                        second_legal_move = self.check_legal_move(self.model.main_board, from_block2,
                                                            self.model.main_board, to_block2, 'blue')
                                            else:
                                                # first move was not a slide
                                                if to_block1 == to_block2:
                                                    second_legal_move = False
                                                elif to_block2 == from_block1:
                                                    second_legal_move = True
                                                else:
                                                    second_legal_move = self.check_legal_move(self.model.main_board, from_block2,
                                                            self.model.main_board, to_block2, 'blue')
                    # check if both moves are legal to exit while loop
                    if first_legal_move and second_legal_move:
                        legal_moves = True
                # carry out legal moves
                from_list_model1, from_sq_model1 = self.get_list_and_square_from_model(from_block1)
                to_list_model1, to_sq_model1 = self.get_list_and_square_from_model(to_block1)
                from_list_view1, from_sq_view1 = self.get_list_and_square_from_view(from_block1)
                to_list_view1, to_sq_view1 = self.get_list_and_square_from_view(to_block1)
                
                self.model.move_piece(from_list_model1, from_sq_model1, to_list_model1,
                                          to_sq_model1)
                self.view.move_piece(from_list_view1, from_sq_view1, to_list_view1,
                                         to_sq_view1)
                if to_list_view1 is self.view.main_board:
                    self.check_slide(to_sq_view1, "blue")
                if to_list_model1 is self.model.blue_safety and to_sq_model1 == 5:
                    self.check_win('blue')
                self.display_all_starts()
                # carry out second legal move if necessary
                if remaining > 0:
                    from_list_model2, from_sq_model2 = self.get_list_and_square_from_model(from_block2)
                    to_list_model2, to_sq_model2 = self.get_list_and_square_from_model(to_block2)
                    from_list_view2, from_sq_view2 = self.get_list_and_square_from_view(from_block2)
                    to_list_view2, to_sq_view2 = self.get_list_and_square_from_view(to_block2)
                    
                    self.model.move_piece(from_list_model2, from_sq_model2, to_list_model2,
                                              to_sq_model2)
                    self.view.move_piece(from_list_view2, from_sq_view2, to_list_view2,
                                             to_sq_view2)
                    if to_list_view2 is self.view.main_board:
                        self.check_slide(to_sq_view2, "blue")
                    if to_list_model2 is self.model.blue_safety and to_sq_model2 == 5:
                        self.check_win('blue')
                    self.display_all_starts()
                # change player
                self.change_player()
            else:
                # no move exists: forfeit turn
                self.view.display_text("No move possible. Click draw pile \n to forfeit turn.")
                block = 1000
                while block != 500:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    block = self.view.get_block(x, y)
                self.change_player()

    def eight_card_player1(self):
        """
        Does: plays out 'eight card' scenario
        """
        self.view.display_text('Click on piece to move eight squares.')
        if self.player1.get_color() == 'yellow':
            if self.eight_card_move_exists('yellow'):
                # get click
                legal_move = False
                while legal_move == False:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    from_block = self.view.get_block(x, y)
                    # check if entering safety zone
                    if from_block <= 58 and from_block + 8 > 58:
                        to_block = (from_block + 8) % 59 + 100
                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                            self.model.yellow_safety, to_block - 100, 'yellow')
                    
                    # check if on main_board
                    elif 0 <= from_block <= 59:
                        to_block = (from_block + 8) % 60
                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                            self.model.main_board, to_block, 'yellow')
                    
                # carry out legal move
                from_list_model, from_sq_model = self.get_list_and_square_from_model(from_block)
                to_list_model, to_sq_model = self.get_list_and_square_from_model(to_block)
                from_list_view, from_sq_view = self.get_list_and_square_from_view(from_block)
                to_list_view, to_sq_view = self.get_list_and_square_from_view(to_block)
                
                self.model.move_piece(from_list_model, from_sq_model, to_list_model,
                                          to_sq_model)
                self.view.move_piece(from_list_view, from_sq_view, to_list_view,
                                         to_sq_view)
                if to_list_view is self.view.main_board:
                    self.check_slide(to_sq_view, "yellow")
                if to_list_model is self.model.yellow_safety and to_sq_model == 5:
                    self.check_win('yellow')
                self.display_all_starts()
                self.change_player()
                    
            else:
                # move doesn't exist: forfeit turn
                self.view.display_text("No move possible. Click draw pile \n to forfeit turn.")
                block = 1000
                while block != 500:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    block = self.view.get_block(x, y)
                self.change_player()
        elif self.player1.get_color() == 'green':
            if self.eight_card_move_exists('green'):
                # get click
                legal_move = False
                while legal_move == False:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    from_block = self.view.get_block(x, y)
                    # check if entering safety zone
                    if from_block <= 13 and from_block + 8 > 13:
                        to_block = (from_block + 8) % 14 + 200
                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                            self.model.green_safety, to_block - 200, 'green')
                    
                    # check if on main_board
                    elif 0 <= from_block <= 59:
                        to_block = (from_block + 8) % 60
                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                            self.model.main_board, to_block, 'green')
                    
                # carry out legal move
                from_list_model, from_sq_model = self.get_list_and_square_from_model(from_block)
                to_list_model, to_sq_model = self.get_list_and_square_from_model(to_block)
                from_list_view, from_sq_view = self.get_list_and_square_from_view(from_block)
                to_list_view, to_sq_view = self.get_list_and_square_from_view(to_block)
                
                self.model.move_piece(from_list_model, from_sq_model, to_list_model,
                                          to_sq_model)
                self.view.move_piece(from_list_view, from_sq_view, to_list_view,
                                         to_sq_view)
                if to_list_view is self.view.main_board:
                    self.check_slide(to_sq_view, "green")
                if to_list_model is self.model.green_safety and to_sq_model == 5:
                    self.check_win('green')
                self.display_all_starts()
                self.change_player()
                    
            else:
                # move doesn't exist: forfeit turn
                self.view.display_text("No move possible. Click draw pile \n to forfeit turn.")
                block = 1000
                while block != 500:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    block = self.view.get_block(x, y)
                self.change_player()
        elif self.player1.get_color() == 'red':
            if self.eight_card_move_exists('red'):
                # get click
                legal_move = False
                while legal_move == False:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    from_block = self.view.get_block(x, y)
                    # check if entering safety zone
                    if from_block <= 28 and from_block + 8 > 28:
                        to_block = (from_block + 8) % 29 + 300
                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                            self.model.red_safety, to_block - 300, 'red')
                    
                    # check if on main_board
                    elif 0 <= from_block <= 59:
                        to_block = (from_block + 8) % 60
                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                            self.model.main_board, to_block, 'red')
                    
                # carry out legal move
                from_list_model, from_sq_model = self.get_list_and_square_from_model(from_block)
                to_list_model, to_sq_model = self.get_list_and_square_from_model(to_block)
                from_list_view, from_sq_view = self.get_list_and_square_from_view(from_block)
                to_list_view, to_sq_view = self.get_list_and_square_from_view(to_block)
                
                self.model.move_piece(from_list_model, from_sq_model, to_list_model,
                                          to_sq_model)
                self.view.move_piece(from_list_view, from_sq_view, to_list_view,
                                         to_sq_view)
                if to_list_view is self.view.main_board:
                    self.check_slide(to_sq_view, "red")
                if to_list_model is self.model.red_safety and to_sq_model == 5:
                    self.check_win('red')
                self.display_all_starts()
                self.change_player()
                    
            else:
                # move doesn't exist: forfeit turn
                self.view.display_text("No move possible. Click draw pile \n to forfeit turn.")
                block = 1000
                while block != 500:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    block = self.view.get_block(x, y)
                self.change_player()
        elif self.player1.get_color() == 'blue':
            if self.eight_card_move_exists('blue'):
                # get click
                legal_move = False
                while legal_move == False:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    from_block = self.view.get_block(x, y)
                    # check if entering safety zone
                    if from_block <= 43 and from_block + 8 > 43:
                        to_block = (from_block + 8) % 44 + 400
                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                            self.model.blue_safety, to_block - 400, 'blue')
                    
                    # check if on main_board
                    elif 0 <= from_block <= 59:
                        to_block = (from_block + 8) % 60
                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                            self.model.main_board, to_block, 'blue')
                    
                # carry out legal move
                from_list_model, from_sq_model = self.get_list_and_square_from_model(from_block)
                to_list_model, to_sq_model = self.get_list_and_square_from_model(to_block)
                from_list_view, from_sq_view = self.get_list_and_square_from_view(from_block)
                to_list_view, to_sq_view = self.get_list_and_square_from_view(to_block)
                
                self.model.move_piece(from_list_model, from_sq_model, to_list_model,
                                          to_sq_model)
                self.view.move_piece(from_list_view, from_sq_view, to_list_view,
                                         to_sq_view)
                if to_list_view is self.view.main_board:
                    self.check_slide(to_sq_view, "blue")
                if to_list_model is self.model.blue_safety and to_sq_model == 5:
                    self.check_win('blue')
                self.display_all_starts()
                self.change_player()
                    
            else:
                # move doesn't exist: forfeit turn
                self.view.display_text("No move possible. Click draw pile \n to forfeit turn.")
                block = 1000
                while block != 500:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    block = self.view.get_block(x, y)
                self.change_player()

    def ten_card_player1(self):
        """
        Does: plays out 'ten card' scenario
        """
        if self.player1.get_color() == 'yellow':
            if self.ten_card_move_exists('yellow'):
                legal_move = False
                while legal_move == False:
                    self.view.display_text('Move a piece forward ten spaces \n or backward 1 space. \n' +
                                           'Click on piece you want to move.')
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    from_block = self.view.get_block(x, y)
                    if 0 <= from_block <= 59 or 100 <= from_block <= 104:
                        # check that from_block has color
                        from_list_model, from_sq_model = self.get_list_and_square_from_model(from_block)
                        if from_list_model[from_sq_model].is_occupied():
                            if from_list_model[from_sq_model].get_color() == 'yellow':
                                self.view.display_text('Click on adjacent square \n in the direction you want to \n' +
                                                       'move. Forward for 10, backward for 1.')
                                click_point = self.view.win.getMouse()
                                x = click_point.getX()
                                y = click_point.getY()
                                direction_block = self.view.get_block(x, y)
                                # direction block must be +1 or -1
                                if 0 <= from_block <= 59:
                                    if direction_block == (from_block + 1) % 60:
                                        forward = True
                                        # check legal move forward +10
                                        if from_block <= 58 and from_block + 10 > 58:
                                            # moves into safety zone
                                            to_block = (from_block + 10) % 59 + 100
                                            legal_move = self.check_legal_move(self.model.main_board, from_block,
                                                        self.model.yellow_safety, to_block - 100, 'yellow')
                                        else:
                                            # check main_board
                                            to_block = (from_block + 10) % 60
                                            legal_move = self.check_legal_move(self.model.main_board, from_block,
                                                        self.model.main_board, to_block, 'yellow')
                                    elif direction_block == (from_block + 60 - 1) % 60:
                                        # check legal move backward -1
                                        forward = False
                                        to_block = direction_block
                                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                                        self.model.main_board, to_block, 'yellow')
                                    else:
                                        nothing = True
                                elif 100 <= from_block <= 104:
                                    # direction block must be -1
                                    if from_block == 100:
                                        if direction_block == 58:
                                            forward = False
                                            to_block = direction_block
                                            legal_move = self.check_legal_move(self.model.yellow_safety,
                                                        from_block - 100, self.model.main_board, to_block, 'yellow')
                                    else:
                                        if direction_block == from_block - 1:
                                            forward = False
                                            to_block = direction_block
                                            legal_move = self.check_legal_move(self.model.yellow_safety,
                                                        from_block - 100, self.model.yellow_safety, to_block - 100,
                                                        'yellow')
                # carry out legal move
                to_list_model, to_sq_model = self.get_list_and_square_from_model(to_block)
                from_list_view, from_sq_view = self.get_list_and_square_from_view(from_block)
                to_list_view, to_sq_view = self.get_list_and_square_from_view(to_block)
                
                self.model.move_piece(from_list_model, from_sq_model, to_list_model,
                                          to_sq_model)
                self.view.move_piece(from_list_view, from_sq_view, to_list_view,
                                         to_sq_view, forward)
                if to_list_view is self.view.main_board:
                    self.check_slide(to_sq_view, "yellow")
                if to_list_model is self.model.yellow_safety and to_sq_model == 5:
                    self.check_win('yellow')
                self.display_all_starts()
                self.change_player()
            else:
                # move doesn't exist: forfeit turn
                self.view.display_text("No move possible. Click draw pile \n to forfeit turn.")
                block = 1000
                while block != 500:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    block = self.view.get_block(x, y)
                self.change_player()
        elif self.player1.get_color() == 'green':
            if self.ten_card_move_exists('green'):
                legal_move = False
                while legal_move == False:
                    self.view.display_text('Move a piece forward ten spaces \n or backward 1 space. \n' +
                                           'Click on piece you want to move.')
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    from_block = self.view.get_block(x, y)
                    if 0 <= from_block <= 59 or 200 <= from_block <= 204:
                        # check that from_block has color
                        from_list_model, from_sq_model = self.get_list_and_square_from_model(from_block)
                        if from_list_model[from_sq_model].is_occupied():
                            if from_list_model[from_sq_model].get_color() == 'green':
                                self.view.display_text('Click on adjacent square \n in the direction you want to \n' +
                                                       'move. Forward for 10, backward for 1.')
                                click_point = self.view.win.getMouse()
                                x = click_point.getX()
                                y = click_point.getY()
                                direction_block = self.view.get_block(x, y)
                                # direction block must be +1 or -1
                                if 0 <= from_block <= 59:
                                    if direction_block == (from_block + 1) % 60:
                                        forward = True
                                        # check legal move forward +10
                                        if from_block <= 13 and from_block + 10 > 13:
                                            # moves into safety zone
                                            to_block = (from_block + 10) % 14 + 200
                                            legal_move = self.check_legal_move(self.model.main_board, from_block,
                                                        self.model.green_safety, to_block - 200, 'green')
                                        else:
                                            # check main_board
                                            to_block = (from_block + 10) % 60
                                            legal_move = self.check_legal_move(self.model.main_board, from_block,
                                                        self.model.main_board, to_block, 'green')
                                    elif direction_block == (from_block + 60 - 1) % 60:
                                        # check legal move backward -1
                                        forward = False
                                        to_block = direction_block
                                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                                        self.model.main_board, to_block, 'green')
                                    else:
                                        nothing = True
                                elif 200 <= from_block <= 204:
                                    # direction block must be -1
                                    if from_block == 200:
                                        if direction_block == 13:
                                            forward = False
                                            to_block = direction_block
                                            legal_move = self.check_legal_move(self.model.green_safety,
                                                        from_block - 200, self.model.main_board, to_block, 'green')
                                    else:
                                        if direction_block == from_block - 1:
                                            forward = False
                                            to_block = direction_block
                                            legal_move = self.check_legal_move(self.model.green_safety,
                                                        from_block - 200, self.model.green_safety, to_block - 200,
                                                        'green')
                # carry out legal move
                to_list_model, to_sq_model = self.get_list_and_square_from_model(to_block)
                from_list_view, from_sq_view = self.get_list_and_square_from_view(from_block)
                to_list_view, to_sq_view = self.get_list_and_square_from_view(to_block)
                
                self.model.move_piece(from_list_model, from_sq_model, to_list_model,
                                          to_sq_model)
                self.view.move_piece(from_list_view, from_sq_view, to_list_view,
                                         to_sq_view, forward)
                if to_list_view is self.view.main_board:
                    self.check_slide(to_sq_view, "green")
                if to_list_model is self.model.green_safety and to_sq_model == 5:
                    self.check_win('green')
                self.display_all_starts()
                self.change_player()
            else:
                # move doesn't exist: forfeit turn
                self.view.display_text("No move possible. Click draw pile \n to forfeit turn.")
                block = 1000
                while block != 500:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    block = self.view.get_block(x, y)
                self.change_player()
        elif self.player1.get_color() == 'red':
            if self.ten_card_move_exists('red'):
                legal_move = False
                while legal_move == False:
                    self.view.display_text('Move a piece forward ten spaces \n or backward 1 space. \n' +
                                           'Click on piece you want to move.')
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    from_block = self.view.get_block(x, y)
                    if 0 <= from_block <= 59 or 300 <= from_block <= 304:
                        # check that from_block has color
                        from_list_model, from_sq_model = self.get_list_and_square_from_model(from_block)
                        if from_list_model[from_sq_model].is_occupied():
                            if from_list_model[from_sq_model].get_color() == 'red':
                                self.view.display_text('Click on adjacent square \n in the direction you want to \n' +
                                                       'move. Forward for 10, backward for 1.')
                                click_point = self.view.win.getMouse()
                                x = click_point.getX()
                                y = click_point.getY()
                                direction_block = self.view.get_block(x, y)
                                # direction block must be +1 or -1
                                if 0 <= from_block <= 59:
                                    if direction_block == (from_block + 1) % 60:
                                        forward = True
                                        # check legal move forward +10
                                        if from_block <= 28 and from_block + 10 > 28:
                                            # moves into safety zone
                                            to_block = (from_block + 10) % 29 + 300
                                            legal_move = self.check_legal_move(self.model.main_board, from_block,
                                                        self.model.red_safety, to_block - 300, 'red')
                                        else:
                                            # check main_board
                                            to_block = (from_block + 10) % 60
                                            legal_move = self.check_legal_move(self.model.main_board, from_block,
                                                        self.model.main_board, to_block, 'red')
                                    elif direction_block == (from_block + 60 - 1) % 60:
                                        # check legal move backward -1
                                        forward = False
                                        to_block = direction_block
                                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                                        self.model.main_board, to_block, 'red')
                                    else:
                                        nothing = True
                                elif 300 <= from_block <= 304:
                                    # direction block must be -1
                                    if from_block == 300:
                                        if direction_block == 28:
                                            forward = False
                                            to_block = direction_block
                                            legal_move = self.check_legal_move(self.model.red_safety,
                                                        from_block - 300, self.model.main_board, to_block, 'red')
                                    else:
                                        if direction_block == from_block - 1:
                                            forward = False
                                            to_block = direction_block
                                            legal_move = self.check_legal_move(self.model.red_safety,
                                                        from_block - 300, self.model.red_safety, to_block - 300,
                                                        'red')
                # carry out legal move
                to_list_model, to_sq_model = self.get_list_and_square_from_model(to_block)
                from_list_view, from_sq_view = self.get_list_and_square_from_view(from_block)
                to_list_view, to_sq_view = self.get_list_and_square_from_view(to_block)
                
                self.model.move_piece(from_list_model, from_sq_model, to_list_model,
                                          to_sq_model)
                self.view.move_piece(from_list_view, from_sq_view, to_list_view,
                                         to_sq_view, forward)
                if to_list_view is self.view.main_board:
                    self.check_slide(to_sq_view, "red")
                if to_list_model is self.model.red_safety and to_sq_model == 5:
                    self.check_win('red')
                self.display_all_starts()
                self.change_player()
            else:
                # move doesn't exist: forfeit turn
                self.view.display_text("No move possible. Click draw pile \n to forfeit turn.")
                block = 1000
                while block != 500:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    block = self.view.get_block(x, y)
                self.change_player()
        elif self.player1.get_color() == 'blue':
            if self.ten_card_move_exists('blue'):
                legal_move = False
                while legal_move == False:
                    self.view.display_text('Move a piece forward ten spaces \n or backward 1 space. \n' +
                                           'Click on piece you want to move.')
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    from_block = self.view.get_block(x, y)
                    if 0 <= from_block <= 59 or 400 <= from_block <= 404:
                        # check that from_block has color
                        from_list_model, from_sq_model = self.get_list_and_square_from_model(from_block)
                        if from_list_model[from_sq_model].is_occupied():
                            if from_list_model[from_sq_model].get_color() == 'blue':
                                self.view.display_text('Click on adjacent square \n in the direction you want to \n' +
                                                       'move. Forward for 10, backward for 1.')
                                click_point = self.view.win.getMouse()
                                x = click_point.getX()
                                y = click_point.getY()
                                direction_block = self.view.get_block(x, y)
                                # direction block must be +1 or -1
                                if 0 <= from_block <= 59:
                                    if direction_block == (from_block + 1) % 60:
                                        forward = True
                                        # check legal move forward +10
                                        if from_block <= 43 and from_block + 10 > 43:
                                            # moves into safety zone
                                            to_block = (from_block + 10) % 44 + 400
                                            legal_move = self.check_legal_move(self.model.main_board, from_block,
                                                        self.model.blue_safety, to_block - 400, 'blue')
                                        else:
                                            # check main_board
                                            to_block = (from_block + 10) % 60
                                            legal_move = self.check_legal_move(self.model.main_board, from_block,
                                                        self.model.main_board, to_block, 'blue')
                                    elif direction_block == (from_block + 60 - 1) % 60:
                                        # check legal move backward -1
                                        forward = False
                                        to_block = direction_block
                                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                                        self.model.main_board, to_block, 'blue')
                                    else:
                                        nothing = True
                                elif 400 <= from_block <= 404:
                                    # direction block must be -1
                                    if from_block == 400:
                                        if direction_block == 43:
                                            forward = False
                                            to_block = direction_block
                                            legal_move = self.check_legal_move(self.model.blue_safety,
                                                        from_block - 400, self.model.main_board, to_block, 'blue')
                                    else:
                                        if direction_block == from_block - 1:
                                            forward = False
                                            to_block = direction_block
                                            legal_move = self.check_legal_move(self.model.blue_safety,
                                                        from_block - 400, self.model.blue_safety, to_block - 400,
                                                        'blue')
                # carry out legal move
                to_list_model, to_sq_model = self.get_list_and_square_from_model(to_block)
                from_list_view, from_sq_view = self.get_list_and_square_from_view(from_block)
                to_list_view, to_sq_view = self.get_list_and_square_from_view(to_block)
                
                self.model.move_piece(from_list_model, from_sq_model, to_list_model,
                                          to_sq_model)
                self.view.move_piece(from_list_view, from_sq_view, to_list_view,
                                         to_sq_view, forward)
                if to_list_view is self.view.main_board:
                    self.check_slide(to_sq_view, "blue")
                if to_list_model is self.model.blue_safety and to_sq_model == 5:
                    self.check_win('blue')
                self.display_all_starts()
                self.change_player()
            else:
                # move doesn't exist: forfeit turn
                self.view.display_text("No move possible. Click draw pile \n to forfeit turn.")
                block = 1000
                while block != 500:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    block = self.view.get_block(x, y)
                self.change_player()

    def eleven_forward_exists(self, color):
        """
        Does: helper function. Determines if moving forward 11 is possible
        Returns: True if move is possible, False if not
        """
        if color == 'yellow':
            # check if all pieces are in start
            if self.model.yellow_start:
                if len(self.model.yellow_start) == 4:
                    return False
            # check for forward move of 11
            for i in range(60):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        if i <= 58 and i + 11 > 58:
                            # check safety zone
                            if self.model.yellow_safety[(i + 11) % 59].is_valid():
                                if self.model.yellow_safety[(i + 11) % 59].is_home():
                                    return True
                                else:
                                    # regular space
                                    if not self.model.yellow_safety[(i + 11) % 59].is_occupied():
                                        return True
                        else:
                            # check main_board
                            if self.model.main_board[(i + 11) % 60].is_occupied():
                                if self.model.main_board[(i + 11) % 60].get_color() != color:
                                    return True
                            else:
                                # from square + 11 is unoccupied
                                return True
            return False
        elif color == 'green':
            # check if all pieces are in start
            if self.model.green_start:
                if len(self.model.green_start) == 4:
                    return False
            # check for forward move of 11
            for i in range(60):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        if i <= 13 and i + 11 > 13:
                            # check safety zone
                            if self.model.green_safety[(i + 11) % 14].is_valid():
                                if self.model.green_safety[(i + 11) % 14].is_home():
                                    return True
                                else:
                                    # regular space
                                    if not self.model.green_safety[(i + 11) % 14].is_occupied():
                                        return True
                        else:
                            # check main_board
                            if self.model.main_board[(i + 11) % 60].is_occupied():
                                if self.model.main_board[(i + 11) % 60].get_color() != color:
                                    return True
                            else:
                                # from square + 11 is unoccupied
                                return True
            return False
        elif color == 'red':
            # check if all pieces are in start
            if self.model.red_start:
                if len(self.model.red_start) == 4:
                    return False
            # check for forward move of 11
            for i in range(60):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        if i <= 28 and i + 11 > 28:
                            # check safety zone
                            if self.model.red_safety[(i + 11) % 29].is_valid():
                                if self.model.red_safety[(i + 11) % 29].is_home():
                                    return True
                                else:
                                    # regular space
                                    if not self.model.red_safety[(i + 11) % 29].is_occupied():
                                        return True
                        else:
                            # check main_board
                            if self.model.main_board[(i + 11) % 60].is_occupied():
                                if self.model.main_board[(i + 11) % 60].get_color() != color:
                                    return True
                            else:
                                # from square + 11 is unoccupied
                                return True
            return False
        elif color == 'blue':
            # check if all pieces are in start
            if self.model.blue_start:
                if len(self.model.blue_start) == 4:
                    return False
            # check for forward move of 11
            for i in range(60):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        if i <= 43 and i + 11 > 43:
                            # check safety zone
                            if self.model.blue_safety[(i + 11) % 44].is_valid():
                                if self.model.blue_safety[(i + 11) % 44].is_home():
                                    return True
                                else:
                                    # regular space
                                    if not self.model.blue_safety[(i + 11) % 44].is_occupied():
                                        return True
                        else:
                            # check main_board
                            if self.model.main_board[(i + 11) % 60].is_occupied():
                                if self.model.main_board[(i + 11) % 60].get_color() != color:
                                    return True
                            else:
                                # from square + 11 is unoccupied
                                return True
            return False
        

    def eleven_card_player1(self):
        """
        Does: plays out 'eleven card' scenario, uses helper method eleven_forward_exists
        """
        if self.player1.get_color() == 'yellow':
            if self.eleven_card_move_exists('yellow'):
                if self.eleven_forward_exists('yellow'):
                    # must move forward 11 or trade pieces
                    legal_move = False
                    while legal_move == False:
                        self.view.display_text("Click on one of your pieces \n to move 11 or trade.")
                        # get first click
                        click_point = self.view.win.getMouse()
                        x = click_point.getX()
                        y = click_point.getY()
                        from_block = self.view.get_block(x, y)
                        if 0 <= from_block <= 59:
                            if self.model.main_board[from_block].is_occupied():
                                if self.model.main_board[from_block].get_color() == 'yellow':
                                    # get click for move of 11 or trade pieces
                                    self.view.display_text("Click on piece again to move 11 \n" +
                                                           "or click on opposing piece \n to trade places.")
                                    # get second click
                                    click_point = self.view.win.getMouse()
                                    x = click_point.getX()
                                    y = click_point.getY()
                                    second_block = self.view.get_block(x, y)
                                    if second_block == from_block:
                                        # attempt move forward 11
                                        # check if entering safety zone
                                        if from_block <= 58 and from_block + 11 > 58:
                                            to_block = (from_block + 11) % 59 + 100
                                            legal_move = self.check_legal_move(self.model.main_board, from_block,
                                                self.model.yellow_safety, to_block - 100, 'yellow')
                                            if legal_move:
                                                # carry out legal move
                                                from_list_model, from_sq_model = self.get_list_and_square_from_model(from_block)
                                                to_list_model, to_sq_model = self.get_list_and_square_from_model(to_block)
                                                from_list_view, from_sq_view = self.get_list_and_square_from_view(from_block)
                                                to_list_view, to_sq_view = self.get_list_and_square_from_view(to_block)
                                                
                                                self.model.move_piece(from_list_model, from_sq_model, to_list_model,
                                                                          to_sq_model)
                                                self.view.move_piece(from_list_view, from_sq_view, to_list_view,
                                                                         to_sq_view)
                                                if to_list_view is self.view.main_board:
                                                    self.check_slide(to_sq_view, "yellow")
                                                if to_list_model is self.model.yellow_safety and to_sq_model == 5:
                                                    self.check_win('yellow')
                                                self.display_all_starts()
                                                self.change_player()
                                        else:
                                            # main board move of 11
                                            to_block = (from_block + 11) % 60
                                            legal_move = self.check_legal_move(self.model.main_board, from_block,
                                                self.model.main_board, to_block, 'yellow')
                                            if legal_move:
                                                # carry out legal move
                                                from_list_model, from_sq_model = self.get_list_and_square_from_model(from_block)
                                                to_list_model, to_sq_model = self.get_list_and_square_from_model(to_block)
                                                from_list_view, from_sq_view = self.get_list_and_square_from_view(from_block)
                                                to_list_view, to_sq_view = self.get_list_and_square_from_view(to_block)
                                                
                                                self.model.move_piece(from_list_model, from_sq_model, to_list_model,
                                                                          to_sq_model)
                                                self.view.move_piece(from_list_view, from_sq_view, to_list_view,
                                                                         to_sq_view)
                                                if to_list_view is self.view.main_board:
                                                    self.check_slide(to_sq_view, "yellow")
                                                if to_list_model is self.model.yellow_safety and to_sq_model == 5:
                                                    self.check_win('yellow')
                                                self.display_all_starts()
                                                self.change_player()
                                    else:
                                        # trade pieces if legal move
                                        to_block = second_block
                                        if 0 <= to_block <= 59:
                                            if self.model.main_board[to_block].is_occupied():
                                                if self.model.main_board[to_block].get_color() != 'yellow':
                                                    op_piece_color = self.model.main_board[to_block].get_color()
                                                    legal_move = True
                                                    # carry out legal move
                                                    self.model.trade_pieces(from_block, to_block)
                                                    self.view.trade_pieces(from_block, to_block)
                                                    self.check_slide(to_block, 'yellow')
                                                    self.check_slide(from_block, op_piece_color)
                                                    self.display_all_starts()
                                                    self.change_player()
                        
                else:
                    # click to trade pieces or click draw pile to forfeit
                    legal_move = False
                    while legal_move == False:
                        self.view.display_text("Click on one of your pieces \n to trade or click draw pile \n to forfeit turn.")
                        # get first click
                        click_point = self.view.win.getMouse()
                        x = click_point.getX()
                        y = click_point.getY()
                        from_block = self.view.get_block(x, y)
                        if from_block == 500:
                            # forfeit turn
                            self.change_player()
                            legal_move = True
                        elif 0 <= from_block <= 59:
                            if self.model.main_board[from_block].is_occupied():
                                if self.model.main_board[from_block].get_color() == 'yellow':
                                    # get second click
                                    self.view.display_text("Click on opposing piece to trade.")
                                    click_point = self.view.win.getMouse()
                                    x = click_point.getX()
                                    y = click_point.getY()
                                    to_block = self.view.get_block(x, y)
                                    if 0 <= to_block <= 59:
                                        if self.model.main_board[to_block].is_occupied():
                                            if self.model.main_board[to_block].get_color() != 'yellow':
                                                # trade pieces
                                                op_piece_color = self.model.main_board[to_block].get_color()
                                                legal_move = True
                                                self.model.trade_pieces(from_block, to_block)
                                                self.view.trade_pieces(from_block, to_block)
                                                self.check_slide(to_block, 'yellow')
                                                self.check_slide(from_block, op_piece_color)
                                                self.display_all_starts()
                                                self.change_player()
                    
            else:
                # no move exists: forfeit turn
                self.view.display_text("No move possible. Click draw pile \n to forfeit turn.")
                block = 1000
                while block != 500:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    block = self.view.get_block(x, y)
                self.change_player()
        elif self.player1.get_color() == 'green':
            if self.eleven_card_move_exists('green'):
                if self.eleven_forward_exists('green'):
                    # must move forward 11 or trade pieces
                    legal_move = False
                    while legal_move == False:
                        self.view.display_text("Click on one of your pieces \n to move 11 or trade.")
                        # get first click
                        click_point = self.view.win.getMouse()
                        x = click_point.getX()
                        y = click_point.getY()
                        from_block = self.view.get_block(x, y)
                        if 0 <= from_block <= 59:
                            if self.model.main_board[from_block].is_occupied():
                                if self.model.main_board[from_block].get_color() == 'green':
                                    # get click for move of 11 or trade pieces
                                    self.view.display_text("Click on piece again to move 11 \n" +
                                                           "or click on opposing piece \n to trade places.")
                                    # get second click
                                    click_point = self.view.win.getMouse()
                                    x = click_point.getX()
                                    y = click_point.getY()
                                    second_block = self.view.get_block(x, y)
                                    if second_block == from_block:
                                        # attempt move forward 11
                                        # check if entering safety zone
                                        if from_block <= 13 and from_block + 11 > 13:
                                            to_block = (from_block + 11) % 14 + 200
                                            legal_move = self.check_legal_move(self.model.main_board, from_block,
                                                self.model.green_safety, to_block - 200, 'green')
                                            if legal_move:
                                                # carry out legal move
                                                from_list_model, from_sq_model = self.get_list_and_square_from_model(from_block)
                                                to_list_model, to_sq_model = self.get_list_and_square_from_model(to_block)
                                                from_list_view, from_sq_view = self.get_list_and_square_from_view(from_block)
                                                to_list_view, to_sq_view = self.get_list_and_square_from_view(to_block)
                                                
                                                self.model.move_piece(from_list_model, from_sq_model, to_list_model,
                                                                          to_sq_model)
                                                self.view.move_piece(from_list_view, from_sq_view, to_list_view,
                                                                         to_sq_view)
                                                if to_list_view is self.view.main_board:
                                                    self.check_slide(to_sq_view, "green")
                                                if to_list_model is self.model.green_safety and to_sq_model == 5:
                                                    self.check_win('green')
                                                self.display_all_starts()
                                                self.change_player()
                                        else:
                                            # main board move of 11
                                            to_block = (from_block + 11) % 60
                                            legal_move = self.check_legal_move(self.model.main_board, from_block,
                                                self.model.main_board, to_block, 'green')
                                            if legal_move:
                                                # carry out legal move
                                                from_list_model, from_sq_model = self.get_list_and_square_from_model(from_block)
                                                to_list_model, to_sq_model = self.get_list_and_square_from_model(to_block)
                                                from_list_view, from_sq_view = self.get_list_and_square_from_view(from_block)
                                                to_list_view, to_sq_view = self.get_list_and_square_from_view(to_block)
                                                
                                                self.model.move_piece(from_list_model, from_sq_model, to_list_model,
                                                                          to_sq_model)
                                                self.view.move_piece(from_list_view, from_sq_view, to_list_view,
                                                                         to_sq_view)
                                                if to_list_view is self.view.main_board:
                                                    self.check_slide(to_sq_view, "green")
                                                if to_list_model is self.model.green_safety and to_sq_model == 5:
                                                    self.check_win('green')
                                                self.display_all_starts()
                                                self.change_player()
                                    else:
                                        # trade pieces if legal move
                                        to_block = second_block
                                        if 0 <= to_block <= 59:
                                            if self.model.main_board[to_block].is_occupied():
                                                if self.model.main_board[to_block].get_color() != 'green':
                                                    op_piece_color = self.model.main_board[to_block].get_color()
                                                    legal_move = True
                                                    # carry out legal move
                                                    self.model.trade_pieces(from_block, to_block)
                                                    self.view.trade_pieces(from_block, to_block)
                                                    self.check_slide(to_block, 'green')
                                                    self.check_slide(from_block, op_piece_color)
                                                    self.display_all_starts()
                                                    self.change_player()
                        
                else:
                    # click to trade pieces or click draw pile to forfeit
                    legal_move = False
                    while legal_move == False:
                        self.view.display_text("Click on one of your pieces \n to trade or click draw pile \n to forfeit turn.")
                        # get first click
                        click_point = self.view.win.getMouse()
                        x = click_point.getX()
                        y = click_point.getY()
                        from_block = self.view.get_block(x, y)
                        if from_block == 500:
                            # forfeit turn
                            self.change_player()
                            legal_move = True
                        elif 0 <= from_block <= 59:
                            if self.model.main_board[from_block].is_occupied():
                                if self.model.main_board[from_block].get_color() == 'green':
                                    # get second click
                                    self.view.display_text("Click on opposing piece to trade.")
                                    click_point = self.view.win.getMouse()
                                    x = click_point.getX()
                                    y = click_point.getY()
                                    to_block = self.view.get_block(x, y)
                                    if 0 <= to_block <= 59:
                                        if self.model.main_board[to_block].is_occupied():
                                            if self.model.main_board[to_block].get_color() != 'green':
                                                # trade pieces
                                                op_piece_color = self.model.main_board[to_block].get_color()
                                                legal_move = True
                                                self.model.trade_pieces(from_block, to_block)
                                                self.view.trade_pieces(from_block, to_block)
                                                self.check_slide(to_block, 'green')
                                                self.check_slide(from_block, op_piece_color)
                                                self.display_all_starts()
                                                self.change_player()
                    
            else:
                # no move exists: forfeit turn
                self.view.display_text("No move possible. Click draw pile \n to forfeit turn.")
                block = 1000
                while block != 500:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    block = self.view.get_block(x, y)
                self.change_player()
        elif self.player1.get_color() == 'red':
            if self.eleven_card_move_exists('red'):
                if self.eleven_forward_exists('red'):
                    # must move forward 11 or trade pieces
                    legal_move = False
                    while legal_move == False:
                        self.view.display_text("Click on one of your pieces \n to move 11 or trade.")
                        # get first click
                        click_point = self.view.win.getMouse()
                        x = click_point.getX()
                        y = click_point.getY()
                        from_block = self.view.get_block(x, y)
                        if 0 <= from_block <= 59:
                            if self.model.main_board[from_block].is_occupied():
                                if self.model.main_board[from_block].get_color() == 'red':
                                    # get click for move of 11 or trade pieces
                                    self.view.display_text("Click on piece again to move 11 \n" +
                                                           "or click on opposing piece \n to trade places.")
                                    # get second click
                                    click_point = self.view.win.getMouse()
                                    x = click_point.getX()
                                    y = click_point.getY()
                                    second_block = self.view.get_block(x, y)
                                    if second_block == from_block:
                                        # attempt move forward 11
                                        # check if entering safety zone
                                        if from_block <= 28 and from_block + 11 > 28:
                                            to_block = (from_block + 11) % 29 + 300
                                            legal_move = self.check_legal_move(self.model.main_board, from_block,
                                                self.model.red_safety, to_block - 300, 'red')
                                            if legal_move:
                                                # carry out legal move
                                                from_list_model, from_sq_model = self.get_list_and_square_from_model(from_block)
                                                to_list_model, to_sq_model = self.get_list_and_square_from_model(to_block)
                                                from_list_view, from_sq_view = self.get_list_and_square_from_view(from_block)
                                                to_list_view, to_sq_view = self.get_list_and_square_from_view(to_block)
                                                
                                                self.model.move_piece(from_list_model, from_sq_model, to_list_model,
                                                                          to_sq_model)
                                                self.view.move_piece(from_list_view, from_sq_view, to_list_view,
                                                                         to_sq_view)
                                                if to_list_view is self.view.main_board:
                                                    self.check_slide(to_sq_view, "red")
                                                if to_list_model is self.model.red_safety and to_sq_model == 5:
                                                    self.check_win('red')
                                                self.display_all_starts()
                                                self.change_player()
                                        else:
                                            # main board move of 11
                                            to_block = (from_block + 11) % 60
                                            legal_move = self.check_legal_move(self.model.main_board, from_block,
                                                self.model.main_board, to_block, 'red')
                                            if legal_move:
                                                # carry out legal move
                                                from_list_model, from_sq_model = self.get_list_and_square_from_model(from_block)
                                                to_list_model, to_sq_model = self.get_list_and_square_from_model(to_block)
                                                from_list_view, from_sq_view = self.get_list_and_square_from_view(from_block)
                                                to_list_view, to_sq_view = self.get_list_and_square_from_view(to_block)
                                                
                                                self.model.move_piece(from_list_model, from_sq_model, to_list_model,
                                                                          to_sq_model)
                                                self.view.move_piece(from_list_view, from_sq_view, to_list_view,
                                                                         to_sq_view)
                                                if to_list_view is self.view.main_board:
                                                    self.check_slide(to_sq_view, "red")
                                                if to_list_model is self.model.red_safety and to_sq_model == 5:
                                                    self.check_win('red')
                                                self.display_all_starts()
                                                self.change_player()
                                    else:
                                        # trade pieces if legal move
                                        to_block = second_block
                                        if 0 <= to_block <= 59:
                                            if self.model.main_board[to_block].is_occupied():
                                                if self.model.main_board[to_block].get_color() != 'red':
                                                    op_piece_color = self.model.main_board[to_block].get_color()
                                                    legal_move = True
                                                    # carry out legal move
                                                    self.model.trade_pieces(from_block, to_block)
                                                    self.view.trade_pieces(from_block, to_block)
                                                    self.check_slide(to_block, 'red')
                                                    self.check_slide(from_block, op_piece_color)
                                                    self.display_all_starts()
                                                    self.change_player()
                        
                else:
                    # click to trade pieces or click draw pile to forfeit
                    legal_move = False
                    while legal_move == False:
                        self.view.display_text("Click on one of your pieces \n to trade or click draw pile \n to forfeit turn.")
                        # get first click
                        click_point = self.view.win.getMouse()
                        x = click_point.getX()
                        y = click_point.getY()
                        from_block = self.view.get_block(x, y)
                        if from_block == 500:
                            # forfeit turn
                            self.change_player()
                            legal_move = True
                        elif 0 <= from_block <= 59:
                            if self.model.main_board[from_block].is_occupied():
                                if self.model.main_board[from_block].get_color() == 'red':
                                    # get second click
                                    self.view.display_text("Click on opposing piece to trade.")
                                    click_point = self.view.win.getMouse()
                                    x = click_point.getX()
                                    y = click_point.getY()
                                    to_block = self.view.get_block(x, y)
                                    if 0 <= to_block <= 59:
                                        if self.model.main_board[to_block].is_occupied():
                                            if self.model.main_board[to_block].get_color() != 'red':
                                                # trade pieces
                                                op_piece_color = self.model.main_board[to_block].get_color()
                                                legal_move = True
                                                self.model.trade_pieces(from_block, to_block)
                                                self.view.trade_pieces(from_block, to_block)
                                                self.check_slide(to_block, 'red')
                                                self.check_slide(from_block, op_piece_color)
                                                self.display_all_starts()
                                                self.change_player()
                    
            else:
                # no move exists: forfeit turn
                self.view.display_text("No move possible. Click draw pile \n to forfeit turn.")
                block = 1000
                while block != 500:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    block = self.view.get_block(x, y)
                self.change_player()
        elif self.player1.get_color() == 'blue':
            if self.eleven_card_move_exists('blue'):
                if self.eleven_forward_exists('blue'):
                    # must move forward 11 or trade pieces
                    legal_move = False
                    while legal_move == False:
                        self.view.display_text("Click on one of your pieces \n to move 11 or trade.")
                        # get first click
                        click_point = self.view.win.getMouse()
                        x = click_point.getX()
                        y = click_point.getY()
                        from_block = self.view.get_block(x, y)
                        if 0 <= from_block <= 59:
                            if self.model.main_board[from_block].is_occupied():
                                if self.model.main_board[from_block].get_color() == 'blue':
                                    # get click for move of 11 or trade pieces
                                    self.view.display_text("Click on piece again to move 11 \n" +
                                                           "or click on opposing piece \n to trade places.")
                                    # get second click
                                    click_point = self.view.win.getMouse()
                                    x = click_point.getX()
                                    y = click_point.getY()
                                    second_block = self.view.get_block(x, y)
                                    if second_block == from_block:
                                        # attempt move forward 11
                                        # check if entering safety zone
                                        if from_block <= 43 and from_block + 11 > 43:
                                            to_block = (from_block + 11) % 44 + 400
                                            legal_move = self.check_legal_move(self.model.main_board, from_block,
                                                self.model.blue_safety, to_block - 400, 'blue')
                                            if legal_move:
                                                # carry out legal move
                                                from_list_model, from_sq_model = self.get_list_and_square_from_model(from_block)
                                                to_list_model, to_sq_model = self.get_list_and_square_from_model(to_block)
                                                from_list_view, from_sq_view = self.get_list_and_square_from_view(from_block)
                                                to_list_view, to_sq_view = self.get_list_and_square_from_view(to_block)
                                                
                                                self.model.move_piece(from_list_model, from_sq_model, to_list_model,
                                                                          to_sq_model)
                                                self.view.move_piece(from_list_view, from_sq_view, to_list_view,
                                                                         to_sq_view)
                                                if to_list_view is self.view.main_board:
                                                    self.check_slide(to_sq_view, "blue")
                                                if to_list_model is self.model.blue_safety and to_sq_model == 5:
                                                    self.check_win('blue')
                                                self.display_all_starts()
                                                self.change_player()
                                        else:
                                            # main board move of 11
                                            to_block = (from_block + 11) % 60
                                            legal_move = self.check_legal_move(self.model.main_board, from_block,
                                                self.model.main_board, to_block, 'blue')
                                            if legal_move:
                                                # carry out legal move
                                                from_list_model, from_sq_model = self.get_list_and_square_from_model(from_block)
                                                to_list_model, to_sq_model = self.get_list_and_square_from_model(to_block)
                                                from_list_view, from_sq_view = self.get_list_and_square_from_view(from_block)
                                                to_list_view, to_sq_view = self.get_list_and_square_from_view(to_block)
                                                
                                                self.model.move_piece(from_list_model, from_sq_model, to_list_model,
                                                                          to_sq_model)
                                                self.view.move_piece(from_list_view, from_sq_view, to_list_view,
                                                                         to_sq_view)
                                                if to_list_view is self.view.main_board:
                                                    self.check_slide(to_sq_view, "blue")
                                                if to_list_model is self.model.blue_safety and to_sq_model == 5:
                                                    self.check_win('blue')
                                                self.display_all_starts()
                                                self.change_player()
                                    else:
                                        # trade pieces if legal move
                                        to_block = second_block
                                        if 0 <= to_block <= 59:
                                            if self.model.main_board[to_block].is_occupied():
                                                if self.model.main_board[to_block].get_color() != 'blue':
                                                    op_piece_color = self.model.main_board[to_block].get_color()
                                                    legal_move = True
                                                    # carry out legal move
                                                    self.model.trade_pieces(from_block, to_block)
                                                    self.view.trade_pieces(from_block, to_block)
                                                    self.check_slide(to_block, 'blue')
                                                    self.check_slide(from_block, op_piece_color)
                                                    self.display_all_starts()
                                                    self.change_player()
                        
                else:
                    # click to trade pieces or click draw pile to forfeit
                    legal_move = False
                    while legal_move == False:
                        self.view.display_text("Click on one of your pieces \n to trade or click draw pile \n to forfeit turn.")
                        # get first click
                        click_point = self.view.win.getMouse()
                        x = click_point.getX()
                        y = click_point.getY()
                        from_block = self.view.get_block(x, y)
                        if from_block == 500:
                            # forfeit turn
                            self.change_player()
                            legal_move = True
                        elif 0 <= from_block <= 59:
                            if self.model.main_board[from_block].is_occupied():
                                if self.model.main_board[from_block].get_color() == 'blue':
                                    # get second click
                                    self.view.display_text("Click on opposing piece to trade.")
                                    click_point = self.view.win.getMouse()
                                    x = click_point.getX()
                                    y = click_point.getY()
                                    to_block = self.view.get_block(x, y)
                                    if 0 <= to_block <= 59:
                                        if self.model.main_board[to_block].is_occupied():
                                            if self.model.main_board[to_block].get_color() != 'blue':
                                                # trade pieces
                                                op_piece_color = self.model.main_board[to_block].get_color()
                                                legal_move = True
                                                self.model.trade_pieces(from_block, to_block)
                                                self.view.trade_pieces(from_block, to_block)
                                                self.check_slide(to_block, 'blue')
                                                self.check_slide(from_block, op_piece_color)
                                                self.display_all_starts()
                                                self.change_player()
                    
            else:
                # no move exists: forfeit turn
                self.view.display_text("No move possible. Click draw pile \n to forfeit turn.")
                block = 1000
                while block != 500:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    block = self.view.get_block(x, y)
                self.change_player()

    def twelve_card_player1(self):
        """
        Does: plays out 'twelve card' scenario
        """
        self.view.display_text('Click on piece to move twelve squares.')
        if self.player1.get_color() == 'yellow':
            if self.twelve_card_move_exists('yellow'):
                # get click
                legal_move = False
                while legal_move == False:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    from_block = self.view.get_block(x, y)
                    # check if entering safety zone
                    if from_block <= 58 and from_block + 12 > 58:
                        to_block = (from_block + 12) % 59 + 100
                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                            self.model.yellow_safety, to_block - 100, 'yellow')
                    
                    # check if on main_board
                    elif 0 <= from_block <= 59:
                        to_block = (from_block + 12) % 60
                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                            self.model.main_board, to_block, 'yellow')
                    
                # carry out legal move
                from_list_model, from_sq_model = self.get_list_and_square_from_model(from_block)
                to_list_model, to_sq_model = self.get_list_and_square_from_model(to_block)
                from_list_view, from_sq_view = self.get_list_and_square_from_view(from_block)
                to_list_view, to_sq_view = self.get_list_and_square_from_view(to_block)
                
                self.model.move_piece(from_list_model, from_sq_model, to_list_model,
                                          to_sq_model)
                self.view.move_piece(from_list_view, from_sq_view, to_list_view,
                                         to_sq_view)
                if to_list_view is self.view.main_board:
                    self.check_slide(to_sq_view, "yellow")
                if to_list_model is self.model.yellow_safety and to_sq_model == 5:
                    self.check_win('yellow')
                self.display_all_starts()
                self.change_player()
                    
            else:
                # move doesn't exist: forfeit turn
                self.view.display_text("No move possible. Click draw pile \n to forfeit turn.")
                block = 1000
                while block != 500:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    block = self.view.get_block(x, y)
                self.change_player()
        elif self.player1.get_color() == 'green':
            if self.twelve_card_move_exists('green'):
                # get click
                legal_move = False
                while legal_move == False:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    from_block = self.view.get_block(x, y)
                    # check if entering safety zone
                    if from_block <= 13 and from_block + 12 > 13:
                        to_block = (from_block + 12) % 14 + 200
                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                            self.model.green_safety, to_block - 200, 'green')
                    
                    # check if on main_board
                    elif 0 <= from_block <= 59:
                        to_block = (from_block + 12) % 60
                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                            self.model.main_board, to_block, 'green')
                    
                # carry out legal move
                from_list_model, from_sq_model = self.get_list_and_square_from_model(from_block)
                to_list_model, to_sq_model = self.get_list_and_square_from_model(to_block)
                from_list_view, from_sq_view = self.get_list_and_square_from_view(from_block)
                to_list_view, to_sq_view = self.get_list_and_square_from_view(to_block)
                
                self.model.move_piece(from_list_model, from_sq_model, to_list_model,
                                          to_sq_model)
                self.view.move_piece(from_list_view, from_sq_view, to_list_view,
                                         to_sq_view)
                if to_list_view is self.view.main_board:
                    self.check_slide(to_sq_view, "green")
                if to_list_model is self.model.green_safety and to_sq_model == 5:
                    self.check_win('green')
                self.display_all_starts()
                self.change_player()
                    
            else:
                # move doesn't exist: forfeit turn
                self.view.display_text("No move possible. Click draw pile \n to forfeit turn.")
                block = 1000
                while block != 500:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    block = self.view.get_block(x, y)
                self.change_player()
        elif self.player1.get_color() == 'red':
            if self.twelve_card_move_exists('red'):
                # get click
                legal_move = False
                while legal_move == False:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    from_block = self.view.get_block(x, y)
                    # check if entering safety zone
                    if from_block <= 28 and from_block + 12 > 28:
                        to_block = (from_block + 12) % 29 + 300
                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                            self.model.red_safety, to_block - 300, 'red')
                    
                    # check if on main_board
                    elif 0 <= from_block <= 59:
                        to_block = (from_block + 12) % 60
                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                            self.model.main_board, to_block, 'red')
                    
                # carry out legal move
                from_list_model, from_sq_model = self.get_list_and_square_from_model(from_block)
                to_list_model, to_sq_model = self.get_list_and_square_from_model(to_block)
                from_list_view, from_sq_view = self.get_list_and_square_from_view(from_block)
                to_list_view, to_sq_view = self.get_list_and_square_from_view(to_block)
                
                self.model.move_piece(from_list_model, from_sq_model, to_list_model,
                                          to_sq_model)
                self.view.move_piece(from_list_view, from_sq_view, to_list_view,
                                         to_sq_view)
                if to_list_view is self.view.main_board:
                    self.check_slide(to_sq_view, "red")
                if to_list_model is self.model.red_safety and to_sq_model == 5:
                    self.check_win('red')
                self.display_all_starts()
                self.change_player()
                    
            else:
                # move doesn't exist: forfeit turn
                self.view.display_text("No move possible. Click draw pile \n to forfeit turn.")
                block = 1000
                while block != 500:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    block = self.view.get_block(x, y)
                self.change_player()
        elif self.player1.get_color() == 'blue':
            if self.twelve_card_move_exists('blue'):
                # get click
                legal_move = False
                while legal_move == False:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    from_block = self.view.get_block(x, y)
                    # check if entering safety zone
                    if from_block <= 43 and from_block + 12 > 43:
                        to_block = (from_block + 12) % 44 + 400
                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                            self.model.blue_safety, to_block - 400, 'blue')
                    
                    # check if on main_board
                    elif 0 <= from_block <= 59:
                        to_block = (from_block + 12) % 60
                        legal_move = self.check_legal_move(self.model.main_board, from_block,
                                            self.model.main_board, to_block, 'blue')
                    
                # carry out legal move
                from_list_model, from_sq_model = self.get_list_and_square_from_model(from_block)
                to_list_model, to_sq_model = self.get_list_and_square_from_model(to_block)
                from_list_view, from_sq_view = self.get_list_and_square_from_view(from_block)
                to_list_view, to_sq_view = self.get_list_and_square_from_view(to_block)
                
                self.model.move_piece(from_list_model, from_sq_model, to_list_model,
                                          to_sq_model)
                self.view.move_piece(from_list_view, from_sq_view, to_list_view,
                                         to_sq_view)
                if to_list_view is self.view.main_board:
                    self.check_slide(to_sq_view, "blue")
                if to_list_model is self.model.blue_safety and to_sq_model == 5:
                    self.check_win('blue')
                self.display_all_starts()
                self.change_player()
                    
            else:
                # move doesn't exist: forfeit turn
                self.view.display_text("No move possible. Click draw pile \n to forfeit turn.")
                block = 1000
                while block != 500:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    block = self.view.get_block(x, y)
                self.change_player()

    def sorry_card_player1(self):
        """
        Does: Plays out 'sorry card' scenario for player 1
        """
        if self.player1.get_color() == 'yellow':
            if self.sorry_card_move_exists('yellow'):
                legal_move = False
                while legal_move == False:
                    self.view.display_text("Click on opposing piece to capture \n and send back to start.")
                    # get click
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    to_block = self.view.get_block(x, y)
                    if 0 <= to_block <= 59:
                        if self.model.main_board[to_block].is_occupied():
                            if self.model.main_board[to_block].get_color() != 'yellow':
                                legal_move = True
                # complete legal move
                self.model.move_piece_from_start(self.model.yellow_start, to_block)
                self.view.move_piece_from_start(self.view.yellow_start, to_block)
                self.check_slide(to_block, "yellow")
                self.display_all_starts()
                self.change_player()
            else:
                # move doesn't exist: forfeit turn
                self.view.display_text("No move possible. Click draw pile \n to forfeit turn.")
                block = 1000
                while block != 500:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    block = self.view.get_block(x, y)
                self.change_player()
        elif self.player1.get_color() == 'green':
            if self.sorry_card_move_exists('green'):
                legal_move = False
                while legal_move == False:
                    self.view.display_text("Click on opposing piece to capture \n and send back to start.")
                    # get click
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    to_block = self.view.get_block(x, y)
                    if 0 <= to_block <= 59:
                        if self.model.main_board[to_block].is_occupied():
                            if self.model.main_board[to_block].get_color() != 'green':
                                legal_move = True
                # complete legal move
                self.model.move_piece_from_start(self.model.green_start, to_block)
                self.view.move_piece_from_start(self.view.green_start, to_block)
                self.check_slide(to_block, "green")
                self.display_all_starts()
                self.change_player()
            else:
                # move doesn't exist: forfeit turn
                self.view.display_text("No move possible. Click draw pile \n to forfeit turn.")
                block = 1000
                while block != 500:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    block = self.view.get_block(x, y)
                self.change_player()
        elif self.player1.get_color() == 'red':
            if self.sorry_card_move_exists('red'):
                legal_move = False
                while legal_move == False:
                    self.view.display_text("Click on opposing piece to capture \n and send back to start.")
                    # get click
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    to_block = self.view.get_block(x, y)
                    if 0 <= to_block <= 59:
                        if self.model.main_board[to_block].is_occupied():
                            if self.model.main_board[to_block].get_color() != 'red':
                                legal_move = True
                # complete legal move
                self.model.move_piece_from_start(self.model.red_start, to_block)
                self.view.move_piece_from_start(self.view.red_start, to_block)
                self.check_slide(to_block, "red")
                self.display_all_starts()
                self.change_player()
            else:
                # move doesn't exist: forfeit turn
                self.view.display_text("No move possible. Click draw pile \n to forfeit turn.")
                block = 1000
                while block != 500:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    block = self.view.get_block(x, y)
                self.change_player()
        elif self.player1.get_color() == 'blue':
            if self.sorry_card_move_exists('blue'):
                legal_move = False
                while legal_move == False:
                    self.view.display_text("Click on opposing piece to capture \n and send back to start.")
                    # get click
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    to_block = self.view.get_block(x, y)
                    if 0 <= to_block <= 59:
                        if self.model.main_board[to_block].is_occupied():
                            if self.model.main_board[to_block].get_color() != 'blue':
                                legal_move = True
                # complete legal move
                self.model.move_piece_from_start(self.model.blue_start, to_block)
                self.view.move_piece_from_start(self.view.blue_start, to_block)
                self.check_slide(to_block, "blue")
                self.display_all_starts()
                self.change_player()
            else:
                # move doesn't exist: forfeit turn
                self.view.display_text("No move possible. Click draw pile \n to forfeit turn.")
                block = 1000
                while block != 500:
                    click_point = self.view.win.getMouse()
                    x = click_point.getX()
                    y = click_point.getY()
                    block = self.view.get_block(x, y)
                self.change_player()

    def play_computer_turn(self, player_color):
        """
        Does: Draws card, then calls computer player method according to card drawn
        """
        if self.model.deck.is_empty():
            self.model.deck = deck()
            self.view.undraw_discard_pile()
            self.view.display_text("Shuffling....")
            time.sleep(PAUSE)
            self.view.display_draw_pile()
        
        self.draw_card()
        if isinstance(self.model.discard[-1], oneCard):
            self.one_card_computer_player(player_color)
        elif isinstance(self.model.discard[-1], twoCard):
            self.two_card_computer_player(player_color)
        elif isinstance(self.model.discard[-1], threeCard):
            self.three_card_computer_player(player_color)
        elif isinstance(self.model.discard[-1], fourCard):
            self.four_card_computer_player(player_color)
        elif isinstance(self.model.discard[-1], fiveCard):
            self.five_card_computer_player(player_color)
        elif isinstance(self.model.discard[-1], sevenCard):
            self.seven_card_computer_player(player_color)
        elif isinstance(self.model.discard[-1], eightCard):
            self.eight_card_computer_player(player_color)
        elif isinstance(self.model.discard[-1], tenCard):
            self.ten_card_computer_player(player_color)
        elif isinstance(self.model.discard[-1], elevenCard):
            self.eleven_card_computer_player(player_color)
        elif isinstance(self.model.discard[-1], twelveCard):
            self.twelve_card_computer_player(player_color)
        elif isinstance(self.model.discard[-1], sorryCard):
            self.sorry_card_computer_player(player_color)
        return

    def one_card_computer_player(self, color):
##        self.view.display_text("{} draws a One.".format(color.capitalize()))
##        time.sleep(PAUSE)
##        self.change_player()
##        return
        """
        Does: Handles all strategies for one_card, changes player at end
        """
        # first, check if move exists
        if not self.one_card_move_exists(color):
            # move does not exist
            self.view.display_text("No move possible. {} player \n forfeits turn.".format(color.capitalize()))
            time.sleep(PAUSE)
        else:
            self.view.display_text("{} draws a One.".format(color.capitalize()))
            time.sleep(PAUSE)
            has_moved = False
            if not has_moved:
                has_moved = self.move_home_strategy(color, 1)
            if not has_moved:
                has_moved = self.move_man_out_strategy(color)
            if not has_moved:
                has_moved = self.move_into_safety_strategy(color, 1)
            if not has_moved:
                has_moved = self.attack_opponent_strategy(color, 1)
                # this must include sliding attack
            if not has_moved:
                has_moved = self.slide_safely_strategy(color, 1)
                # slide without hurting self
            if not has_moved:
                has_moved = self.move_off_of_start_spots_strategy(color, 1)
            if not has_moved:
                has_moved = self.any_possible_forward_move_strategy(color, 1)
        self.change_player()

    def two_card_computer_player(self, color):
##        self.view.display_text("{} draws a Two.".format(color.capitalize()))
##        time.sleep(PAUSE)
##        self.change_player()
##        return
        """
        Does: Handles all strategies for two_card, changes player at end
        """
        # first, check if move exists
        if not self.two_card_move_exists(color):
            # move does not exist
            self.view.display_text("No move possible. {} player \n forfeits turn.".format(color.capitalize()))
            time.sleep(PAUSE)
        else:
            self.view.display_text("{} draws a Two.".format(color.capitalize()))
            time.sleep(PAUSE)
            has_moved = False
            if not has_moved:
                has_moved = self.move_home_strategy(color, 2)
            if not has_moved:
                has_moved = self.move_man_out_strategy(color)
            if not has_moved:
                has_moved = self.move_into_safety_strategy(color, 2)
            if not has_moved:
                has_moved = self.attack_opponent_strategy(color, 2)
                # this must include sliding attack
            if not has_moved:
                has_moved = self.slide_safely_strategy(color, 2)
                # slide without hurting self
            if not has_moved:
                has_moved = self.move_off_of_start_spots_strategy(color, 2)
            if not has_moved:
                has_moved = self.any_possible_forward_move_strategy(color, 2)
        # check if game is won before taking next turn
        if self.game_over == False:
            self.view.display_text("{} draws again.".format(color.capitalize()))
            time.sleep(SHORT_PAUSE)
            self.play_computer_turn(color)

    def three_card_computer_player(self, color):
##        self.view.display_text("{} draws a Three.".format(color.capitalize()))
##        time.sleep(PAUSE)
##        self.change_player()
##        return
        """
        Does: Handles all strategies for three_card, changes player at end
        """
        # first, check if move exists
        if not self.three_card_move_exists(color):
            # move does not exist
            self.view.display_text("No move possible. {} player \n forfeits turn.".format(color.capitalize()))
            time.sleep(PAUSE)
        else:
            self.view.display_text("{} draws a Three.".format(color.capitalize()))
            time.sleep(PAUSE)
            has_moved = False
            if not has_moved:
                has_moved = self.move_home_strategy(color, 3)
            if not has_moved:
                has_moved = self.move_into_safety_strategy(color, 3)
            if not has_moved:
                has_moved = self.attack_opponent_strategy(color, 3)
                # this must include sliding attack
            if not has_moved:
                has_moved = self.slide_safely_strategy(color, 3)
                # slide without hurting self
            if not has_moved:
                has_moved = self.move_off_of_start_spots_strategy(color, 3)
            if not has_moved:
                has_moved = self.any_possible_forward_move_strategy(color, 3)
        self.change_player()

    def four_card_computer_player(self, color):
##        self.view.display_text("{} draws a Four.".format(color.capitalize()))
##        time.sleep(PAUSE)
##        self.change_player()
##        return
        """
        Does: Handels all strategies for four_card, changes player at end
        """
        # first, check if move exists
        if not self.four_card_move_exists(color):
            # move does not exist
            self.view.display_text("No move possible. {} player \n forfeits turn.".format(color.capitalize()))
            time.sleep(PAUSE)
        else:
            self.view.display_text("{} draws a Four.".format(color.capitalize()))
            time.sleep(PAUSE)
            has_moved = False
            if not has_moved:
                has_moved = self.check_if_near_start_four_backward_move_strategy(color)
            if not has_moved:
                has_moved = self.check_to_attack_opponent_backward_move_strategy(color, 4)
                # must also check if safe_slide and/or attack_slide
            if not has_moved:
                has_moved = self.check_move_off_of_start_spots_backward_move_strategy(color, 4)
            if not has_moved:
                has_moved = self.check_safe_slide_backward_move_strategy(color, 4)
            if not has_moved:
                has_moved = self.check_main_board_backward_move_strategy(color, 4)
            if not has_moved:
                has_moved = self.check_safety_zone_backward_move_strategy(color, 4)
        self.change_player()

    def five_card_computer_player(self, color):
##        self.view.display_text("{} draws a Five.".format(color.capitalize()))
##        time.sleep(PAUSE)
##        self.change_player()
##        return
        """
        Does: Handles all strategies for five_card, changes player at end
        """
        # first, check if move exists
        if not self.five_card_move_exists(color):
            # move does not exist
            self.view.display_text("No move possible. {} player \n forfeits turn.".format(color.capitalize()))
            time.sleep(PAUSE)
        else:
            self.view.display_text("{} draws a Five.".format(color.capitalize()))
            time.sleep(PAUSE)
            has_moved = False
            if not has_moved:
                has_moved = self.move_home_strategy(color, 5)
            if not has_moved:
                has_moved = self.move_into_safety_strategy(color, 5)
            if not has_moved:
                has_moved = self.attack_opponent_strategy(color, 5)
                # this must include sliding attack
            if not has_moved:
                has_moved = self.slide_safely_strategy(color, 5)
                # slide without hurting self
            if not has_moved:
                has_moved = self.move_off_of_start_spots_strategy(color, 5)
            if not has_moved:
                has_moved = self.any_possible_forward_move_strategy(color, 5)
        self.change_player()

    def seven_card_computer_player(self, color):
##        self.view.display_text("{} draws a Seven.".format(color.capitalize()))
##        time.sleep(PAUSE)
##        self.change_player()
##        return
        """
        Does: Handles all strategies for seven_card, changes player at end
        """
        # first, check if move exists
        if not self.seven_card_move_exists(color):
            # move does not exist
            self.view.display_text("No move possible. {} player \n forfeits turn.".format(color.capitalize()))
            time.sleep(PAUSE)
        else:
            self.view.display_text("{} draws a Seven.".format(color.capitalize()))
            time.sleep(PAUSE)
            has_moved = False
            if not has_moved:
                has_moved = self.move_home_strategy(color, 7)
            if not has_moved:
                has_moved = self.split_get_one_piece_home_strategy(color)
            if not has_moved:
                has_moved = self.move_into_safety_strategy(color, 7)
            if not has_moved:
                has_moved = self.attack_opponent_strategy(color, 7)
            if not has_moved:
                has_moved = self.split_attack_opponent_strategy(color)
                # this must include sliding attack
            if not has_moved:
                has_moved = self.slide_safely_strategy(color, 7)
            if not has_moved:
                has_moved = self.split_slide_safely_strategy(color)
                # slide without hurting self
            if not has_moved:
                has_moved = self.any_possible_forward_move_strategy(color, 7)
            if not has_moved:
                has_moved = self.split_cannot_move_seven_strategy(color)
        self.change_player()

    def eight_card_computer_player(self, color):
##        self.view.display_text("{} draws an Eight.".format(color.capitalize()))
##        time.sleep(PAUSE)
##        self.change_player()
##        return
        """
        Does: Handles all strategies for eight_card, changes player at end
        """
        # first, check if move exists
        if not self.eight_card_move_exists(color):
            # move does not exist
            self.view.display_text("No move possible. {} player \n forfeits turn.".format(color.capitalize()))
            time.sleep(PAUSE)
        else:
            self.view.display_text("{} draws an Eight.".format(color.capitalize()))
            time.sleep(PAUSE)
            has_moved = False
            if not has_moved:
                has_moved = self.move_home_strategy(color, 8)
            if not has_moved:
                has_moved = self.move_into_safety_strategy(color, 8)
            if not has_moved:
                has_moved = self.attack_opponent_strategy(color, 8)
                # this must include sliding attack
            if not has_moved:
                has_moved = self.slide_safely_strategy(color, 8)
                # slide without hurting self
            if not has_moved:
                has_moved = self.move_off_of_start_spots_strategy(color, 8)
            if not has_moved:
                has_moved = self.any_possible_forward_move_strategy(color, 8)
        self.change_player()

    def ten_card_computer_player(self, color):
##        self.view.display_text("{} draws a Ten.".format(color.capitalize()))
##        time.sleep(PAUSE)
##        self.change_player()
##        return
        """
        Does: Handles all strategies for ten_card, changes player at end
        """
        # first, check if move exists
        if not self.ten_card_move_exists(color):
            # move does not exist
            self.view.display_text("No move possible. {} player \n forfeits turn.".format(color.capitalize()))
            time.sleep(PAUSE)
        else:
            self.view.display_text("{} draws a Ten.".format(color.capitalize()))
            time.sleep(PAUSE)
            has_moved = False
            if not has_moved:
                has_moved = self.move_home_strategy(color, 10)
            if not has_moved:
                has_moved = self.move_into_safety_strategy(color, 10)
            if not has_moved:
                has_moved = self.attack_opponent_strategy(color, 10)
                # this must include sliding attack
            if not has_moved:
                has_moved = self.check_to_attack_opponent_backward_move_strategy(color, 1)
                # slide without hurting self
            if not has_moved:
                has_moved = self.check_if_near_start_backward_move_one_strategy(color)
            if not has_moved:
                has_moved = self.move_off_of_start_spots_strategy(color, 10)
            if not has_moved:
                has_moved = self.check_move_off_of_start_spots_backward_move_strategy(color, 1)
            if not has_moved:
                has_moved = self.slide_safely_strategy(color, 10)
            if not has_moved:
                has_moved = self.any_possible_forward_move_strategy(color, 10)
            if not has_moved:
                has_moved = self.check_safe_slide_backward_move_strategy(color, 1)
            if not has_moved:
                has_moved = self.check_main_board_backward_move_strategy(color, 1)
            if not has_moved:
                has_moved = self.check_safety_zone_backward_move_strategy(color, 1)
        self.change_player()

    def eleven_card_computer_player(self, color):
##        self.view.display_text("{} draws an Eleven.".format(color.capitalize()))
##        time.sleep(PAUSE)
##        self.change_player()
##        return
        """
        Does: Handles all strategies for eleven_card, changes player at end
        """
        # first, check if move exists
        if not self.eleven_card_move_exists(color):
            # move does not exist
            self.view.display_text("No move possible. {} player \n forfeits turn.".format(color.capitalize()))
            time.sleep(PAUSE)
        else:
            self.view.display_text("{} draws an Eleven.".format(color.capitalize()))
            time.sleep(PAUSE)
            has_moved = False
            if not has_moved:
                has_moved = self.move_home_strategy(color, 11)
            if not has_moved:
                has_moved = self.move_into_safety_strategy(color, 11)
            if not has_moved:
                has_moved = self.attack_opponent_strategy(color, 11)
                # this must include sliding attack
            if not has_moved:
                has_moved = self.make_good_trade_strategy(color)
            if not has_moved:
                has_moved = self.move_off_of_start_spots_strategy(color, 11)
            if not has_moved:
                has_moved = self.slide_safely_strategy(color, 11)
            if not has_moved:
                has_moved = self.any_possible_forward_move_strategy(color, 11)
            if not has_moved:
                has_moved = self.forfeit_turn_strategy(color)
        self.change_player()

    def twelve_card_computer_player(self, color):
##        self.view.display_text("{} draws a Twelve.".format(color.capitalize()))
##        time.sleep(PAUSE)
##        self.change_player()
##        return
        """
        Does: Handles all strategies for twelve_card, changes player at end
        """
        # first, check if move exists
        if not self.twelve_card_move_exists(color):
            # move does not exist
            self.view.display_text("No move possible. {} player \n forfeits turn.".format(color.capitalize()))
            time.sleep(PAUSE)
        else:
            self.view.display_text("{} draws a Twelve.".format(color.capitalize()))
            time.sleep(PAUSE)
            has_moved = False
            if not has_moved:
                has_moved = self.move_home_strategy(color, 12)
            if not has_moved:
                has_moved = self.move_into_safety_strategy(color, 12)
            if not has_moved:
                has_moved = self.attack_opponent_strategy(color, 12)
                # this must include sliding attack
            if not has_moved:
                has_moved = self.slide_safely_strategy(color, 12)
                # slide without hurting self
            if not has_moved:
                has_moved = self.move_off_of_start_spots_strategy(color, 12)
            if not has_moved:
                has_moved = self.any_possible_forward_move_strategy(color, 12)
        self.change_player()

    def sorry_card_computer_player(self, color):
##        self.view.display_text("{} draws SORRY!".format(color.capitalize()))
##        time.sleep(PAUSE)
##        self.change_player()
##        return
        """
        Does: Handles all strategies for sorry_card, changes player at end
        """
        # first, check if move exists
        if not self.sorry_card_move_exists(color):
            # move does not exist
            self.view.display_text("No move possible. {} player \n forfeits turn.".format(color.capitalize()))
            time.sleep(PAUSE)
        else:
            self.view.display_text("{} draws SORRY!.".format(color.capitalize()))
            time.sleep(PAUSE)
            has_moved = False
            if not has_moved:
                has_moved = self.attack_multiple_men_with_slide_sorry_strategy(color)
            if not has_moved:
                has_moved = self.attack_opponent_nearest_home_sorry_strategy(color)
        self.change_player()

    def move_man_out_strategy(self, color):
        """
        Does: Tries to move man out of start
        Returns: True if move was completed
        """
        if color == "yellow":
            if self.model.yellow_start:
                if self.model.main_board[0].is_occupied():
                    if self.model.main_board[0].get_color() != color:
                        # start spot has opponent's piece
                        self.model.move_piece_from_start(self.model.yellow_start, 0)
                        self.view.move_piece_from_start(self.view.yellow_start, 0)
                        self.display_all_starts()
                        ##print('{}: move_man_out_strategy'.format(color.capitalize()))
                        return True
                else:
                    # start spot is empty
                    self.model.move_piece_from_start(self.model.yellow_start, 0)
                    self.view.move_piece_from_start(self.view.yellow_start, 0)
                    self.display_all_starts()
                    ##print('{}: move_man_out_strategy'.format(color.capitalize()))
                    return True
        elif color == "green":
            if self.model.green_start:
                if self.model.main_board[15].is_occupied():
                    if self.model.main_board[15].get_color() != color:
                        # start spot has opponent's piece
                        self.model.move_piece_from_start(self.model.green_start, 15)
                        self.view.move_piece_from_start(self.view.green_start, 15)
                        self.display_all_starts()
                        ##print('{}: move_man_out_strategy'.format(color.capitalize()))
                        return True
                else:
                    # start spot is empty
                    self.model.move_piece_from_start(self.model.green_start, 15)
                    self.view.move_piece_from_start(self.view.green_start, 15)
                    self.display_all_starts()
                    ##print('{}: move_man_out_strategy'.format(color.capitalize()))
                    return True
        elif color == "red":
            if self.model.red_start:
                if self.model.main_board[30].is_occupied():
                    if self.model.main_board[30].get_color() != color:
                        # start spot has opponent's piece
                        self.model.move_piece_from_start(self.model.red_start, 30)
                        self.view.move_piece_from_start(self.view.red_start, 30)
                        self.display_all_starts()
                        ##print('{}: move_man_out_strategy'.format(color.capitalize()))
                        return True
                else:
                    # start spot is empty
                    self.model.move_piece_from_start(self.model.red_start, 30)
                    self.view.move_piece_from_start(self.view.red_start, 30)
                    self.display_all_starts()
                    ##print('{}: move_man_out_strategy'.format(color.capitalize()))
                    return True
        elif color == "blue":
            if self.model.blue_start:
                if self.model.main_board[45].is_occupied():
                    if self.model.main_board[45].get_color() != color:
                        # start spot has opponent's piece
                        self.model.move_piece_from_start(self.model.blue_start, 45)
                        self.view.move_piece_from_start(self.view.blue_start, 45)
                        self.display_all_starts()
                        ##print('{}: move_man_out_strategy'.format(color.capitalize()))
                        return True
                else:
                    # start spot is empty
                    self.model.move_piece_from_start(self.model.blue_start, 45)
                    self.view.move_piece_from_start(self.view.blue_start, 45)
                    self.display_all_starts()
                    ##print('{}: move_man_out_strategy'.format(color.capitalize()))
                    return True
        return False

    def move_home_strategy(self, color, move_num):
        """
        Does: checks if piece can move into home, and checks if win
        Returns: True if move was completed
        """
        if color == "yellow":
            # check safety_zone
            for i in range(4, -1, -1):
                if self.model.yellow_safety[i].is_occupied():
                    if i + move_num == 5:
                        self.model.move_piece(self.model.yellow_safety, i, self.model.yellow_safety, 5)
                        self.view.move_piece(self.view.yellow_safety, i, self.view.yellow_safety, 5)
                        self.check_win(color)
                        ##print('{}: move_home_strategy'.format(color.capitalize()))
                        return True
            # check main_board (6 spaces max)
            for i in range(58, 58 - 7, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        if i + move_num > 58:
                            to_sq = move_num - 1 - (58 - i)
                            if to_sq == 5:
                                # complete move
                                self.model.move_piece(self.model.main_board, i, self.model.yellow_safety, to_sq)
                                self.view.move_piece(self.view.main_board, i, self.view.yellow_safety, to_sq)
                                self.check_win(color)
                                ##print('{}: move_home_strategy'.format(color.capitalize()))
                                return True
        elif color == "green":
            # check safety_zone
            for i in range(4, -1, -1):
                if self.model.green_safety[i].is_occupied():
                    if i + move_num == 5:
                        self.model.move_piece(self.model.green_safety, i, self.model.green_safety, 5)
                        self.view.move_piece(self.view.green_safety, i, self.view.green_safety, 5)
                        self.check_win(color)
                        ##print('{}: move_home_strategy'.format(color.capitalize()))
                        return True
            # check main_board (6 spaces max)
            for i in range(13, 13 - 7, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        if i + move_num > 13:
                            to_sq = move_num - 1 - (13 - i)
                            if to_sq == 5:
                                # complete move
                                self.model.move_piece(self.model.main_board, i, self.model.green_safety, to_sq)
                                self.view.move_piece(self.view.main_board, i, self.view.green_safety, to_sq)
                                self.check_win(color)
                                ##print('{}: move_home_strategy'.format(color.capitalize()))
                                return True
        elif color == "red":
            # check safety_zone
            for i in range(4, -1, -1):
                if self.model.red_safety[i].is_occupied():
                    if i + move_num == 5:
                        self.model.move_piece(self.model.red_safety, i, self.model.red_safety, 5)
                        self.view.move_piece(self.view.red_safety, i, self.view.red_safety, 5)
                        self.check_win(color)
                        ##print('{}: move_home_strategy'.format(color.capitalize()))
                        return True
            # check main_board (6 spaces max)
            for i in range(28, 28 - 7, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        if i + move_num > 28:
                            to_sq = move_num - 1 - (28 - i)
                            if to_sq == 5:
                                # complete move
                                self.model.move_piece(self.model.main_board, i, self.model.red_safety, to_sq)
                                self.view.move_piece(self.view.main_board, i, self.view.red_safety, to_sq)
                                self.check_win(color)
                                ##print('{}: move_home_strategy'.format(color.capitalize()))
                                return True
        elif color == "blue":
            # check safety_zone
            for i in range(4, -1, -1):
                if self.model.blue_safety[i].is_occupied():
                    if i + move_num == 5:
                        self.model.move_piece(self.model.blue_safety, i, self.model.blue_safety, 5)
                        self.view.move_piece(self.view.blue_safety, i, self.view.blue_safety, 5)
                        self.check_win(color)
                        #print('{}: move_home_strategy'.format(color.capitalize()))
                        return True
            # check main_board (6 spaces max)
            for i in range(43, 43 - 7, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        if i + move_num > 43:
                            to_sq = move_num - 1 - (43 - i)
                            if to_sq == 5:
                                # complete move
                                self.model.move_piece(self.model.main_board, i, self.model.blue_safety, to_sq)
                                self.view.move_piece(self.view.main_board, i, self.view.blue_safety, to_sq)
                                self.check_win(color)
                                #print('{}: move_home_strategy'.format(color.capitalize()))
                                return True
        return False

    def move_into_safety_strategy(self, color, move_num):
        """
        Does: checks if move into safety (or move within safety) is possible
        Returns: True if move was executed
        """
        if color == "yellow":
            # check main_board (only 12 spaces max)
            for i in range(58, 58 - 12, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        if i + move_num > 58:
                            # check legal move
                            to_sq = move_num - 1 - (58 - i)
                            if self.check_legal_move(self.model.main_board, i, self.model.yellow_safety, to_sq, color):
                                # complete move
                                self.model.move_piece(self.model.main_board, i, self.model.yellow_safety, to_sq)
                                self.view.move_piece(self.view.main_board, i, self.view.yellow_safety, to_sq)
                                if to_sq == 5:
                                    self.check_win(color)
                                #print('{}: move_into_safety_strategy'.format(color.capitalize()))
                                return True
            # check safety_zone
            for i in range(4, -1, -1):
                if self.model.yellow_safety[i].is_occupied():
                    if i + move_num <= 5:
                        # complete move if legal
                        if self.check_legal_move(self.model.yellow_safety, i, self.model.yellow_safety,
                                                 i + move_num, color):
                            # complete move
                            self.model.move_piece(self.model.yellow_safety, i, self.model.yellow_safety, i + move_num)
                            self.view.move_piece(self.view.yellow_safety, i, self.view.yellow_safety, i + move_num)
                            if i + move_num == 5:
                                self.check_win(color)
                            #print('{}: move_into_safety_strategy'.format(color.capitalize()))
                            return True
        elif color == "green":
            # check main_board (only 12 spaces max)
            for i in range(13, 13 - 12, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        if i + move_num > 13:
                            # check legal move
                            to_sq = move_num - 1 - (13 - i)
                            if self.check_legal_move(self.model.main_board, i, self.model.green_safety, to_sq, color):
                                # complete move
                                self.model.move_piece(self.model.main_board, i, self.model.green_safety, to_sq)
                                self.view.move_piece(self.view.main_board, i, self.view.green_safety, to_sq)
                                if to_sq == 5:
                                    self.check_win(color)
                                #print('{}: move_into_safety_strategy'.format(color.capitalize()))
                                return True
            # check safety_zone
            for i in range(4, -1, -1):
                if self.model.green_safety[i].is_occupied():
                    if i + move_num <= 5:
                        # complete move if legal
                        if self.check_legal_move(self.model.green_safety, i, self.model.green_safety,
                                                 i + move_num, color):
                            # complete move
                            self.model.move_piece(self.model.green_safety, i, self.model.green_safety, i + move_num)
                            self.view.move_piece(self.view.green_safety, i, self.view.green_safety, i + move_num)
                            if i + move_num == 5:
                                self.check_win(color)
                            #print('{}: move_into_safety_strategy'.format(color.capitalize()))
                            return True
        elif color == "red":
            # check main_board (only 12 spaces max)
            for i in range(28, 28 - 12, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        if i + move_num > 28:
                            # check legal move
                            to_sq = move_num - 1 - (28 - i)
                            if self.check_legal_move(self.model.main_board, i, self.model.red_safety, to_sq, color):
                                # complete move
                                self.model.move_piece(self.model.main_board, i, self.model.red_safety, to_sq)
                                self.view.move_piece(self.view.main_board, i, self.view.red_safety, to_sq)
                                if to_sq == 5:
                                    self.check_win(color)
                                #print('{}: move_into_safety_strategy'.format(color.capitalize()))
                                return True
            # check safety_zone
            for i in range(4, -1, -1):
                if self.model.red_safety[i].is_occupied():
                    if i + move_num <= 5:
                        # complete move if legal
                        if self.check_legal_move(self.model.red_safety, i, self.model.red_safety,
                                                 i + move_num, color):
                            # complete move
                            self.model.move_piece(self.model.red_safety, i, self.model.red_safety, i + move_num)
                            self.view.move_piece(self.view.red_safety, i, self.view.red_safety, i + move_num)
                            if i + move_num == 5:
                                self.check_win(color)
                            #print('{}: move_into_safety_strategy'.format(color.capitalize()))
                            return True
        elif color == "blue":
            # check main_board (only 12 spaces max)
            for i in range(43, 43 - 12, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        if i + move_num > 43:
                            # check legal move
                            to_sq = move_num - 1 - (43 - i)
                            if self.check_legal_move(self.model.main_board, i, self.model.blue_safety, to_sq, color):
                                # complete move
                                self.model.move_piece(self.model.main_board, i, self.model.blue_safety, to_sq)
                                self.view.move_piece(self.view.main_board, i, self.view.blue_safety, to_sq)
                                if to_sq == 5:
                                    self.check_win(color)
                                #print('{}: move_into_safety_strategy'.format(color.capitalize()))
                                return True
            # check safety_zone
            for i in range(4, -1, -1):
                if self.model.blue_safety[i].is_occupied():
                    if i + move_num <= 5:
                        # complete move if legal
                        if self.check_legal_move(self.model.blue_safety, i, self.model.blue_safety,
                                                 i + move_num, color):
                            # complete move
                            self.model.move_piece(self.model.blue_safety, i, self.model.blue_safety, i + move_num)
                            self.view.move_piece(self.view.blue_safety, i, self.view.blue_safety, i + move_num)
                            if i + move_num == 5:
                                self.check_win(color)
                            #print('{}: move_into_safety_strategy'.format(color.capitalize()))
                            return True
        return False

    def attack_opponent_strategy(self, color, move_num):
        """
        Does: checks if FORWARD move and/or SLIDE attacks an opponent, completes move
        Returns: True if move was executed
        """
        # check if slide
        def is_slide(from_sq):
            # checks if from_sq is the start of a slide
            # Returns: True if is slide
            if from_sq == 57 and color != 'yellow':
                return True
            elif from_sq == 5 and color != 'yellow':
                return True
            elif from_sq == 12 and color != 'green':
                return True
            elif from_sq == 20 and color != 'green':
                return True
            elif from_sq == 27 and color != 'red':
                return True
            elif from_sq == 35 and color != 'red':
                return True
            elif from_sq == 42 and color != 'blue':
                return True
            elif from_sq == 50 and color != 'blue':
                return True
            return False
        
        # must check if SLIDING also attacks opponent
        def is_attack_slide(start_sq):
            def is_attack(from_sq, slide_length):
                for j in range(0, slide_length):
                    if self.model.main_board[(from_sq + j) % 60].is_occupied():
                        if self.model.main_board[(from_sq + j) % 60].get_color() != color:
                            return True
                return False
            # check which slide and slide_length
            if start_sq == 5 and color != "yellow":
                return is_attack(start_sq, 5)
            elif start_sq == 57 and color != "yellow":
                return is_attack(start_sq, 4)
            elif start_sq == 50 and color != "blue":
                return is_attack(start_sq, 5)
            elif start_sq == 42 and color != "blue":
                return is_attack(start_sq, 4)
            elif start_sq == 35 and color != "red":
                return is_attack(start_sq, 5)
            elif start_sq == 27 and color != "red":
                return is_attack(start_sq, 4)
            elif start_sq == 20 and color != "green":
                return is_attack(start_sq, 5)
            elif start_sq == 12 and color != "green":
                return is_attack(start_sq, 4)
            return False
            
        # must also check if 'safe slide'
        def is_safe_slide(start_sq):
            def is_safe(from_sq, slide_length):
                for j in range(1, slide_length):
                    if self.model.main_board[(from_sq + j) % 60].is_occupied():
                        if self.model.main_board[(from_sq + j) % 60].get_color() == color:
                            return False
                return True
            # check which slide and slide_length
            if start_sq == 5 and color != "yellow":
                return is_safe(start_sq, 5)
            elif start_sq == 57 and color != "yellow":
                return is_safe(start_sq, 4)
            elif start_sq == 50 and color != "blue":
                return is_safe(start_sq, 5)
            elif start_sq == 42 and color != "blue":
                return is_safe(start_sq, 4)
            elif start_sq == 35 and color != "red":
                return is_safe(start_sq, 5)
            elif start_sq == 27 and color != "red":
                return is_safe(start_sq, 4)
            elif start_sq == 20 and color != "green":
                return is_safe(start_sq, 5)
            elif start_sq == 12 and color != "green":
                return is_safe(start_sq, 4)
            return False

        # complete move
        def make_move(from_sq, to_sq):
            # makes move: from_sq to to_sq, check_slide
            self.model.move_piece(self.model.main_board, from_sq, self.model.main_board, to_sq)
            self.view.move_piece(self.view.main_board, from_sq, self.view.main_board, to_sq)
            self.check_slide(to_sq, color)
            self.display_all_starts()
            #print('{}: attack_opponent_strategy'.format(color.capitalize()))

        # check if color can attack
        if color == "yellow":
            # first check if forward move attacks directly, then
            # check if possible slide 'attacks' but 'is_safe_slide'
            for i in range(58, -1, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        if i + move_num <= 58:
                            to_sq = i + move_num
                            attacks_directly = False
                            # safe_slide defaults to True to limit options below
                            safe_slide = True
                            attack_slide = False
                            if self.model.main_board[to_sq].is_occupied():
                                if self.model.main_board[to_sq].get_color() != color:
                                    # piece at to_sq is opponent: check if slide
                                    attacks_directly = True
                            # check if slide
                            must_slide = is_slide(to_sq)
                            # check if safe_slide
                            if must_slide:
                                safe_slide = is_safe_slide(to_sq)
                                attack_slide = is_attack_slide(to_sq)
                            # check all conditions: attacks_directly, safe_slide, attack_slide
                            # if attacks directly and safe_slide: do move
                            # elif attacks directly and not safe_slide: do nothing
                            # elif not attacks_directly, but (safe_slide and attack_slide): do move
                            # elif not attacks_directly, and (not safe_slide or not attack_slide): do nothing
                            if (attacks_directly and safe_slide) or (not attacks_directly and safe_slide and attack_slide):
                                # do move
                                make_move(i, to_sq)
                                return True
            # check rest of main_board
            for i in range(59, 58, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        # slide not possible: check attacks_directly only
                        if self.model.main_board[(i + move_num) % 60].is_occupied():
                            if self.model.main_board[(i + move_num) % 60].get_color() != color:
                                # target is opponent piece: do move
                                make_move(i, (i + move_num) % 60)
                                return True
        elif color == "green":
            # first check if forward move attacks directly, then
            # check if possible slide 'attacks' but 'is_safe_slide'
            for i in range(13, -1, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        if i + move_num <= 13:
                            to_sq = (i + move_num) % 60
                            attacks_directly = False
                            # safe_slide defaults to True to limit options below
                            safe_slide = True
                            attack_slide = False
                            if self.model.main_board[to_sq].is_occupied():
                                if self.model.main_board[to_sq].get_color() != color:
                                    # piece at to_sq is opponent: check if slide
                                    attacks_directly = True
                            # check if slide
                            must_slide = is_slide(to_sq)
                            # check if safe_slide
                            if must_slide:
                                safe_slide = is_safe_slide(to_sq)
                                attack_slide = is_attack_slide(to_sq)
                            # check all conditions: attacks_directly, safe_slide, attack_slide
                            # if attacks directly and safe_slide: do move
                            # elif attacks directly and not safe_slide: do nothing
                            # elif not attacks_directly, but (safe_slide and attack_slide): do move
                            # elif not attacks_directly, and (not safe_slide or not attack_slide): do nothing
                            if (attacks_directly and safe_slide) or (not attacks_directly and safe_slide and attack_slide):
                                # do move
                                make_move(i, to_sq)
                                return True
            # check rest of main_board
            for i in range(59, 13, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        # don't need to check if moving into safety_zone
                        to_sq = (i + move_num) % 60
                        attacks_directly = False
                        # safe_slide defaults to True to limit options below
                        safe_slide = True
                        attack_slide = False
                        if self.model.main_board[to_sq].is_occupied():
                            if self.model.main_board[to_sq].get_color() != color:
                                # piece at to_sq is opponent: check if slide
                                attacks_directly = True
                        # check if slide
                        must_slide = is_slide(to_sq)
                        # check if safe_slide
                        if must_slide:
                            safe_slide = is_safe_slide(to_sq)
                            attack_slide = is_attack_slide(to_sq)
                        # check all conditions: attacks_directly, safe_slide, attack_slide
                        # if attacks directly and safe_slide: do move
                        # elif attacks directly and not safe_slide: do nothing
                        # elif not attacks_directly, but (safe_slide and attack_slide): do move
                        # elif not attacks_directly, and (not safe_slide or not attack_slide): do nothing
                        if (attacks_directly and safe_slide) or (not attacks_directly and safe_slide and attack_slide):
                            # do move
                            make_move(i, to_sq)
                            return True
        elif color == "red":
            # first check if forward move attacks directly, then
            # check if possible slide 'attacks' but 'is_safe_slide'
            for i in range(28, -1, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        if i + move_num <= 28:
                            to_sq = (i + move_num) % 60
                            attacks_directly = False
                            # safe_slide defaults to True to limit options below
                            safe_slide = True
                            attack_slide = False
                            if self.model.main_board[to_sq].is_occupied():
                                if self.model.main_board[to_sq].get_color() != color:
                                    # piece at to_sq is opponent: check if slide
                                    attacks_directly = True
                            # check if slide
                            must_slide = is_slide(to_sq)
                            # check if safe_slide
                            if must_slide:
                                safe_slide = is_safe_slide(to_sq)
                                attack_slide = is_attack_slide(to_sq)
                            # check all conditions: attacks_directly, safe_slide, attack_slide
                            # if attacks directly and safe_slide: do move
                            # elif attacks directly and not safe_slide: do nothing
                            # elif not attacks_directly, but (safe_slide and attack_slide): do move
                            # elif not attacks_directly, and (not safe_slide or not attack_slide): do nothing
                            if (attacks_directly and safe_slide) or (not attacks_directly and safe_slide and attack_slide):
                                # do move
                                make_move(i, to_sq)
                                return True
            # check rest of main_board
            for i in range(59, 28, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        # don't need to check if moving into safety_zone
                        to_sq = (i + move_num) % 60
                        attacks_directly = False
                        # safe_slide defaults to True to limit options below
                        safe_slide = True
                        attack_slide = False
                        if self.model.main_board[to_sq].is_occupied():
                            if self.model.main_board[to_sq].get_color() != color:
                                # piece at to_sq is opponent: check if slide
                                attacks_directly = True
                        # check if slide
                        must_slide = is_slide(to_sq)
                        # check if safe_slide
                        if must_slide:
                            safe_slide = is_safe_slide(to_sq)
                            attack_slide = is_attack_slide(to_sq)
                        # check all conditions: attacks_directly, safe_slide, attack_slide
                        # if attacks directly and safe_slide: do move
                        # elif attacks directly and not safe_slide: do nothing
                        # elif not attacks_directly, but (safe_slide and attack_slide): do move
                        # elif not attacks_directly, and (not safe_slide or not attack_slide): do nothing
                        if (attacks_directly and safe_slide) or (not attacks_directly and safe_slide and attack_slide):
                            # do move
                            make_move(i, to_sq)
                            return True
        elif color == "blue":
            # first check if forward move attacks directly, then
            # check if possible slide 'attacks' but 'is_safe_slide'
            for i in range(43, -1, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        if i + move_num <= 43:
                            to_sq = (i + move_num) % 60
                            attacks_directly = False
                            # safe_slide defaults to True to limit options below
                            safe_slide = True
                            attack_slide = False
                            if self.model.main_board[to_sq].is_occupied():
                                if self.model.main_board[to_sq].get_color() != color:
                                    # piece at to_sq is opponent: check if slide
                                    attacks_directly = True
                            # check if slide
                            must_slide = is_slide(to_sq)
                            # check if safe_slide
                            if must_slide:
                                safe_slide = is_safe_slide(to_sq)
                                attack_slide = is_attack_slide(to_sq)
                            # check all conditions: attacks_directly, safe_slide, attack_slide
                            # if attacks directly and safe_slide: do move
                            # elif attacks directly and not safe_slide: do nothing
                            # elif not attacks_directly, but (safe_slide and attack_slide): do move
                            # elif not attacks_directly, and (not safe_slide or not attack_slide): do nothing
                            if (attacks_directly and safe_slide) or (not attacks_directly and safe_slide and attack_slide):
                                # do move
                                make_move(i, to_sq)
                                return True
            # check rest of main_board
            for i in range(59, 43, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        # don't need to check if moving into safety_zone
                        to_sq = (i + move_num) % 60
                        attacks_directly = False
                        # safe_slide defaults to True to limit options below
                        safe_slide = True
                        attack_slide = False
                        if self.model.main_board[to_sq].is_occupied():
                            if self.model.main_board[to_sq].get_color() != color:
                                # piece at to_sq is opponent: check if slide
                                attacks_directly = True
                        # check if slide
                        must_slide = is_slide(to_sq)
                        # check if safe_slide
                        if must_slide:
                            safe_slide = is_safe_slide(to_sq)
                            attack_slide = is_attack_slide(to_sq)
                        # check all conditions: attacks_directly, safe_slide, attack_slide
                        # if attacks directly and safe_slide: do move
                        # elif attacks directly and not safe_slide: do nothing
                        # elif not attacks_directly, but (safe_slide and attack_slide): do move
                        # elif not attacks_directly, and (not safe_slide or not attack_slide): do nothing
                        if (attacks_directly and safe_slide) or (not attacks_directly and safe_slide and attack_slide):
                            # do move
                            make_move(i, to_sq)
                            return True
        return False

    def slide_safely_strategy(self, color, move_num):
        """
        Does: checks if FORWARD move produces a safe slide
        Returns: True if move was completed
        """
        def is_safe_slide(start_sq, slide_length):
            # returns True if no player's pieces will be knocked off
            for j in range(1, slide_length):
                if self.model.main_board[(start_sq + j) % 60].is_occupied():
                    if self.model.main_board[(start_sq + j) % 60].get_color() == color:
                        return False
            return True
        def make_move(from_sq, to_sq):
            # makes move: from_sq to to_sq, check_slide
            self.model.move_piece(self.model.main_board, from_sq, self.model.main_board, to_sq)
            self.view.move_piece(self.view.main_board, from_sq, self.view.main_board, to_sq)
            self.check_slide(to_sq, color)
            self.display_all_starts()
            #print('{}: slide_safely_strategy'.format(color.capitalize()))
            
        if color == "yellow":
            for i in range(58, -1, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        # check if target square is beginning of slide
                        if (i + move_num) % 60 == 50:
                            if is_safe_slide(i, 5):
                                make_move(i, (i + move_num) % 60)
                                return True
                        elif (i + move_num) % 60 == 42:
                            if is_safe_slide(i, 4):
                                make_move(i, (i + move_num) % 60)
                                return True
                        elif (i + move_num) % 60 == 35:
                            if is_safe_slide(i, 5):
                                make_move(i, (i + move_num) % 60)
                                return True
                        elif (i + move_num) % 60 == 27:
                            if is_safe_slide(i, 4):
                                make_move(i, (i + move_num) % 60)
                                return True
                        elif (i + move_num) % 60 == 20:
                            if is_safe_slide(i, 5):
                                make_move(i, (i + move_num) % 60)
                                return True
                        elif (i + move_num) % 60 == 12:
                            if is_safe_slide(i, 4):
                                make_move(i, (i + move_num) % 60)
                                return True
            # don't need to check rest of main_board
        elif color == "green":
            for i in range(13, -1, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        # check if target square is beginning of slide
                        if (i + move_num) % 60 == 5:
                            if is_safe_slide(i, 5):
                                make_move(i, (i + move_num) % 60)
                                return True
                        elif (i + move_num) % 60 == 57:
                            if is_safe_slide(i, 4):
                                make_move(i, (i + move_num) % 60)
                                return True
                        elif (i + move_num) % 60 == 50:
                            if is_safe_slide(i, 5):
                                make_move(i, (i + move_num) % 60)
                                return True
                        elif (i + move_num) % 60 == 42:
                            if is_safe_slide(i, 4):
                                make_move(i, (i + move_num) % 60)
                                return True
                        elif (i + move_num) % 60 == 35:
                            if is_safe_slide(i, 5):
                                make_move(i, (i + move_num) % 60)
                                return True
                        elif (i + move_num) % 60 == 27:
                            if is_safe_slide(i, 4):
                                make_move(i, (i + move_num) % 60)
                                return True
            # check rest of main_board
            for i in range(59, 13, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        # check if target square is beginning of slide
                        if (i + move_num) % 60 == 5:
                            if is_safe_slide(i, 5):
                                make_move(i, (i + move_num) % 60)
                                return True
                        elif (i + move_num) % 60 == 57:
                            if is_safe_slide(i, 4):
                                make_move(i, (i + move_num) % 60)
                                return True
                        elif (i + move_num) % 60 == 50:
                            if is_safe_slide(i, 5):
                                make_move(i, (i + move_num) % 60)
                                return True
                        elif (i + move_num) % 60 == 42:
                            if is_safe_slide(i, 4):
                                make_move(i, (i + move_num) % 60)
                                return True
                        elif (i + move_num) % 60 == 35:
                            if is_safe_slide(i, 5):
                                make_move(i, (i + move_num) % 60)
                                return True
                        elif (i + move_num) % 60 == 27:
                            if is_safe_slide(i, 4):
                                make_move(i, (i + move_num) % 60)
                                return True
        elif color == "red":
            for i in range(28, -1, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        # check if target square is beginning of slide
                        if (i + move_num) % 60 == 20:
                            if is_safe_slide(i, 5):
                                make_move(i, (i + move_num) % 60)
                                return True
                        elif (i + move_num) % 60 == 12:
                            if is_safe_slide(i, 4):
                                make_move(i, (i + move_num) % 60)
                                return True
                        elif (i + move_num) % 60 == 5:
                            if is_safe_slide(i, 5):
                                make_move(i, (i + move_num) % 60)
                                return True
                        elif (i + move_num) % 60 == 57:
                            if is_safe_slide(i, 4):
                                make_move(i, (i + move_num) % 60)
                                return True
                        elif (i + move_num) % 60 == 50:
                            if is_safe_slide(i, 5):
                                make_move(i, (i + move_num) % 60)
                                return True
                        elif (i + move_num) % 60 == 42:
                            if is_safe_slide(i, 4):
                                make_move(i, (i + move_num) % 60)
                                return True
                        
            # check rest of main_board
            for i in range(59, 28, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        # check if target square is beginning of slide
                        if (i + move_num) % 60 == 20:
                            if is_safe_slide(i, 5):
                                make_move(i, (i + move_num) % 60)
                                return True
                        elif (i + move_num) % 60 == 12:
                            if is_safe_slide(i, 4):
                                make_move(i, (i + move_num) % 60)
                                return True
                        elif (i + move_num) % 60 == 5:
                            if is_safe_slide(i, 5):
                                make_move(i, (i + move_num) % 60)
                                return True
                        elif (i + move_num) % 60 == 57:
                            if is_safe_slide(i, 4):
                                make_move(i, (i + move_num) % 60)
                                return True
                        elif (i + move_num) % 60 == 50:
                            if is_safe_slide(i, 5):
                                make_move(i, (i + move_num) % 60)
                                return True
                        elif (i + move_num) % 60 == 42:
                            if is_safe_slide(i, 4):
                                make_move(i, (i + move_num) % 60)
                                return True
        elif color == "blue":
            for i in range(43, -1, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        # check if target square is beginning of slide
                        if (i + move_num) % 60 == 35:
                            if is_safe_slide(i, 5):
                                make_move(i, (i + move_num) % 60)
                                return True
                        elif (i + move_num) % 60 == 27:
                            if is_safe_slide(i, 4):
                                make_move(i, (i + move_num) % 60)
                                return True
                        elif (i + move_num) % 60 == 20:
                            if is_safe_slide(i, 5):
                                make_move(i, (i + move_num) % 60)
                                return True
                        elif (i + move_num) % 60 == 12:
                            if is_safe_slide(i, 4):
                                make_move(i, (i + move_num) % 60)
                                return True
                        elif (i + move_num) % 60 == 5:
                            if is_safe_slide(i, 5):
                                make_move(i, (i + move_num) % 60)
                                return True
                        elif (i + move_num) % 60 == 57:
                            if is_safe_slide(i, 4):
                                make_move(i, (i + move_num) % 60)
                                return True
            # check rest of main_board
            for i in range(59, 43, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        # check if target square is beginning of slide
                        if (i + move_num) % 60 == 35:
                            if is_safe_slide(i, 5):
                                make_move(i, (i + move_num) % 60)
                                return True
                        elif (i + move_num) % 60 == 27:
                            if is_safe_slide(i, 4):
                                make_move(i, (i + move_num) % 60)
                                return True
                        elif (i + move_num) % 60 == 20:
                            if is_safe_slide(i, 5):
                                make_move(i, (i + move_num) % 60)
                                return True
                        elif (i + move_num) % 60 == 12:
                            if is_safe_slide(i, 4):
                                make_move(i, (i + move_num) % 60)
                                return True
                        elif (i + move_num) % 60 == 5:
                            if is_safe_slide(i, 5):
                                make_move(i, (i + move_num) % 60)
                                return True
                        elif (i + move_num) % 60 == 57:
                            if is_safe_slide(i, 4):
                                make_move(i, (i + move_num) % 60)
                                return True
        return False

    def move_off_of_start_spots_strategy(self, color, move_num):
        """
        Does: checks all start spots, and makes move FORWARD
        Returns: True if move was completed
        """
        def helper_method(spot_arr):
            for num in spot_arr:
                if self.model.main_board[num].is_occupied():
                    if self.model.main_board[num].get_color() == color:
                        if self.check_legal_move(self.model.main_board, num, self.model.main_board,
                                                 num + move_num, color):
                            # move is legal
                            self.model.move_piece(self.model.main_board, num, self.model.main_board, num + move_num)
                            self.view.move_piece(self.view.main_board, num, self.view.main_board, num + move_num)
                            self.check_slide(num + move_num, color)
                            self.display_all_starts()
                            #print('{}: move_off_of_start_spots_strategy'.format(color.capitalize()))
                            return True
            return False
        if color == "yellow":
            spot_arr = [0, 45, 30, 15]
            return helper_method(spot_arr)
        elif color == "green":
            spot_arr = [15, 0, 45, 30]
            return helper_method(spot_arr)
        elif color == "red":
            spot_arr = [30, 15, 0, 45]
            return helper_method(spot_arr)
        elif color == "blue":
            spot_arr = [45, 30, 15, 0]
            return helper_method(spot_arr)
        return False

    def any_possible_forward_move_strategy(self, color, move_num):
        """
        Does: Makes first FORWARD move possible, moves piece move_num spaces
        Returns: True if move was completed
        """
        if color == "yellow":
            # check safety zone
            for i in range(4, -1, -1):
                # no need to check color here
                if self.model.yellow_safety[i].is_occupied():
                    if self.check_legal_move(self.model.yellow_safety, i, self.model.yellow_safety,
                                             i + move_num, color):
                        # move is legal
                        self.model.move_piece(self.model.yellow_safety, i, self.model.yellow_safety, i + move_num)
                        self.view.move_piece(self.view.yellow_safety, i, self.view.yellow_safety, i + move_num)
                        if i + move_num == 5:
                            self.check_win(color)
                        #print('{}: any_possible_forward_move_strategy'.format(color.capitalize()))
                        return True
            # check main_board
            for i in range(58, -1, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        # check if entering safety_zone
                        if i + move_num > 58:
                            # move enters safety_zone
                            to_sq = move_num - 1 - (58 - i)
                            if self.check_legal_move(self.model.main_board, i, self.model.yellow_safety, to_sq, color):
                                self.model.move_piece(self.model.main_board, i, self.model.yellow_safety, to_sq)
                                self.view.move_piece(self.view.main_board, i, self.view.yellow_safety, to_sq)
                                if to_sq == 5:
                                    self.check_win(color)
                                #print('{}: any_possible_forward_move_strategy'.format(color.capitalize()))
                                return True
                        else:
                            # move stays on main_board
                            to_sq = (i + move_num) % 60
                            if self.check_legal_move(self.model.main_board, i, self.model.main_board, to_sq, color):
                                self.model.move_piece(self.model.main_board, i, self.model.main_board, to_sq)
                                self.view.move_piece(self.view.main_board, i, self.view.main_board, to_sq)
                                self.check_slide(to_sq, color)
                                self.display_all_starts()
                                #print('{}: any_possible_forward_move_strategy'.format(color.capitalize()))
                                return True
            # check rest of main_board
            for i in range(59, 60, 1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        to_sq = (i + move_num) % 60
                        if self.check_legal_move(self.model.main_board, i, self.model.main_board, to_sq, color):
                            self.model.move_piece(self.model.main_board, i, self.model.main_board, to_sq)
                            self.view.move_piece(self.view.main_board, i, self.view.main_board, to_sq)
                            self.check_slide(to_sq, color)
                            self.display_all_starts()
                            #print('{}: any_possible_forward_move_strategy'.format(color.capitalize()))
                            return True
        elif color == "green":
            # check safety zone
            for i in range(4, -1, -1):
                # no need to check color here
                if self.model.green_safety[i].is_occupied():
                    if self.check_legal_move(self.model.green_safety, i, self.model.green_safety,
                                             i + move_num, color):
                        # move is legal
                        self.model.move_piece(self.model.green_safety, i, self.model.green_safety, i + move_num)
                        self.view.move_piece(self.view.green_safety, i, self.view.green_safety, i + move_num)
                        if i + move_num == 5:
                            self.check_win(color)
                        #print('{}: any_possible_forward_move_strategy'.format(color.capitalize()))
                        return True
            # check main_board
            for i in range(13, -1, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        # check if entering safety_zone
                        if i + move_num > 13:
                            # move enters safety_zone
                            to_sq = move_num - 1 - (13 - i)
                            if self.check_legal_move(self.model.main_board, i, self.model.green_safety, to_sq, color):
                                self.model.move_piece(self.model.main_board, i, self.model.green_safety, to_sq)
                                self.view.move_piece(self.view.main_board, i, self.view.green_safety, to_sq)
                                if to_sq == 5:
                                    self.check_win(color)
                                #print('{}: any_possible_forward_move_strategy'.format(color.capitalize()))
                                return True
                        else:
                            # move stays on main_board
                            to_sq = (i + move_num) % 60
                            if self.check_legal_move(self.model.main_board, i, self.model.main_board, to_sq, color):
                                self.model.move_piece(self.model.main_board, i, self.model.main_board, to_sq)
                                self.view.move_piece(self.view.main_board, i, self.view.main_board, to_sq)
                                self.check_slide(to_sq, color)
                                self.display_all_starts()
                                #print('{}: any_possible_forward_move_strategy'.format(color.capitalize()))
                                return True
            # check rest of main_board
            for i in range(59, 13, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        # move stays on main_board
                        to_sq = (i + move_num) % 60
                        if self.check_legal_move(self.model.main_board, i, self.model.main_board, to_sq, color):
                            self.model.move_piece(self.model.main_board, i, self.model.main_board, to_sq)
                            self.view.move_piece(self.view.main_board, i, self.view.main_board, to_sq)
                            self.check_slide(to_sq, color)
                            self.display_all_starts()
                            #print('{}: any_possible_forward_move_strategy'.format(color.capitalize()))
                            return True
        elif color == "red":
            # check safety zone
            for i in range(4, -1, -1):
                # no need to check color here
                if self.model.red_safety[i].is_occupied():
                    if self.check_legal_move(self.model.red_safety, i, self.model.red_safety,
                                             i + move_num, color):
                        # move is legal
                        self.model.move_piece(self.model.red_safety, i, self.model.red_safety, i + move_num)
                        self.view.move_piece(self.view.red_safety, i, self.view.red_safety, i + move_num)
                        if i + move_num == 5:
                            self.check_win(color)
                        #print('{}: any_possible_forward_move_strategy'.format(color.capitalize()))
                        return True
            # check main_board
            for i in range(28, -1, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        # check if entering safety_zone
                        if i + move_num > 28:
                            # move enters safety_zone
                            to_sq = move_num - 1 - (28 - i)
                            if self.check_legal_move(self.model.main_board, i, self.model.red_safety, to_sq, color):
                                self.model.move_piece(self.model.main_board, i, self.model.red_safety, to_sq)
                                self.view.move_piece(self.view.main_board, i, self.view.red_safety, to_sq)
                                if to_sq == 5:
                                    self.check_win(color)
                                #print('{}: any_possible_forward_move_strategy'.format(color.capitalize()))
                                return True
                        else:
                            # move stays on main_board
                            to_sq = (i + move_num) % 60
                            if self.check_legal_move(self.model.main_board, i, self.model.main_board, to_sq, color):
                                self.model.move_piece(self.model.main_board, i, self.model.main_board, to_sq)
                                self.view.move_piece(self.view.main_board, i, self.view.main_board, to_sq)
                                self.check_slide(to_sq, color)
                                self.display_all_starts()
                                #print('{}: any_possible_forward_move_strategy'.format(color.capitalize()))
                                return True
            # check rest of main_board
            for i in range(59, 28, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        # move stays on main_board
                        to_sq = (i + move_num) % 60
                        if self.check_legal_move(self.model.main_board, i, self.model.main_board, to_sq, color):
                            self.model.move_piece(self.model.main_board, i, self.model.main_board, to_sq)
                            self.view.move_piece(self.view.main_board, i, self.view.main_board, to_sq)
                            self.check_slide(to_sq, color)
                            self.display_all_starts()
                            #print('{}: any_possible_forward_move_strategy'.format(color.capitalize()))
                            return True
        elif color == "blue":
            # check safety zone
            for i in range(4, -1, -1):
                # no need to check color here
                if self.model.blue_safety[i].is_occupied():
                    if self.check_legal_move(self.model.blue_safety, i, self.model.blue_safety,
                                             i + move_num, color):
                        # move is legal
                        self.model.move_piece(self.model.blue_safety, i, self.model.blue_safety, i + move_num)
                        self.view.move_piece(self.view.blue_safety, i, self.view.blue_safety, i + move_num)
                        if i + move_num == 5:
                            self.check_win(color)
                        #print('{}: any_possible_forward_move_strategy'.format(color.capitalize()))
                        return True
            # check main_board
            for i in range(43, -1, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        # check if entering safety_zone
                        if i + move_num > 43:
                            # move enters safety_zone
                            to_sq = move_num - 1 - (43 - i)
                            if self.check_legal_move(self.model.main_board, i, self.model.blue_safety, to_sq, color):
                                self.model.move_piece(self.model.main_board, i, self.model.blue_safety, to_sq)
                                self.view.move_piece(self.view.main_board, i, self.view.blue_safety, to_sq)
                                if to_sq == 5:
                                    self.check_win(color)
                                #print('{}: any_possible_forward_move_strategy'.format(color.capitalize()))
                                return True
                        else:
                            # move stays on main_board
                            to_sq = (i + move_num) % 60
                            if self.check_legal_move(self.model.main_board, i, self.model.main_board, to_sq, color):
                                self.model.move_piece(self.model.main_board, i, self.model.main_board, to_sq)
                                self.view.move_piece(self.view.main_board, i, self.view.main_board, to_sq)
                                self.check_slide(to_sq, color)
                                self.display_all_starts()
                                #print('{}: any_possible_forward_move_strategy'.format(color.capitalize()))
                                return True
            # check rest of main_board
            for i in range(59, 43, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        # move stays on main_board
                        to_sq = (i + move_num) % 60
                        if self.check_legal_move(self.model.main_board, i, self.model.main_board, to_sq, color):
                            self.model.move_piece(self.model.main_board, i, self.model.main_board, to_sq)
                            self.view.move_piece(self.view.main_board, i, self.view.main_board, to_sq)
                            self.check_slide(to_sq, color)
                            self.display_all_starts()
                            #print('{}: any_possible_forward_move_strategy'.format(color.capitalize()))
                            return True
        return False

    def check_if_near_start_four_backward_move_strategy(self, color):
        """
        Does: checks spaces near start for BACKWARD FOUR move
        Returns: True if move executes
        """
        def make_move(from_sq, to_sq):
            self.model.move_piece(self.model.main_board, from_sq, self.model.main_board, to_sq)
            self.view.move_piece(self.view.main_board, from_sq, self.view.main_board, to_sq, False)
            self.check_slide(to_sq, color)
            self.display_all_starts()
            #print('{}: check_if_near_start_four_backward_move_strategy'.format(color.capitalize()))

        # method begins here
        if color == "yellow":
            arr = [59, 0, 1, 2, 3]
            for num in arr:
                if self.model.main_board[num].is_occupied():
                    if self.model.main_board[num].get_color() == color:
                        to_sq = (num + 60 - 4) % 60
                        if self.check_legal_move(self.model.main_board, num, self.model.main_board, to_sq, color):
                            make_move(num, to_sq)
                            return True
        elif color == "green":
            arr = [14, 15, 16, 17, 18]
            for num in arr:
                if self.model.main_board[num].is_occupied():
                    if self.model.main_board[num].get_color() == color:
                        to_sq = (num + 60 - 4) % 60
                        if self.check_legal_move(self.model.main_board, num, self.model.main_board, to_sq, color):
                            make_move(num, to_sq)
                            return True
        elif color == "red":
            arr = [29, 30, 31, 32, 33]
            for num in arr:
                if self.model.main_board[num].is_occupied():
                    if self.model.main_board[num].get_color() == color:
                        to_sq = (num + 60 - 4) % 60
                        if self.check_legal_move(self.model.main_board, num, self.model.main_board, to_sq, color):
                            make_move(num, to_sq)
                            return True
        elif color == "blue":
            arr = [44, 45, 46, 47, 48]
            for num in arr:
                if self.model.main_board[num].is_occupied():
                    if self.model.main_board[num].get_color() == color:
                        to_sq = (num + 60 - 4) % 60
                        if self.check_legal_move(self.model.main_board, num, self.model.main_board, to_sq, color):
                            make_move(num, to_sq)
                            return True
        return False
    
    def check_to_attack_opponent_backward_move_strategy(self, color, move_num):
        """
        Does: checks and executes backward move if attacks opponent, must check for safe_slide
        Input: move_num is saved as abs(move_num), so parameter can be -4, 4, -1, or 1: either sign does same move
        Returns: True if move was executed
        """
        move_num = abs(move_num)
        def is_safe_attack(from_list, from_sq, to_list, to_sq):
            # checks if attacks_directly, safe_slide, attack_slide
            # 'to_list' will always be main_board
            # returns True if move executes

            def make_move():
                self.model.move_piece(from_list, from_sq, to_list, to_sq)
                if from_list is self.model.yellow_safety:
                    self.view.move_piece(self.view.yellow_safety, from_sq, self.view.main_board, to_sq, False)
                elif from_list is self.model.green_safety:
                    self.view.move_piece(self.view.green_safety, from_sq, self.view.main_board, to_sq, False)
                elif from_list is self.model.red_safety:
                    self.view.move_piece(self.view.red_safety, from_sq, self.view.main_board, to_sq, False)
                elif from_list is self.model.blue_safety:
                    self.view.move_piece(self.view.blue_safety, from_sq, self.view.main_board, to_sq, False)
                else:
                    self.view.move_piece(self.view.main_board, from_sq, self.view.main_board, to_sq, False)
                self.check_slide(to_sq, color)
                self.display_all_starts()
                #print('{}: check_to_attack_opponent_backward_move_strategy'.format(color.capitalize()))

            # check if slide
            def is_slide(from_sq):
                # checks if from_sq is the start of a slide
                # Returns: True if is slide
                if from_sq == 57 and color != 'yellow':
                    return True
                elif from_sq == 5 and color != 'yellow':
                    return True
                elif from_sq == 12 and color != 'green':
                    return True
                elif from_sq == 20 and color != 'green':
                    return True
                elif from_sq == 27 and color != 'red':
                    return True
                elif from_sq == 35 and color != 'red':
                    return True
                elif from_sq == 42 and color != 'blue':
                    return True
                elif from_sq == 50 and color != 'blue':
                    return True
                return False

            # must check if SLIDING also attacks opponent
            def is_attack_slide(start_sq):
                def is_attack(from_sq2, slide_length):
                    for j in range(0, slide_length):
                        if self.model.main_board[(from_sq2 + j) % 60].is_occupied():
                            if self.model.main_board[(from_sq2 + j) % 60].get_color() != color:
                                return True
                    return False
                # check which slide and slide_length
                if start_sq == 5 and color != "yellow":
                    return is_attack(start_sq, 5)
                elif start_sq == 57 and color != "yellow":
                    return is_attack(start_sq, 4)
                elif start_sq == 50 and color != "blue":
                    return is_attack(start_sq, 5)
                elif start_sq == 42 and color != "blue":
                    return is_attack(start_sq, 4)
                elif start_sq == 35 and color != "red":
                    return is_attack(start_sq, 5)
                elif start_sq == 27 and color != "red":
                    return is_attack(start_sq, 4)
                elif start_sq == 20 and color != "green":
                    return is_attack(start_sq, 5)
                elif start_sq == 12 and color != "green":
                    return is_attack(start_sq, 4)
                return False
                
            # must also check if 'safe slide'
            def is_safe_slide(start_sq):
                def is_safe(from_sq2, slide_length):
                    for j in range(1, slide_length):
                        if (from_sq2 + j) % 60 != from_sq:
                            # the above check avoids the piece that's moving
                            if self.model.main_board[(from_sq2 + j) % 60].is_occupied():
                                if self.model.main_board[(from_sq2 + j) % 60].get_color() == color:
                                    return False
                    return True
                # check which slide and slide_length
                if start_sq == 5 and color != "yellow":
                    return is_safe(start_sq, 5)
                elif start_sq == 57 and color != "yellow":
                    return is_safe(start_sq, 4)
                elif start_sq == 50 and color != "blue":
                    return is_safe(start_sq, 5)
                elif start_sq == 42 and color != "blue":
                    return is_safe(start_sq, 4)
                elif start_sq == 35 and color != "red":
                    return is_safe(start_sq, 5)
                elif start_sq == 27 and color != "red":
                    return is_safe(start_sq, 4)
                elif start_sq == 20 and color != "green":
                    return is_safe(start_sq, 5)
                elif start_sq == 12 and color != "green":
                    return is_safe(start_sq, 4)
                return False

            # is_safe_attack body begins here
            attacks_directly = False
            safe_slide = True
            attack_slide = False
            # check if attacks_directly
            if to_list[to_sq].is_occupied():
                if to_list[to_sq].get_color() != color:
                    attacks_directly = True
            # check if slide
            must_slide = is_slide(to_sq)
            # check if safe_slide
            if must_slide:
                safe_slide = is_safe_slide(to_sq)
                attack_slide = is_attack_slide(to_sq)
            # check all conditions: attacks_directly, safe_slide, attack_slide
            if (attacks_directly and safe_slide) or (not attacks_directly and safe_slide and attack_slide):
                # do move
                make_move()
                return True
            return False
            
        # strategy body begins here
        if color == "yellow":
            for i in range(59, 60, 1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        to_sq = (i + 60 - move_num) % 60
                        if is_safe_attack(self.model.main_board, i, self.model.main_board, to_sq):
                            return True
            for i in range(0, 59, 1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        to_sq = (i + 60 - move_num) % 60
                        if is_safe_attack(self.model.main_board, i, self.model.main_board, to_sq):
                            return True
            for i in range(4, -1, -1):
                if self.model.yellow_safety[i].is_occupied():
                    # no need to check color in safety_zone
                    if i - move_num < 0:
                        to_sq = 58 + (i - move_num) + 1
                        if is_safe_attack(self.model.yellow_safety, i, self.model.main_board, to_sq):
                            return True
        elif color == "green":
            for i in range(14, 60, 1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        to_sq = (i + 60 - move_num) % 60
                        if is_safe_attack(self.model.main_board, i, self.model.main_board, to_sq):
                            return True
            for i in range(0, 14, 1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        to_sq = (i + 60 - move_num) % 60
                        if is_safe_attack(self.model.main_board, i, self.model.main_board, to_sq):
                            return True
            for i in range(4, -1, -1):
                if self.model.green_safety[i].is_occupied():
                    # no need to check color in safety_zone
                    if i - move_num < 0:
                        to_sq = 13 + (i - move_num) + 1
                        if is_safe_attack(self.model.green_safety, i, self.model.main_board, to_sq):
                            return True
        elif color == "red":
            for i in range(29, 60, 1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        to_sq = (i + 60 - move_num) % 60
                        if is_safe_attack(self.model.main_board, i, self.model.main_board, to_sq):
                            return True
            for i in range(0, 29, 1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        to_sq = (i + 60 - move_num) % 60
                        if is_safe_attack(self.model.main_board, i, self.model.main_board, to_sq):
                            return True
            for i in range(4, -1, -1):
                if self.model.red_safety[i].is_occupied():
                    # no need to check color in safety_zone
                    if i - move_num < 0:
                        to_sq = 28 + (i - move_num) + 1
                        if is_safe_attack(self.model.red_safety, i, self.model.main_board, to_sq):
                            return True
        elif color == "blue":
            for i in range(44, 60, 1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        to_sq = (i + 60 - move_num) % 60
                        if is_safe_attack(self.model.main_board, i, self.model.main_board, to_sq):
                            return True
            for i in range(0, 44, 1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        to_sq = (i + 60 - move_num) % 60
                        if is_safe_attack(self.model.main_board, i, self.model.main_board, to_sq):
                            return True
            for i in range(4, -1, -1):
                if self.model.blue_safety[i].is_occupied():
                    # no need to check color in safety_zone
                    if i - move_num < 0:
                        to_sq = 43 + (i - move_num) + 1
                        if is_safe_attack(self.model.blue_safety, i, self.model.main_board, to_sq):
                            return True
        return False
    
    def check_safe_slide_backward_move_strategy(self, color, move_num):
        """
        Does: checks and performs safe slide from a backward move
        Input: move_num is saved as abs(move_num), so parameter can be -4, 4, -1, or 1: either sign does same move
        Returns: True if move was executed
        """
        move_num = abs(move_num)

        def check_all_slides(from_sq, to_sq):
            # checks all possible slide starts
            # return True if move executes
            def make_move(from_sq, to_sq):
                self.model.move_piece(self.model.main_board, from_sq, self.model.main_board, to_sq)
                self.view.move_piece(self.view.main_board, from_sq, self.view.main_board, to_sq, False)
                self.check_slide(to_sq, color)
                self.display_all_starts()
                #print('{}: check_safe_slide_backward_move_strategy'.format(color.capitalize()))

            def is_safe_slide(from_sq, slide_length, avoid_index):
                # must avoid the index with the original piece that is moving
                for i in range(from_sq, from_sq + slide_length):
                    if i != avoid_index:
                        if self.model.main_board[i].is_occupied():
                            if self.model.main_board[i].get_color() == color:
                                return False
                return True
            
            # method starts here
            if to_sq == 50 and color != "blue":
                if is_safe_slide(to_sq, 5, from_sq):
                    make_move(from_sq, to_sq)
                    return True
            elif to_sq == 42 and color != "blue":
                if is_safe_slide(to_sq, 4, from_sq):
                    make_move(from_sq, to_sq)
                    return True
            elif to_sq == 35 and color != "red":
                if is_safe_slide(to_sq, 5, from_sq):
                    make_move(from_sq, to_sq)
                    return True
            elif to_sq == 27 and color != "red":
                if is_safe_slide(to_sq, 4, from_sq):
                    make_move(from_sq, to_sq)
                    return True
            elif to_sq == 20 and color != "green":
                if is_safe_slide(to_sq, 5, from_sq):
                    make_move(from_sq, to_sq)
                    return True
            elif to_sq == 12 and color != "green":
                if is_safe_slide(to_sq, 4, from_sq):
                    make_move(from_sq, to_sq)
                    return True
            elif to_sq == 5 and color != "yellow":
                if is_safe_slide(to_sq, 5, from_sq):
                    make_move(from_sq, to_sq)
                    return True
            elif to_sq == 57 and color != "yellow":
                if is_safe_slide(to_sq, 4, from_sq):
                    make_move(from_sq, to_sq)
                    return True
            return False

        if color == "yellow":
            for i in range(59, -1, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        to_sq = (i + 60 - move_num) % 60
                        if check_all_slides(i, to_sq):
                            return True
        elif color == "green":
            for i in range(14, -1, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        to_sq = (i + 60 - move_num) % 60
                        if check_all_slides(i, to_sq):
                            return True
            for i in range(59, 14, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        to_sq = (i + 60 - move_num) % 60
                        if check_all_slides(i, to_sq):
                            return True
        elif color == "red":
            for i in range(29, -1, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        to_sq = (i + 60 - move_num) % 60
                        if check_all_slides(i, to_sq):
                            return True
            for i in range(59, 29, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        to_sq = (i + 60 - move_num) % 60
                        if check_all_slides(i, to_sq):
                            return True
        elif color == "blue":
            for i in range(44, -1, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        to_sq = (i + 60 - move_num) % 60
                        if check_all_slides(i, to_sq):
                            return True
            for i in range(59, 44, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        to_sq = (i + 60 - move_num) % 60
                        if check_all_slides(i, to_sq):
                            return True
        return False
    
    def check_main_board_backward_move_strategy(self, color, move_num):
        """
        Does: checks and performs backward move on main_board (4 or 1)
        Input: move_num is saved as abs(move_num), so parameter can be -4, 4, -1, or 1: either sign does same move
        Returns: True if move was executed
        """
        move_num = abs(move_num)
        
        def make_move(from_sq, to_sq):
            self.model.move_piece(self.model.main_board, from_sq, self.model.main_board, to_sq)
            self.view.move_piece(self.view.main_board, from_sq, self.view.main_board, to_sq, False)
            self.check_slide(to_sq, color)
            self.display_all_starts()
            #print('{}: check_main_board_backward_move_strategy'.format(color.capitalize()))
            
        if color == "yellow":
            for i in range(59, 60, 1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        to_sq = (i + 60 - move_num) % 60
                        if self.check_legal_move(self.model.main_board, i, self.model.main_board, to_sq, color):
                            # do legal move
                            make_move(i, to_sq)
                            return True
            for i in range(0, 59, 1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        to_sq = (i + 60 - move_num) % 60
                        if self.check_legal_move(self.model.main_board, i, self.model.main_board, to_sq, color):
                            # do legal move
                            make_move(i, to_sq)
                            return True
        elif color == "green":
            for i in range(14, 60, 1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        to_sq = (i + 60 - move_num) % 60
                        if self.check_legal_move(self.model.main_board, i, self.model.main_board, to_sq, color):
                            # do legal move
                            make_move(i, to_sq)
                            return True
            for i in range(0, 14, 1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        to_sq = (i + 60 - move_num) % 60
                        if self.check_legal_move(self.model.main_board, i, self.model.main_board, to_sq, color):
                            # do legal move
                            make_move(i, to_sq)
                            return True
        elif color == "red":
            for i in range(29, 60, 1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        to_sq = (i + 60 - move_num) % 60
                        if self.check_legal_move(self.model.main_board, i, self.model.main_board, to_sq, color):
                            # do legal move
                            make_move(i, to_sq)
                            return True
            for i in range(0, 29, 1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        to_sq = (i + 60 - move_num) % 60
                        if self.check_legal_move(self.model.main_board, i, self.model.main_board, to_sq, color):
                            # do legal move
                            make_move(i, to_sq)
                            return True
        elif color == "blue":
            for i in range(44, 60, 1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        to_sq = (i + 60 - move_num) % 60
                        if self.check_legal_move(self.model.main_board, i, self.model.main_board, to_sq, color):
                            # do legal move
                            make_move(i, to_sq)
                            return True
            for i in range(0, 44, 1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        to_sq = (i + 60 - move_num) % 60
                        if self.check_legal_move(self.model.main_board, i, self.model.main_board, to_sq, color):
                            # do legal move
                            make_move(i, to_sq)
                            return True
        return False
    
    def check_safety_zone_backward_move_strategy(self, color, move_num):
        """
        Does: checks and performs backward move in safety_zone (4 or 1)
        Input: move_num is saved as abs(move_num), so parameter can be -4, 4, -1, or 1: either sign does same move
        Returns: True if move was executed
        """
        move_num = abs(move_num)
        
        if color == "yellow":
            # check each square in safety_zone for legal move
            for i in range(4, -1, -1):
                if self.model.yellow_safety[i].is_occupied():
                    # no need to check color of piece
                    if i - move_num < 0:
                        # piece enters main_board
                        to_sq = 58 + (i - move_num) + 1
                        if self.check_legal_move(self.model.yellow_safety, i, self.model.main_board, to_sq, color):
                            # legal move: execute
                            self.model.move_piece(self.model.yellow_safety, i, self.model.main_board, to_sq)
                            self.view.move_piece(self.view.yellow_safety, i, self.view.main_board, to_sq, False)
                            self.check_slide(to_sq, color)
                            self.display_all_starts()
                            #print('{}: check_safety_zone_backward_move_strategy'.format(color.capitalize()))
                            return True
                    else:
                        # piece stays in safety_zone
                        to_sq = i - move_num
                        if self.check_legal_move(self.model.yellow_safety, i, self.model.yellow_safety, to_sq, color):
                            # legal move: execute
                            self.model.move_piece(self.model.yellow_safety, i, self.model.yellow_safety, to_sq)
                            self.view.move_piece(self.view.yellow_safety, i, self.view.yellow_safety, to_sq, False)
                            #print('{}: check_safety_zone_backward_move_strategy'.format(color.capitalize()))
                            return True
        elif color == "green":
            # check each square in safety_zone for legal move
            for i in range(4, -1, -1):
                if self.model.green_safety[i].is_occupied():
                    # no need to check color of piece
                    if i - move_num < 0:
                        # piece enters main_board
                        to_sq = 13 + (i - move_num) + 1
                        if self.check_legal_move(self.model.green_safety, i, self.model.main_board, to_sq, color):
                            # legal move: execute
                            self.model.move_piece(self.model.green_safety, i, self.model.main_board, to_sq)
                            self.view.move_piece(self.view.green_safety, i, self.view.main_board, to_sq, False)
                            self.check_slide(to_sq, color)
                            self.display_all_starts()
                            #print('{}: check_safety_zone_backward_move_strategy'.format(color.capitalize()))
                            return True
                    else:
                        # piece stays in safety_zone
                        to_sq = i - move_num
                        if self.check_legal_move(self.model.green_safety, i, self.model.green_safety, to_sq, color):
                            # legal move: execute
                            self.model.move_piece(self.model.green_safety, i, self.model.green_safety, to_sq)
                            self.view.move_piece(self.view.green_safety, i, self.view.green_safety, to_sq, False)
                            #print('{}: check_safety_zone_backward_move_strategy'.format(color.capitalize()))
                            return True
        elif color == "red":
            # check each square in safety_zone for legal move
            for i in range(4, -1, -1):
                if self.model.red_safety[i].is_occupied():
                    # no need to check color of piece
                    if i - move_num < 0:
                        # piece enters main_board
                        to_sq = 28 + (i - move_num) + 1
                        if self.check_legal_move(self.model.red_safety, i, self.model.main_board, to_sq, color):
                            # legal move: execute
                            self.model.move_piece(self.model.red_safety, i, self.model.main_board, to_sq)
                            self.view.move_piece(self.view.red_safety, i, self.view.main_board, to_sq, False)
                            self.check_slide(to_sq, color)
                            self.display_all_starts()
                            #print('{}: check_safety_zone_backward_move_strategy'.format(color.capitalize()))
                            return True
                    else:
                        # piece stays in safety_zone
                        to_sq = i - move_num
                        if self.check_legal_move(self.model.red_safety, i, self.model.red_safety, to_sq, color):
                            # legal move: execute
                            self.model.move_piece(self.model.red_safety, i, self.model.red_safety, to_sq)
                            self.view.move_piece(self.view.red_safety, i, self.view.red_safety, to_sq, False)
                            #print('{}: check_safety_zone_backward_move_strategy'.format(color.capitalize()))
                            return True
        elif color == "blue":
            # check each square in safety_zone for legal move
            for i in range(4, -1, -1):
                if self.model.blue_safety[i].is_occupied():
                    # no need to check color of piece
                    if i - move_num < 0:
                        # piece enters main_board
                        to_sq = 43 + (i - move_num) + 1
                        if self.check_legal_move(self.model.blue_safety, i, self.model.main_board, to_sq, color):
                            # legal move: execute
                            self.model.move_piece(self.model.blue_safety, i, self.model.main_board, to_sq)
                            self.view.move_piece(self.view.blue_safety, i, self.view.main_board, to_sq, False)
                            self.check_slide(to_sq, color)
                            self.display_all_starts()
                            #print('{}: check_safety_zone_backward_move_strategy'.format(color.capitalize()))
                            return True
                    else:
                        # piece stays in safety_zone
                        to_sq = i - move_num
                        if self.check_legal_move(self.model.blue_safety, i, self.model.blue_safety, to_sq, color):
                            # legal move: execute
                            self.model.move_piece(self.model.blue_safety, i, self.model.blue_safety, to_sq)
                            self.view.move_piece(self.view.blue_safety, i, self.view.blue_safety, to_sq, False)
                            #print('{}: check_safety_zone_backward_move_strategy'.format(color.capitalize()))
                            return True
        return False

    def check_move_off_of_start_spots_backward_move_strategy(self, color, move_num):
        """
        Does: checks all start spots and does backward move
        Input: move_num is saved as abs(move_num) so input can be 1 or -1, etc., both do same backward move
        Returns: True if move is executed
        """
        move_num = abs(move_num)

        def make_move(from_sq, to_sq):
            self.model.move_piece(self.model.main_board, from_sq, self.model.main_board, to_sq)
            self.view.move_piece(self.view.main_board, from_sq, self.view.main_board, to_sq, False)
            self.check_slide(to_sq, color)
            self.display_all_starts()
            #print('{}: check_move_off_of_start_spots_backward_move_strategy'.format(color.capitalize()))
        # method body begins here
        if color == "yellow":
            arr = [15, 30, 45]
            for num in arr:
                if self.model.main_board[num].is_occupied():
                    if self.model.main_board[num].get_color() == color:
                        to_sq = (num + 60 - move_num) % 60
                        if self.check_legal_move(self.model.main_board, num, self.model.main_board, to_sq, color):
                            # backward move is legal: execute
                            make_move(num, to_sq)
                            return True
        elif color == "green":
            arr = [30, 45, 0]
            for num in arr:
                if self.model.main_board[num].is_occupied():
                    if self.model.main_board[num].get_color() == color:
                        to_sq = (num + 60 - move_num) % 60
                        if self.check_legal_move(self.model.main_board, num, self.model.main_board, to_sq, color):
                            # backward move is legal: execute
                            make_move(num, to_sq)
                            return True
        elif color == "red":
            arr = [45, 0, 15]
            for num in arr:
                if self.model.main_board[num].is_occupied():
                    if self.model.main_board[num].get_color() == color:
                        to_sq = (num + 60 - move_num) % 60
                        if self.check_legal_move(self.model.main_board, num, self.model.main_board, to_sq, color):
                            # backward move is legal: execute
                            make_move(num, to_sq)
                            return True
        elif color == "blue":
            arr = [0, 15, 30]
            for num in arr:
                if self.model.main_board[num].is_occupied():
                    if self.model.main_board[num].get_color() == color:
                        to_sq = (num + 60 - move_num) % 60
                        if self.check_legal_move(self.model.main_board, num, self.model.main_board, to_sq, color):
                            # backward move is legal: execute
                            make_move(num, to_sq)
                            return True
        return False
    
    def check_if_near_start_backward_move_one_strategy(self, color):
        """
        Does: checks 2 spots near color's start for backward move of one
        Returns: True if move is executed
        """
        def make_move(from_sq, to_sq):
            self.model.move_piece(self.model.main_board, from_sq, self.model.main_board, to_sq)
            self.view.move_piece(self.view.main_board, from_sq, self.view.main_board, to_sq, False)
            self.check_slide(to_sq, color)
            self.display_all_starts()
            #print('{}: check_if_near_start_backward_move_one_strategy'.format(color.capitalize()))
            
        # method body begins here
        if color == "yellow":
            arr = [59, 0]
            for num in arr:
                if self.model.main_board[num].is_occupied():
                    if self.model.main_board[num].get_color() == color:
                        to_sq = (num + 60 - 1) % 60
                        if self.check_legal_move(self.model.main_board, num, self.model.main_board, to_sq, color):
                            # move is legal: execute
                            make_move(num, to_sq)
                            return True
        elif color == "green":
            arr = [14, 15]
            for num in arr:
                if self.model.main_board[num].is_occupied():
                    if self.model.main_board[num].get_color() == color:
                        to_sq = (num + 60 - 1) % 60
                        if self.check_legal_move(self.model.main_board, num, self.model.main_board, to_sq, color):
                            # move is legal: execute
                            make_move(num, to_sq)
                            return True
        elif color == "red":
            arr = [29, 30]
            for num in arr:
                if self.model.main_board[num].is_occupied():
                    if self.model.main_board[num].get_color() == color:
                        to_sq = (num + 60 - 1) % 60
                        if self.check_legal_move(self.model.main_board, num, self.model.main_board, to_sq, color):
                            # move is legal: execute
                            make_move(num, to_sq)
                            return True
        elif color == "blue":
            arr = [44, 45]
            for num in arr:
                if self.model.main_board[num].is_occupied():
                    if self.model.main_board[num].get_color() == color:
                        to_sq = (num + 60 - 1) % 60
                        if self.check_legal_move(self.model.main_board, num, self.model.main_board, to_sq, color):
                            # move is legal: execute
                            make_move(num, to_sq)
                            return True
        return False

    def attack_opponent_nearest_home_sorry_strategy(self, color):
        """
        Does: attacks opponent nearest player's home
        Returns: True if move executed
        """
        if color == "yellow":
            arr = []
            for i in range(58, -1, -1):
                arr.append(i)
            for i in range(59, 58, -1):
                arr.append(i)
            for num in arr:
                if self.model.main_board[num].is_occupied():
                    if self.model.main_board[num].get_color() != color:
                        # attack opponent at num
                        self.model.move_piece_from_start(self.model.yellow_start, num)
                        self.view.move_piece_from_start(self.view.yellow_start, num)
                        self.check_slide(num, color)
                        self.display_all_starts()
                        #print('{}: attack_opponent_nearest_home_sorry_strategy'.format(color.capitalize()))
                        return True
        elif color == "green":
            arr = []
            for i in range(13, -1, -1):
                arr.append(i)
            for i in range(59, 13, -1):
                arr.append(i)
            for num in arr:
                if self.model.main_board[num].is_occupied():
                    if self.model.main_board[num].get_color() != color:
                        # attack opponent at num
                        self.model.move_piece_from_start(self.model.green_start, num)
                        self.view.move_piece_from_start(self.view.green_start, num)
                        self.check_slide(num, color)
                        self.display_all_starts()
                        #print('{}: attack_opponent_nearest_home_sorry_strategy'.format(color.capitalize()))
                        return True
        elif color == "red":
            arr = []
            for i in range(28, -1, -1):
                arr.append(i)
            for i in range(59, 28, -1):
                arr.append(i)
            for num in arr:
                if self.model.main_board[num].is_occupied():
                    if self.model.main_board[num].get_color() != color:
                        # attack opponent at num
                        self.model.move_piece_from_start(self.model.red_start, num)
                        self.view.move_piece_from_start(self.view.red_start, num)
                        self.check_slide(num, color)
                        self.display_all_starts()
                        #print('{}: attack_opponent_nearest_home_sorry_strategy'.format(color.capitalize()))
                        return True
        elif color == "blue":
            arr = []
            for i in range(43, -1, -1):
                arr.append(i)
            for i in range(59, 43, -1):
                arr.append(i)
            for num in arr:
                if self.model.main_board[num].is_occupied():
                    if self.model.main_board[num].get_color() != color:
                        # attack opponent at num
                        self.model.move_piece_from_start(self.model.blue_start, num)
                        self.view.move_piece_from_start(self.view.blue_start, num)
                        self.check_slide(num, color)
                        self.display_all_starts()
                        #print('{}: attack_opponent_nearest_home_sorry_strategy'.format(color.capitalize()))
                        return True
        return False

    def attack_multiple_men_with_slide_sorry_strategy(self, color):
        """
        Does: looks for and performs a slide move that attacks 2 or more opponents
        Returns: True if move executes
        """
        def make_move(to_sq):
            if color == "yellow":
                self.model.move_piece_from_start(self.model.yellow_start, to_sq)
                self.view.move_piece_from_start(self.view.yellow_start, to_sq)
                self.check_slide(to_sq, color)
                self.display_all_starts()
            elif color == "green":
                self.model.move_piece_from_start(self.model.green_start, to_sq)
                self.view.move_piece_from_start(self.view.green_start, to_sq)
                self.check_slide(to_sq, color)
                self.display_all_starts()
            elif color == "red":
                self.model.move_piece_from_start(self.model.red_start, to_sq)
                self.view.move_piece_from_start(self.view.red_start, to_sq)
                self.check_slide(to_sq, color)
                self.display_all_starts()
            elif color == "blue":
                self.model.move_piece_from_start(self.model.blue_start, to_sq)
                self.view.move_piece_from_start(self.view.blue_start, to_sq)
                self.check_slide(to_sq, color)
                self.display_all_starts()
            #print('{}: attack_multiple_men_with_slide_sorry_strategy'.format(color.capitalize()))
            
        # method body begins here
        arr = [[57, 4],[5, 5],[12, 4],[20, 5],[27, 4],[35, 5],[42, 4],[50, 5]]
        for i in range(len(arr)):
            num_attacked = 0
            if self.model.main_board[arr[i][0]].is_occupied():
                if self.model.main_board[arr[i][0]].get_color() != color:
                    num_attacked += 1
                    # check entire slide for another opponent
                    for j in range(arr[i][0] + 1, arr[i][0] + arr[i][1]):
                        if self.model.main_board[j % 60].is_occupied():
                            if self.model.main_board[j % 60].get_color() != color:
                                num_attacked += 1
                    # if 2 or more attacked, do move
                    if num_attacked > 1:
                        make_move(arr[i][0])
                        return True
        return False

    def make_good_trade_strategy(self, color):
        """
        Does: determines if a beneficial trade is present and completes trade
        Returns: True if trade is executed
        """
        def make_trade(from_sq, to_sq, color_to_sq):
            self.model.trade_pieces(from_sq, to_sq)
            self.view.trade_pieces(from_sq, to_sq)
            # pieces have switched so switch color also
            self.check_slide(to_sq, color)
            self.check_slide(from_sq, color_to_sq)
            self.display_all_starts()
            #print('{}: make_good_trade_strategy'.format(color.capitalize()))
            
        if color == "yellow":
            player_pieces = []
            opponent_pieces = []
            # find all positions of player pieces
            for i in range(59, 60, 1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        player_pieces.append(i)
            for i in range(0, 59, 1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        player_pieces.append(i)
            # find all positions of opponent pieces except one
            for i in range(58, -1, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() != color:
                        opponent_pieces.append(i)
            # we do not want to trade into space 59
            # check possible trades: trade advances piece more than 11 spaces forward
            for i in player_pieces:
                for j in opponent_pieces:
                    if 58 >= i >= 54:
                        # player is too close to home for forward move: can trade if opponent in range
                        if i < j <= 58:
                            # opponent in range
                            make_trade(i, j, self.model.main_board[j].get_color())
                            return True
                    else:
                        # player is far away from home: look for trade
                        if j > i + 11:
                            # opponent in range
                            make_trade(i, j, self.model.main_board[j].get_color())
                            return True
        elif color == "green":
            player_pieces = []
            opponent_pieces = []
            # find all positions of player pieces
            for i in range(14, 60, 1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        player_pieces.append(i)
            for i in range(0, 14, 1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        player_pieces.append(i)
            # find all positions of opponent pieces except one
            for i in range(13, -1, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() != color:
                        opponent_pieces.append(i)
            # we do not want to trade into space 14
            for i in range(59, 14, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() != color:
                        opponent_pieces.append(i)
            # check possible trades: trade advances piece more than 11 spaces forward
            for i in player_pieces:
                for j in opponent_pieces:
                    if 13 >= i >= 9:
                        # player is too close to home for forward move: can trade if opponent in range
                        if i < j <= 13:
                            # opponent in range
                            make_trade(i, j, self.model.main_board[j].get_color())
                            return True
                    else:
                        # player is far away from home: look for trade
                        if i >= 14:
                            if i + 11 < j or (i + 11)%60 < j <= 13 or (0 <= j <= 10 and (j - 11 + 60)%60 > i) or \
                               (11 <= j <= 13):
                                # opponent in range
                                make_trade(i, j, self.model.main_board[j].get_color())
                                return True
                        else:
                            if i + 11 < j <= 13:
                                #opponent in range
                                make_trade(i, j, self.model.main_board[j].get_color())
                                return True
                        
        elif color == "red":
            player_pieces = []
            opponent_pieces = []
            # find all positions of player pieces
            for i in range(29, 60, 1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        player_pieces.append(i)
            for i in range(0, 29, 1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        player_pieces.append(i)
            # find all positions of opponent pieces except one
            for i in range(28, -1, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() != color:
                        opponent_pieces.append(i)
            # we do not want to trade into space 29
            for i in range(59, 29, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() != color:
                        opponent_pieces.append(i)
            # check possible trades: trade advances piece more than 11 spaces forward
            for i in player_pieces:
                for j in opponent_pieces:
                    if 28 >= i >= 24:
                        # player is too close to home for forward move: can trade if opponent in range
                        if i < j <= 28:
                            # opponent in range
                            make_trade(i, j, self.model.main_board[j].get_color())
                            return True
                    else:
                        # player is far away from home: look for trade
                        if i >= 29:
                            if i + 11 < j or (i + 11)%60 < j <= 28 or (0 <= j <= 10 and (j - 11 + 60)%60 > i) or \
                               (11 <= j <= 28):
                                # opponent in range
                                make_trade(i, j, self.model.main_board[j].get_color())
                                return True
                        else:
                            if i + 11 < j <= 28:
                                #opponent in range
                                make_trade(i, j, self.model.main_board[j].get_color())
                                return True
        elif color == "blue":
            player_pieces = []
            opponent_pieces = []
            # find all positions of player pieces
            for i in range(44, 60, 1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        player_pieces.append(i)
            for i in range(0, 44, 1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        player_pieces.append(i)
            # find all positions of opponent pieces except one
            for i in range(43, -1, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() != color:
                        opponent_pieces.append(i)
            # we do not want to trade into space 44
            for i in range(59, 44, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() != color:
                        opponent_pieces.append(i)
            # check possible trades: trade advances piece more than 11 spaces forward
            for i in player_pieces:
                for j in opponent_pieces:
                    if 43 >= i >= 39:
                        # player is too close to home for forward move: can trade if opponent in range
                        if i < j <= 43:
                            # opponent in range
                            make_trade(i, j, self.model.main_board[j].get_color())
                            return True
                    else:
                        # player is far away from home: look for trade
                        if i >= 44:
                            if i + 11 < j or (i + 11)%60 < j <= 43 or (0 <= j <= 10 and (j - 11 + 60)%60 > i) or \
                                (11 <= j <= 43):
                                # opponent in range
                                make_trade(i, j, self.model.main_board[j].get_color())
                                return True
                        else:
                            if i + 11 < j <= 43:
                                #opponent in range
                                make_trade(i, j, self.model.main_board[j].get_color())
                                return True
        return False

    def split_get_one_piece_home_strategy(self, color):
        """
        Does: finds split move that moves on piece home, other piece makes legal move and/or slides safely
        Returns: True if moves execute
        """
        def make_move(p1_from_block, p1_target_block, p2_from_block, p2_target_block):
            # makes both moves
            # p1 blocks can't be same, p2 blocks can't be same
            p1_from_list_model, p1_from_sq_model = self.get_list_and_square_from_model(p1_from_block)
            p1_to_list_model, p1_to_sq_model = self.get_list_and_square_from_model(p1_target_block)
            p1_from_list_view, p1_from_sq_view = self.get_list_and_square_from_view(p1_from_block)
            p1_to_list_view, p1_to_sq_view = self.get_list_and_square_from_view(p1_target_block)
            p2_from_list_model, p2_from_sq_model = self.get_list_and_square_from_model(p2_from_block)
            p2_to_list_model, p2_to_sq_model = self.get_list_and_square_from_model(p2_target_block)
            p2_from_list_view, p2_from_sq_view = self.get_list_and_square_from_view(p2_from_block)
            p2_to_list_view, p2_to_sq_view = self.get_list_and_square_from_view(p2_target_block)

            self.model.move_piece(p1_from_list_model, p1_from_sq_model, p1_to_list_model, p1_to_sq_model)
            self.view.move_piece(p1_from_list_view, p1_from_sq_view, p1_to_list_view, p1_to_sq_view)
            if p1_to_list_model is self.model.main_board:
                self.check_slide(p1_to_sq_view, color)
            self.display_all_starts()

            self.model.move_piece(p2_from_list_model, p2_from_sq_model, p2_to_list_model, p2_to_sq_model)
            self.view.move_piece(p2_from_list_view, p2_from_sq_view, p2_to_list_view, p2_to_sq_view)
            if p2_to_list_model is self.model.main_board:
                self.check_slide(p2_to_sq_view, color)
            self.display_all_starts()
            #print('{}: split_get_one_piece_home_strategy'.format(color.capitalize()))
            
        # body of method begins here
        # we don't need to check for safe_slide here: because of the order of pieces
        # the unsafe slide will never happen
        player_pieces = self.get_player_pieces(color)
        for i in range(len(player_pieces) - 1):
            for j in range(i + 1, len(player_pieces)):
                m = 6
                p1_legal = False
                p2_legal = False
                p1_goes_home = False
                while (m >= 1) and not(p1_legal and p2_legal and p1_goes_home):
                    p1_legal = False
                    p2_legal = False
                    p1_goes_home = False
                    n = 7 - m
                    p1_target = self.find_real_target(player_pieces[i], m, color)
                    if p1_target != -1:
                        zone, sq = self.get_list_and_square_from_model(p1_target)
                        # check if legal move, target does not have color or is_home
                        if zone[sq].is_home():
                            # legal and p1_goes_home
                            p1_legal = True
                            p1_goes_home = True
                        elif zone[sq].is_occupied():
                            if zone[sq].get_color() != color:
                                # legal move
                                p1_legal = True
                        else:
                            # unoccupied: legal move
                            p1_legal = True
                        # continue if p1_legal and goes_home
                        if p1_legal and p1_goes_home:
                            p2_target = self.find_real_target(player_pieces[j], n, color)
                            # check if p2_legal
                            if p2_target != -1:
                                zone, sq = self.get_list_and_square_from_model(p2_target)
                                if zone[sq].is_home():
                                    # legal move
                                    p2_legal = True
                                elif zone[sq].is_occupied():
                                    if zone[sq].get_color() != color:
                                        # legal move
                                        p2_legal = True
                                else:
                                    # unoccupied: legal_move
                                    p2_legal = True
                    if not (p1_legal and p2_legal and p1_goes_home):
                        m -= 1
                # end of while loop: if m > 0 do move
                if m > 0:
                    make_move(player_pieces[i], p1_target, player_pieces[j], p2_target)
                    return True
        return False
    
    def split_attack_opponent_strategy(self, color):
        """
        Does: finds a split move where at least one piece ATTACKS DIRECTLY
        or with SLIDE ATTACK
        Returns: True if move was executed
        """
        def make_move(p1_from_block, p1_target_block, p2_from_block, p2_target_block):
            # makes both moves
            # p1 blocks can't be same, p2 blocks can't be same
            p1_from_list_model, p1_from_sq_model = self.get_list_and_square_from_model(p1_from_block)
            p1_to_list_model, p1_to_sq_model = self.get_list_and_square_from_model(p1_target_block)
            p1_from_list_view, p1_from_sq_view = self.get_list_and_square_from_view(p1_from_block)
            p1_to_list_view, p1_to_sq_view = self.get_list_and_square_from_view(p1_target_block)
            p2_from_list_model, p2_from_sq_model = self.get_list_and_square_from_model(p2_from_block)
            p2_to_list_model, p2_to_sq_model = self.get_list_and_square_from_model(p2_target_block)
            p2_from_list_view, p2_from_sq_view = self.get_list_and_square_from_view(p2_from_block)
            p2_to_list_view, p2_to_sq_view = self.get_list_and_square_from_view(p2_target_block)

            self.model.move_piece(p1_from_list_model, p1_from_sq_model, p1_to_list_model, p1_to_sq_model)
            self.view.move_piece(p1_from_list_view, p1_from_sq_view, p1_to_list_view, p1_to_sq_view)
            if p1_to_list_model is self.model.main_board:
                self.check_slide(p1_to_sq_view, color)
            self.display_all_starts()

            self.model.move_piece(p2_from_list_model, p2_from_sq_model, p2_to_list_model, p2_to_sq_model)
            self.view.move_piece(p2_from_list_view, p2_from_sq_view, p2_to_list_view, p2_to_sq_view)
            if p2_to_list_model is self.model.main_board:
                self.check_slide(p2_to_sq_view, color)
            self.display_all_starts()
            #print('{}: split_attack_opponent_strategy'.format(color.capitalize()))
            
        # check if slide
        def is_slide(from_block):
            # checks if from_sq is the start of a slide
            # Returns: True if is slide
            if from_block == 57 and color != 'yellow':
                return True
            elif from_block == 5 and color != 'yellow':
                return True
            elif from_block == 12 and color != 'green':
                return True
            elif from_block == 20 and color != 'green':
                return True
            elif from_block == 27 and color != 'red':
                return True
            elif from_block == 35 and color != 'red':
                return True
            elif from_block == 42 and color != 'blue':
                return True
            elif from_block == 50 and color != 'blue':
                return True
            return False
            
        # check if 'safe slide'
        def is_safe_slide(start_block, include, exclude):
            # if not excluding a piece, enter exclude = -1
            # include is for BLOCK where first piece will land
            def is_safe(from_sq2, slide_length):
                for j in range(1, slide_length):
                    if (from_sq2 + j) % 60 != exclude:
                        # the above check avoids the first piece that's moving
                        if (from_sq2 + j) % 60 == include:
                            # first piece will move here, return False
                            return False
                        if self.model.main_board[(from_sq2 + j) % 60].is_occupied():
                            if self.model.main_board[(from_sq2 + j) % 60].get_color() == color:
                                return False
                return True
            # check which slide and slide_length
            if start_block == 5 and color != "yellow":
                return is_safe(start_block, 5)
            elif start_block == 57 and color != "yellow":
                return is_safe(start_block, 4)
            elif start_block == 50 and color != "blue":
                return is_safe(start_block, 5)
            elif start_block == 42 and color != "blue":
                return is_safe(start_block, 4)
            elif start_block == 35 and color != "red":
                return is_safe(start_block, 5)
            elif start_block == 27 and color != "red":
                return is_safe(start_block, 4)
            elif start_block == 20 and color != "green":
                return is_safe(start_block, 5)
            elif start_block == 12 and color != "green":
                return is_safe(start_block, 4)
            return False
        
        # must check if SLIDING also attacks opponent
        def is_attack_slide(start_block):
            def is_attack(from_block, slide_length):
                for j in range(0, slide_length):
                    if self.model.main_board[(from_block + j) % 60].is_occupied():
                        if self.model.main_board[(from_block + j) % 60].get_color() != color:
                            return True
                return False
            # check which slide and slide_length
            if start_block == 5 and color != "yellow":
                return is_attack(start_block, 5)
            elif start_block == 57 and color != "yellow":
                return is_attack(start_block, 4)
            elif start_block == 50 and color != "blue":
                return is_attack(start_block, 5)
            elif start_block == 42 and color != "blue":
                return is_attack(start_block, 4)
            elif start_block == 35 and color != "red":
                return is_attack(start_block, 5)
            elif start_block == 27 and color != "red":
                return is_attack(start_block, 4)
            elif start_block == 20 and color != "green":
                return is_attack(start_block, 5)
            elif start_block == 12 and color != "green":
                return is_attack(start_block, 4)
            return False

        # body of method begins here
        player_pieces = self.get_player_pieces(color)
        for i in range(len(player_pieces) - 1):
            for j in range(i + 1, len(player_pieces)):
                m = 1
                p1_legal = False
                p2_legal = False
                p1_attacks_directly = False
                p2_attacks_directly = False
                p1_attack_slide = False
                p2_attack_slide = False
                while (m <= 6) and not ((p1_legal and p2_legal) and (p1_attacks_directly or p2_attacks_directly
                                        or p1_attack_slide or p2_attack_slide)):
                    p1_legal = False
                    p2_legal = False
                    p1_attacks_directly = False
                    p2_attacks_directly = False
                    p1_attack_slide = False
                    p2_attack_slide = False
                    n = 7 - m
                    p1_target = self.find_real_target(player_pieces[i], m, color)
                    if p1_target != -1:
                        zone, sq = self.get_list_and_square_from_model(p1_target)
                        # check if legal move, target does not have color
                        if zone[sq].is_occupied():
                            if zone[sq].get_color() != color:
                                # legal move and attacks_directly
                                p1_legal = True
                                p1_attacks_directly = True
                        else:
                            # unoccupied: legal move
                            p1_legal = True
                        # continue if p1_legal
                        if p1_legal:
                            if is_slide(p1_target):
                                if is_safe_slide(p1_target, -1, -1):
                                    p1_attack_slide = is_attack_slide(p1_target)
                            # continue with piece2
                            p2_target = self.find_real_target(player_pieces[j], n, color)
                            if p2_target != -1 and p2_target != p1_target:
                                zone, sq = self.get_list_and_square_from_model(p2_target)
                                # check if legal move, target does not have color
                                if p2_target == player_pieces[i]:
                                    # legal move
                                    p2_legal = True
                                elif zone[sq].is_occupied():
                                    if zone[sq].get_color() != color:
                                        # legal move and attacks_directly
                                        p2_legal = True
                                        p2_attacks_directly = True
                                else:
                                    # unoccupied: legal move
                                    p2_legal = True
                                # continue if p2_legal
                                if p2_legal:
                                    if is_slide(p2_target):
                                        if is_safe_slide(p2_target,
                                                self.find_target_block(player_pieces[i], m, -1, color),
                                                player_pieces[i]):
                                            p2_attack_slide = is_attack_slide(p2_target)
                    if not ((p1_legal and p2_legal) and (p1_attacks_directly or p2_attacks_directly
                                        or p1_attack_slide or p2_attack_slide)):
                        m += 1
                # exit while loop: move is attack if m < 7
                if m < 7:
                    #print(player_pieces[i])
                    #print(p1_target)
                    #print(player_pieces[j])
                    #print(p2_target)
                    make_move(player_pieces[i], p1_target, player_pieces[j], p2_target)
                    return True
        return False
    
    def split_slide_safely_strategy(self, color):
        """
        Does: tries to find split move for safe_slide (does not include forward move of 7)
        Returns: True if move executes
        """
        def make_move(p1_from_block, p1_target_block, p2_from_block, p2_target_block):
            # makes both moves
            # p1 blocks can't be same, p2 blocks can't be same
            p1_from_list_model, p1_from_sq_model = self.get_list_and_square_from_model(p1_from_block)
            p1_to_list_model, p1_to_sq_model = self.get_list_and_square_from_model(p1_target_block)
            p1_from_list_view, p1_from_sq_view = self.get_list_and_square_from_view(p1_from_block)
            p1_to_list_view, p1_to_sq_view = self.get_list_and_square_from_view(p1_target_block)
            p2_from_list_model, p2_from_sq_model = self.get_list_and_square_from_model(p2_from_block)
            p2_to_list_model, p2_to_sq_model = self.get_list_and_square_from_model(p2_target_block)
            p2_from_list_view, p2_from_sq_view = self.get_list_and_square_from_view(p2_from_block)
            p2_to_list_view, p2_to_sq_view = self.get_list_and_square_from_view(p2_target_block)

            self.model.move_piece(p1_from_list_model, p1_from_sq_model, p1_to_list_model, p1_to_sq_model)
            self.view.move_piece(p1_from_list_view, p1_from_sq_view, p1_to_list_view, p1_to_sq_view)
            if p1_to_list_model is self.model.main_board:
                self.check_slide(p1_to_sq_view, color)
            self.display_all_starts()

            self.model.move_piece(p2_from_list_model, p2_from_sq_model, p2_to_list_model, p2_to_sq_model)
            self.view.move_piece(p2_from_list_view, p2_from_sq_view, p2_to_list_view, p2_to_sq_view)
            if p2_to_list_model is self.model.main_board:
                self.check_slide(p2_to_sq_view, color)
            self.display_all_starts()
            #print('{}: split_slide_safely_strategy'.format(color.capitalize()))
            
        # check if slide
        def is_slide(from_block):
            # checks if from_sq is the start of a slide
            # Returns: True if is slide
            if from_block == 57 and color != 'yellow':
                return True
            elif from_block == 5 and color != 'yellow':
                return True
            elif from_block == 12 and color != 'green':
                return True
            elif from_block == 20 and color != 'green':
                return True
            elif from_block == 27 and color != 'red':
                return True
            elif from_block == 35 and color != 'red':
                return True
            elif from_block == 42 and color != 'blue':
                return True
            elif from_block == 50 and color != 'blue':
                return True
            return False
            
        # check if 'safe slide'
        def is_safe_slide(start_block, include, exclude):
            # if not excluding a piece, enter exclude = -1
            # include is for BLOCK where first piece will land
            def is_safe(from_sq2, slide_length):
                for j in range(1, slide_length):
                    if (from_sq2 + j) % 60 != exclude:
                        # the above check avoids the first piece that's moving
                        if (from_sq2 + j) % 60 == include:
                            # first piece will move here, return False
                            return False
                        if self.model.main_board[(from_sq2 + j) % 60].is_occupied():
                            if self.model.main_board[(from_sq2 + j) % 60].get_color() == color:
                                return False
                return True
            # check which slide and slide_length
            if start_block == 5 and color != "yellow":
                return is_safe(start_block, 5)
            elif start_block == 57 and color != "yellow":
                return is_safe(start_block, 4)
            elif start_block == 50 and color != "blue":
                return is_safe(start_block, 5)
            elif start_block == 42 and color != "blue":
                return is_safe(start_block, 4)
            elif start_block == 35 and color != "red":
                return is_safe(start_block, 5)
            elif start_block == 27 and color != "red":
                return is_safe(start_block, 4)
            elif start_block == 20 and color != "green":
                return is_safe(start_block, 5)
            elif start_block == 12 and color != "green":
                return is_safe(start_block, 4)
            return False
        
        # main body of method begins here
        player_pieces = self.get_player_pieces(color)
        for i in range(len(player_pieces) - 1):
            for j in range(i + 1, len(player_pieces)):
                m = 6
                piece1_legal = False
                piece2_legal = False
                piece1_safe_slide = False
                piece2_safe_slide = False
                while (m >= 1) and not ((piece1_legal and piece2_legal) and (piece1_safe_slide or piece2_safe_slide)):
                    piece1_legal = False
                    piece2_legal = False
                    piece1_is_slide = False
                    piece2_is_slide = False
                    piece1_safe_slide = False
                    piece2_safe_slide = False
                    n = 7 - m
                    piece1_target = self.find_real_target(player_pieces[i], m, color)
                    if piece1_target != -1:
                        zone, sq = self.get_list_and_square_from_model(piece1_target)
                        # check if legal move, target does not have color
                        if zone[sq].is_occupied():
                            if zone[sq].get_color() != color:
                                # legal move
                                piece1_legal = True
                        else:
                            # unoccupied: legal move
                            piece1_legal = True
                        # continue if piece1_legal
                        if piece1_legal:
                            piece1_is_slide = is_slide(piece1_target)
                            if piece1_is_slide:
                                piece1_safe_slide = is_safe_slide(piece1_target, -1, -1)
                            # continue with piece2
                            piece2_target = self.find_real_target(player_pieces[j], n, color)
                            if piece2_target != -1 and piece2_target != piece1_target:
                                zone, sq = self.get_list_and_square_from_model(piece2_target)
                                # check if legal move, target does not have color
                                if piece2_target == player_pieces[i]:
                                    # legal move
                                    piece2_legal = True
                                elif zone[sq].is_occupied():
                                    if zone[sq].get_color() != color:
                                        # legal move
                                        piece2_legal = True
                                else:
                                    # unoccupied: legal move
                                    piece2_legal = True
                                # continue if piece2_legal
                                if piece2_legal:
                                    piece2_is_slide = is_slide(piece2_target)
                                    if piece2_is_slide:
                                        piece2_safe_slide = is_safe_slide(piece2_target,
                                                self.find_target_block(player_pieces[i], m, -1, color),
                                                player_pieces[i])
                    if not ((piece1_legal and piece2_legal) and (piece1_safe_slide or piece2_safe_slide)):
                        m -= 1
                # after while loop: moves are legal and at least one is safe_slide if m > 0
                if m > 0:
                    make_move(player_pieces[i], piece1_target, player_pieces[j], piece2_target)
                    return True
        return False
    
    def split_cannot_move_seven_strategy(self, color):
        """
        Does: last resort split move for seven card, happens when all other strategies fail
        Returns: True if move executes
        """
        def make_move(p1_from_block, p1_target_block, p2_from_block, p2_target_block):
            # makes both moves
            p1_from_list_model, p1_from_sq_model = self.get_list_and_square_from_model(p1_from_block)
            p1_to_list_model, p1_to_sq_model = self.get_list_and_square_from_model(p1_target_block)
            p1_from_list_view, p1_from_sq_view = self.get_list_and_square_from_view(p1_from_block)
            p1_to_list_view, p1_to_sq_view = self.get_list_and_square_from_view(p1_target_block)
            p2_from_list_model, p2_from_sq_model = self.get_list_and_square_from_model(p2_from_block)
            p2_to_list_model, p2_to_sq_model = self.get_list_and_square_from_model(p2_target_block)
            p2_from_list_view, p2_from_sq_view = self.get_list_and_square_from_view(p2_from_block)
            p2_to_list_view, p2_to_sq_view = self.get_list_and_square_from_view(p2_target_block)
            
            self.model.move_piece(p1_from_list_model, p1_from_sq_model, p1_to_list_model, p1_to_sq_model)
            self.view.move_piece(p1_from_list_view, p1_from_sq_view, p1_to_list_view, p1_to_sq_view)
            if p1_to_list_model is self.model.main_board:
                self.check_slide(p1_to_sq_view, color)
            self.display_all_starts()

            self.model.move_piece(p2_from_list_model, p2_from_sq_model, p2_to_list_model, p2_to_sq_model)
            self.view.move_piece(p2_from_list_view, p2_from_sq_view, p2_to_list_view, p2_to_sq_view)
            if p2_to_list_model is self.model.main_board:
                self.check_slide(p2_to_sq_view, color)
            self.display_all_starts()
            #print('{}: split_cannot_move_seven_strategy'.format(color.capitalize()))
        
        # body of method begins here
        # get player pieces 'blocks' in array
        player_pieces = self.get_player_pieces(color)
        # compare pieces one by one
        for i in range(0, len(player_pieces) - 1):
            for j in range(i + 1, len(player_pieces)):
                m = 6
                piece1_safe = False
                piece2_safe = False
                while (m >= 1) and not (piece1_safe and piece2_safe):
                    piece1_safe = False
                    piece2_safe = False
                    n = 7 - m
                    piece1_target = self.find_target_block(player_pieces[i], m, -1, color)
                    if piece1_target != -1:
                        piece1_safe = True
                        piece2_target = self.find_target_block(player_pieces[j], n, player_pieces[i], color)
                        if piece2_target != -1:
                            if piece1_target != piece2_target:
                                # this would prevent a double slide but that's ok: this strategy
                                # won't get to that point, it will make a move before that possibility
                                piece2_safe = True
                            else:
                                # targets are the same: ok if home space
                                zone, sq = self.get_list_and_square_from_model(piece1_target)
                                if zone[sq].is_home():
                                    piece2_safe = True
                    if not (piece1_safe and piece2_safe):
                        m -= 1
                if piece1_safe and piece2_safe:
                    # make move
                    p1_real_target = self.find_real_target(player_pieces[i], m, color)
                    p2_real_target = self.find_real_target(player_pieces[j], n, color)
                    if p1_real_target != -1 and p2_real_target != -1:
                        make_move(player_pieces[i], p1_real_target, player_pieces[j], p2_real_target)
                        return True
        return False

    def get_player_pieces(self, color):
        """
        Does: for 7 card strategy, puts piece BLOCKS in array
        Returns: array of BLOCK numbers
        """
        # puts block numbers in array and returns it
        arr = []
        if color == "yellow":
            for i in range(4, -1, -1):
                if self.model.yellow_safety[i].is_occupied():
                    arr.append(i + 100)
            for i in range(58, -1, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        arr.append(i)
            for i in range(59, 58, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        arr.append(i)
        elif color == "green":
            for i in range(4, -1, -1):
                if self.model.green_safety[i].is_occupied():
                    arr.append(i + 200)
            for i in range(13, -1, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        arr.append(i)
            for i in range(59, 13, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        arr.append(i)
        elif color == "red":
            for i in range(4, -1, -1):
                if self.model.red_safety[i].is_occupied():
                    arr.append(i + 300)
            for i in range(28, -1, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        arr.append(i)
            for i in range(59, 28, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        arr.append(i)
        elif color == "blue":
            for i in range(4, -1, -1):
                if self.model.blue_safety[i].is_occupied():
                    arr.append(i + 400)
            for i in range(43, -1, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        arr.append(i)
            for i in range(59, 43, -1):
                if self.model.main_board[i].is_occupied():
                    if self.model.main_board[i].get_color() == color:
                        arr.append(i)
        return arr

    def find_target_block(self, from_block, move_num, exclude_block, color):
        """
        Does: for 7 card, finds and returns BLOCK where piece will end up (after slide if applicable)
        Returns: target BLOCK if found, -1 if not
        """
        # finds 'target block': block where piece will wind up (after slide if applicable)
        # 'exclude_block' is block where other piece in question is and should be excluded from search
        # 'exclude_block' is -1 if no blocks should be excluded
        target_block = -1
        if color == "yellow":
            if from_block <= 58:
                if from_block + move_num > 58:
                    target_block = (from_block + move_num) % 59 + 100
                    if target_block > 105:
                        return -1
                else:
                    target_block = (from_block + move_num) % 60
            elif from_block == 59:
                target_block = (from_block + move_num) % 60
            elif from_block > 59:
                target_block = from_block + move_num
                if target_block > 105:
                    return -1
        elif color == "green":
            if from_block <= 13:
                if from_block + move_num > 13:
                    target_block = (from_block + move_num) % 14 + 200
                    if target_block > 205:
                        return -1
                else:
                    target_block = (from_block + move_num) % 60
            elif 13 < from_block <= 59:
                target_block = (from_block + move_num) % 60
            elif from_block > 59:
                target_block = from_block + move_num
                if target_block > 205:
                    return -1
        elif color == "red":
            if from_block <= 28:
                if from_block + move_num > 28:
                    target_block = (from_block + move_num) % 29 + 300
                    if target_block > 305:
                        return -1
                else:
                    target_block = (from_block + move_num) % 60
            elif 28 < from_block <= 59:
                target_block = (from_block + move_num) % 60
            elif from_block > 59:
                target_block = from_block + move_num
                if target_block > 305:
                    return -1
        elif color == "blue":
            if from_block <= 43:
                if from_block + move_num > 43:
                    target_block = (from_block + move_num) % 44 + 400
                    if target_block > 405:
                        return -1
                else:
                    target_block = (from_block + move_num) % 60
            elif 43 < from_block <= 59:
                target_block = (from_block + move_num) % 60
            elif from_block > 59:
                target_block = from_block + move_num
                if target_block > 405:
                    return -1
        # check if target_block is occupied by color: return -1
        if target_block != -1:
            if target_block != exclude_block:
                zone, sq = self.get_list_and_square_from_model(target_block)
                if zone[sq].is_occupied():
                    if zone[sq].get_color() == color:
                        return -1
        # add slide if necessary
        if target_block == 50 and color != "blue":
            target_block += 4
        elif target_block == 42 and color != "blue":
            target_block += 3
        elif target_block == 35 and color != "red":
            target_block += 4
        elif target_block == 27 and color != "red":
            target_block += 3
        elif target_block == 20 and color != "green":
            target_block += 4
        elif target_block == 12 and color != "green":
            target_block += 3
        elif target_block == 5 and color != "yellow":
            target_block += 4
        elif target_block == 57 and color != "yellow":
            target_block = 0
        return target_block

    def find_real_target(self, from_block, move_num, color):
        """
        Does: finds 'real' target BLOCK == actual BLOCK to move from before slide
        Returns: real_target BLOCK num if found, -1 if not
        """
        # finds 'real_target' before slide
        # if from_block == -1, then function returns -1
        real_target = -1
        if color == "yellow":
            if 0 <= from_block <= 58:
                if from_block + move_num > 58:
                    real_target = (from_block + move_num)%59 + 100
                else:
                    real_target = (from_block + move_num)%60
            elif from_block == 59:
                real_target = (from_block + move_num)%60
            elif from_block > 59:
                real_target = from_block + move_num
                if real_target > 105:
                    return -1
        elif color == "green":
            if 0 <= from_block <= 13:
                if from_block + move_num > 13:
                    real_target = (from_block + move_num)%14 + 200
                else:
                    real_target = (from_block + move_num)%60
            elif 13 < from_block <= 59:
                real_target = (from_block + move_num)%60
            elif from_block > 59:
                real_target = from_block + move_num
                if real_target > 205:
                    return -1
        elif color == "red":
            if 0 <= from_block <= 28:
                if from_block + move_num > 28:
                    real_target = (from_block + move_num)%29 + 300
                else:
                    real_target = (from_block + move_num)%60
            elif 28 < from_block <= 59:
                real_target = (from_block + move_num)%60
            elif from_block > 59:
                real_target = from_block + move_num
                if real_target > 305:
                    return -1
        elif color == "blue":
            if 0 <= from_block <= 43:
                if from_block + move_num > 43:
                    real_target = (from_block + move_num)%44 + 400
                else:
                    real_target = (from_block + move_num)%60
            elif 43 < from_block <= 59:
                real_target = (from_block + move_num)%60
            elif from_block > 59:
                real_target = from_block + move_num
                if real_target > 405:
                    return -1
        return real_target

    def forfeit_turn_strategy(self, color):
        """
        Does: Forfeits move by doing nothing!
        Returns: True
        """
        self.view.display_text("{} player \n forfeits turn.".format(color.capitalize()))
        #print('{}: forfeit_turn_strategy'.format(color.capitalize()))
        return True
    
    def check_slide(self, from_sq, color):
        """
        Does: checks if slide is possible and executes slide in view
        """
        if from_sq == 57 and color != 'yellow':
            self.view.slide(57, 3)
        elif from_sq == 5 and color != 'yellow':
            self.view.slide(5, 4)
        elif from_sq == 12 and color != 'green':
            self.view.slide(12, 3)
        elif from_sq == 20 and color != 'green':
            self.view.slide(20, 4)
        elif from_sq == 27 and color != 'red':
            self.view.slide(27, 3)
        elif from_sq == 35 and color != 'red':
            self.view.slide(35, 4)
        elif from_sq == 42 and color != 'blue':
            self.view.slide(42, 3)
        elif from_sq == 50 and color != 'blue':
            self.view.slide(50, 4)

    def draw_card(self):
        """
        Does: draws a card in model and displays in view
        """
        self.model.draw_card()
        if self.model.deck.is_empty():
            self.view.undraw_draw_pile()
            update()
        self.view.display_discard(self.model.discard[-1].get_name())

    def inform_player(self):
        """
        Does: tells player what color they are, and which color goes first
        """
        self.view.display_text('You are the {} player.'.format(self.player1.get_color().capitalize()))
        time.sleep(LONG_PAUSE)
        if self.player1_turn:
            self.view.display_text('{} player goes first.'.format(self.player1.get_color().capitalize()))
            time.sleep(PAUSE)
        elif self.player2_turn:
            self.view.display_text('{} player goes first.'.format(self.player2.get_color().capitalize()))
            time.sleep(PAUSE)
        elif self.player3_turn:
            self.view.display_text('{} player goes first.'.format(self.player3.get_color().capitalize()))
            time.sleep(PAUSE)
        elif self.player4_turn:
            self.view.display_text('{} player goes first.'.format(self.player4.get_color().capitalize()))
            time.sleep(PAUSE)
        

    def play_sorry(self):
        """
        Does: loops the game until game is won
        """
        # first, inform player
        self.inform_player()
        
        while self.game_over == False:
            if self.player1_turn:
                self.play_player1_turn()
                #self.play_computer_turn(self.player1.get_color())
            elif self.player2_turn:
                self.play_computer_turn(self.player2.get_color())
            elif self.player3_turn:
                self.play_computer_turn(self.player3.get_color())
            elif self.player4_turn:
                self.play_computer_turn(self.player4.get_color())
        # game over
        print('GAME OVER')


