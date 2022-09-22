# sorry_model.py
# This is the model for Sorry!
from sorry_cards import *

class validSpace():
    def __init__(self):
        self.space = []
        self.home = False

    def is_occupied(self):
        if not self.space:
            return False
        elif self.space:
            return True

    def is_valid(self):
        return True

    def is_home(self):
        return self.home

    def set_home(self):
        self.home = True

    def get_color(self):
        if self.space:
            return self.space[0].get_color()
        else:
            print('Unoccupied space.')

    def add_piece(self, new_piece):
        self.space.append(new_piece)

    def remove_piece(self):
        if self.space:
            old_piece = self.space.pop(0)
            return old_piece
        else:
            print('Cannot remove a piece if unoccupied.')

class invalidSpace():
    def is_occupied(self):
        return False

    def is_valid(self):
        return False

    def is_home(self):
        return False

    def set_home(self):
        print('Invalid space cannot be set as home.')

    def get_color(self):
        print('Invalid space cannot contain a piece.')

    def add_piece(self, new_piece):
        print('Cannot add piece to invalid space.')

    def remove_piece(self):
        print('Cannot remove a piece from an invalid space.')
        return None

class piece():
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

class sorryModel():
    def __init__(self, num_players):
        if num_players == 2 or num_players == 3 or num_players == 4:
            self.num_players = num_players
        else:
            print('Invalid number of players')
            self.num_players = 4
        self.yellow_start = []
        self.green_start = []
        self.red_start = []
        self.blue_start = []
        self.yellow_safety = []
        self.green_safety = []
        self.red_safety = []
        self.blue_safety = []
        self.main_board = []
        self.deck = deck()
        self.discard = []
        self.create_board(self.num_players)

    def create_board(self, num_players):
        """
        Does: creates board as lists of valid spaces and invalid spaces
        """
        # create main board
        for i in range(60):
            self.main_board.append(validSpace())
        # yellow safety zone and home
        for i in range(6):
            self.yellow_safety.append(validSpace())
        self.yellow_safety[5].set_home()
        for i in range(12):
            self.yellow_safety.append(invalidSpace())
        # green safety zone and home
        for i in range(6):
            self.green_safety.append(validSpace())
        self.green_safety[5].set_home()
        for i in range(12):
            self.green_safety.append(invalidSpace())
        # red safety zone and home
        for i in range(6):
            self.red_safety.append(validSpace())
        self.red_safety[5].set_home()
        for i in range(12):
            self.red_safety.append(invalidSpace())
        # blue safety zone and home
        for i in range(6):
            self.blue_safety.append(validSpace())
        self.blue_safety[5].set_home()
        for i in range(12):
            self.blue_safety.append(invalidSpace())
        # create game pieces according to num_players
        if num_players == 2:
            for i in range(4):
                self.yellow_start.append(piece('yellow'))
            for i in range(4):
                self.red_start.append(piece('red'))
        elif num_players == 3:
            for i in range(4):
                self.yellow_start.append(piece('yellow'))
            for i in range(4):
                self.green_start.append(piece('green'))
            for i in range(4):
                self.blue_start.append(piece('blue'))
        elif num_players == 4:
            for i in range(4):
                self.yellow_start.append(piece('yellow'))
            for i in range(4):
                self.green_start.append(piece('green'))
            for i in range(4):
                self.red_start.append(piece('red'))
            for i in range(4):
                self.blue_start.append(piece('blue'))

    def move_piece(self, from_list, from_sq, to_list, to_sq):
        """
        Does: moves piece to desired list and square, if occupied it removes
        piece to appropriate start. If piece must slide it calls slide().
        Does not check the rules.
        Returns: Void
        """
        new_piece_color = from_list[from_sq].get_color()
        if to_list[to_sq].is_home():
            nothing = True
        elif to_list[to_sq].is_occupied():
            # knock piece back to start
            if to_list[to_sq].get_color() == 'yellow':
                old_piece = to_list[to_sq].remove_piece()
                self.yellow_start.append(old_piece)
            elif to_list[to_sq].get_color() == 'green':
                old_piece = to_list[to_sq].remove_piece()
                self.green_start.append(old_piece)
            elif to_list[to_sq].get_color() == 'red':
                old_piece = to_list[to_sq].remove_piece()
                self.red_start.append(old_piece)
            elif to_list[to_sq].get_color() == 'blue':
                old_piece = to_list[to_sq].remove_piece()
                self.blue_start.append(old_piece)
        
        # complete move
        new_piece = from_list[from_sq].remove_piece()
        to_list[to_sq].add_piece(new_piece)
        # check for possible slide and execute
        if to_sq == 57 and new_piece_color != 'yellow':
            self.slide(57, 3)
        elif to_sq == 5 and not to_list[to_sq].is_home() \
             and new_piece_color != 'yellow':
            self.slide(5, 4)
        elif to_sq == 12 and new_piece_color != 'green':
            self.slide(12, 3)
        elif to_sq == 20 and new_piece_color != 'green':
            self.slide(20, 4)
        elif to_sq == 27 and new_piece_color != 'red':
            self.slide(27, 3)
        elif to_sq == 35 and new_piece_color != 'red':
            self.slide(35, 4)
        elif to_sq == 42 and new_piece_color != 'blue':
            self.slide(42, 3)
        elif to_sq == 50 and new_piece_color != 'blue':
            self.slide(50, 4)

    def move_piece_from_start(self, start_list, to_sq):
        """
        Does: takes piece from start and places it on the board,
        removes other piece back to start if necessary, checks and executes
        slide if necessary
        """
        new_piece_color = start_list[-1].get_color()
        if self.main_board[to_sq].is_occupied():
            # knock piece back to start
            if self.main_board[to_sq].get_color() == 'yellow':
                old_piece = self.main_board[to_sq].remove_piece()
                self.yellow_start.append(old_piece)
            elif self.main_board[to_sq].get_color() == 'green':
                old_piece = self.main_board[to_sq].remove_piece()
                self.green_start.append(old_piece)
            elif self.main_board[to_sq].get_color() == 'red':
                old_piece = self.main_board[to_sq].remove_piece()
                self.red_start.append(old_piece)
            elif self.main_board[to_sq].get_color() == 'blue':
                old_piece = self.main_board[to_sq].remove_piece()
                self.blue_start.append(old_piece)
        
        # complete move
        new_piece = start_list.pop()
        self.main_board[to_sq].add_piece(new_piece)
        # check for possible slide and execute
        if to_sq == 57 and new_piece_color != 'yellow':
            self.slide(57, 3)
        elif to_sq == 5 and new_piece_color != 'yellow':
            self.slide(5, 4)
        elif to_sq == 12 and new_piece_color != 'green':
            self.slide(12, 3)
        elif to_sq == 20 and new_piece_color != 'green':
            self.slide(20, 4)
        elif to_sq == 27 and new_piece_color != 'red':
            self.slide(27, 3)
        elif to_sq == 35 and new_piece_color != 'red':
            self.slide(35, 4)
        elif to_sq == 42 and new_piece_color != 'blue':
            self.slide(42, 3)
        elif to_sq == 50 and new_piece_color != 'blue':
            self.slide(50, 4)

    def trade_pieces(self, from_sq, to_sq):
        """
        Does: trades one piece with another, checks and executes slide
        """
        piece1 = self.main_board[from_sq].remove_piece()
        piece2 = self.main_board[to_sq].remove_piece()
        self.main_board[to_sq].add_piece(piece1)
        self.main_board[from_sq].add_piece(piece2)
        # check for possible slide and execute
        if to_sq == 57 and self.main_board[to_sq].get_color() != 'yellow':
            self.slide(57, 3)
        elif to_sq == 5 and self.main_board[to_sq].get_color() != 'yellow':
            self.slide(5, 4)
        elif to_sq == 12 and self.main_board[to_sq].get_color() != 'green':
            self.slide(12, 3)
        elif to_sq == 20 and self.main_board[to_sq].get_color() != 'green':
            self.slide(20, 4)
        elif to_sq == 27 and self.main_board[to_sq].get_color() != 'red':
            self.slide(27, 3)
        elif to_sq == 35 and self.main_board[to_sq].get_color() != 'red':
            self.slide(35, 4)
        elif to_sq == 42 and self.main_board[to_sq].get_color() != 'blue':
            self.slide(42, 3)
        elif to_sq == 50 and self.main_board[to_sq].get_color() != 'blue':
            self.slide(50, 4)
        # check for possible slide and execute
        if from_sq == 57 and self.main_board[from_sq].get_color() != 'yellow':
            self.slide(57, 3)
        elif from_sq == 5 and self.main_board[from_sq].get_color() != 'yellow':
            self.slide(5, 4)
        elif from_sq == 12 and self.main_board[from_sq].get_color() != 'green':
            self.slide(12, 3)
        elif from_sq == 20 and self.main_board[from_sq].get_color() != 'green':
            self.slide(20, 4)
        elif from_sq == 27 and self.main_board[from_sq].get_color() != 'red':
            self.slide(27, 3)
        elif from_sq == 35 and self.main_board[from_sq].get_color() != 'red':
            self.slide(35, 4)
        elif from_sq == 42 and self.main_board[from_sq].get_color() != 'blue':
            self.slide(42, 3)
        elif from_sq == 50 and self.main_board[from_sq].get_color() != 'blue':
            self.slide(50, 4)


    def slide(self, from_sq, num_spaces):
        """
        Does: performs a slide for given number of spaces
        """
        for i in range(num_spaces):
            new_sq = (from_sq + i) % 60
            self.move_piece(self.main_board, new_sq, self.main_board,
                            (new_sq + 1) % 60)

    def draw_card(self):
        """
        Does: draws a card from deck into discard pile
        """
        self.deck.draw_card(self.discard)
        
        
##def main():
##    model = sorryModel(4)
####    print(model.yellow_start[0].get_color())
####    print(model.green_start[0].get_color())
####    print(model.red_start[0].get_color())
####    print(model.blue_start[0].get_color())
####    model.move_piece_from_start(model.yellow_start, 12)
####    print(model.main_board[12].is_occupied())
####    print(model.main_board[15].is_occupied())
####    model.move_piece(model.main_board, 15, model.main_board, 20)
####    print(model.main_board[20].is_occupied())
####    print(model.main_board[24].is_occupied())
####    model.move_piece(model.main_board, 24, model.main_board, 57)
####    print(model.main_board[57].is_occupied())
##    
##
##main()
