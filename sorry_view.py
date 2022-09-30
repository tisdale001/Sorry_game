# sorry_view.py
# This is a view for multiple players

from graphics import *
import math
import time

FRAMES = 58
FRAMES2 = 58
FRAMES3 = 232

class validViewSpace():
    def __init__(self):
        self.space = []
        self.home = False

    def is_home(self):
        return self.home

    def set_home(self):
        self.home = True

    def is_occupied(self):
        if self.space:
            return True
        return False

    def get_num_pieces(self):
        if self.space:
            return len(self.space)
        return 0

    def add_piece(self, new_piece):
        self.space.append(new_piece)

    def remove_piece(self):
        if self.space:
            old_piece = self.space.pop(0)
            return old_piece
        else:
            print('Cannot remove a piece if unoccupied.')

class sorryView():
    def __init__(self):
        self.win = GraphWin("Sorry", 952, 952, autoflush = False)
        self.win.setBackground('lightblue')
        self.main_text = Text(Point(476, 476), 'Sorry!')
        self.draw_pile = Image(Point(476, 476 - 128), 'back_of_card.gif')
        self.discard_pile = []
        self.yellow_start = []
        self.green_start = []
        self.red_start = []
        self.blue_start = []
        self.yellow_safety = []
        self.green_safety = []
        self.red_safety = []
        self.blue_safety = []
        self.main_board = []
        self.setup_board()
        self.draw_board()

    def setup_board(self):
        """
        Does: sets up array for main_board and safety zones
        """
        for i in range(60):
            self.main_board.append(validViewSpace())
        for i in range(6):
            self.yellow_safety.append(validViewSpace())
        for i in range(6):
            self.green_safety.append(validViewSpace())
        for i in range(6):
            self.red_safety.append(validViewSpace())
        for i in range(6):
            self.blue_safety.append(validViewSpace())
        self.yellow_safety[5].set_home()
        self.green_safety[5].set_home()
        self.red_safety[5].set_home()
        self.blue_safety[5].set_home()
        

    def draw_board(self):
        # border
        rect1 = Rectangle(Point(3, 3), Point(949, 949))
        rect1.setWidth(6)
        rect1.draw(self.win)
        rect2 = Rectangle(Point(9, 9), Point(943, 943))
        rect2.setOutline('white')
        rect2.setWidth(6)
        rect2.draw(self.win)
        # boxes
        for i in range(16):
            rect = Rectangle(Point(12 + i*58, 940), Point(70 + i*58, 882))
            rect.setFill('white')
            rect.setWidth(3)
            rect.draw(self.win)
        for i in range(16):
            rect = Rectangle(Point(12 + i*58, 12), Point(70 + i*58, 70))
            rect.setFill('white')
            rect.setWidth(3)
            rect.draw(self.win)
        for i in range(14):
            rect = Rectangle(Point(12, 70 + i*58), Point(70, 128 + i*58))
            rect.setFill('white')
            rect.setWidth(3)
            rect.draw(self.win)
        for i in range(14):
            rect = Rectangle(Point(882, 70 + i*58), Point(940, 128 + i*58))
            rect.setFill('white')
            rect.setWidth(3)
            rect.draw(self.win)
        # safety zone: yellow
        for i in range(5):
            rect = Rectangle(Point(766, 882 - i*58), Point(824, 824 - i*58))
            rect.setWidth(3)
            rect.draw(self.win)
        rect = Rectangle(Point(766, 592), Point(824, 534))
        rect.setWidth(3)
        rect.setFill('black')
        rect.draw(self.win)
        for i in range(5):
            rect = Rectangle(Point(769, 879 - i*58), Point(821, 827 - i*58))
            rect.setWidth(3)
            rect.setOutline('white')
            rect.draw(self.win)
        for i in range(5):
            rect = Rectangle(Point(772, 876 - i*58), Point(818, 830 - i*58))
            rect.setFill('yellow')
            rect.draw(self.win)
        circ = Circle(Point(795, 534 - 12), 58 + 12)
        circ.setFill('black')
        circ.draw(self.win)
        circ2 = Circle(Point(795, 534 - 12), 58 + 6)
        circ2.setOutline('white')
        circ2.setWidth(3)
        circ2.setFill('black')
        circ2.draw(self.win)
        # star of david: yellow
        tri = Polygon(Point(795, 586), Point(740, 490), Point(850, 490))
        tri.setWidth(3)
        tri.setOutline('white')
        tri.draw(self.win)
        tri2 = Polygon(Point(795, 458), Point(740, 554), Point(850, 554))
        tri2.setWidth(3)
        tri2.setOutline('white')
        tri2.draw(self.win)
        tri3 = Polygon(Point(795, 580), Point(745, 493), Point(845, 493))
        tri3.setWidth(3)
        tri3.setOutline('black')
        tri3.draw(self.win)
        tri4 = Polygon(Point(795, 464), Point(745, 551), Point(845, 551))
        tri4.setWidth(3)
        tri4.setOutline('black')
        tri4.draw(self.win)
        tri5 = Polygon(Point(795, 574), Point(750, 496), Point(840, 496))
        tri5.setWidth(3)
        tri5.setOutline('yellow')
        tri5.setFill('yellow')
        tri5.draw(self.win)
        tri6 = Polygon(Point(795, 470), Point(750, 548), Point(840, 548))
        tri6.setWidth(3)
        tri6.setOutline('yellow')
        tri6.setFill('yellow')
        tri6.draw(self.win)
        # start: yellow
        rect = Rectangle(Point(650, 882), Point(708, 824))
        rect.setFill('black')
        rect.setWidth(3)
        rect.draw(self.win)
        
        circ = Circle(Point(679, 812), 70)
        circ.setFill('black')
        circ.setWidth(3)
        circ.draw(self.win)
        circ2 = Circle(Point(679, 812), 64)
        circ2.setOutline('white')
        circ2.setFill('white')
        circ2.setWidth(3)
        circ2.draw(self.win)
        circ3 = Circle(Point(679, 812), 58)
        circ3.setFill('yellow')
        circ3.setWidth(3)
        circ3.draw(self.win)
        # safety zone: red
        for i in range(5):
            rect = Rectangle(Point(128, 70 + i*58), Point(186, 128 + i*58))
            rect.setWidth(3)
            rect.draw(self.win)
        rect = Rectangle(Point(128, 360), Point(186, 418))
        rect.setFill('black')
        rect.setWidth(3)
        rect.draw(self.win)
        for i in range(5):
            rect = Rectangle(Point(131, 73 + i*58), Point(183, 125 + i*58))
            rect.setWidth(3)
            rect.setOutline('white')
            rect.draw(self.win)
        for i in range(5):
            rect = Rectangle(Point(134, 76 + i*58), Point(180, 122 + i*58))
            rect.setFill('red')
            rect.draw(self.win)
        circ = Circle(Point(157, 430), 70)
        circ.setFill('black')
        circ.draw(self.win)
        circ2 = Circle(Point(157, 430), 64)
        circ2.setOutline('white')
        circ2.setWidth(3)
        circ2.setFill('black')
        circ2.draw(self.win)
        # star of david: red
        tri = Polygon(Point(157, 494), Point(102, 398), Point(212, 398))
        tri.setWidth(3)
        tri.setOutline('white')
        tri.draw(self.win)
        tri2 = Polygon(Point(157, 366), Point(102, 462), Point(212, 462))
        tri2.setWidth(3)
        tri2.setOutline('white')
        tri2.draw(self.win)
        tri3 = Polygon(Point(157, 488), Point(107, 401), Point(207, 401))
        tri3.setWidth(3)
        tri3.setOutline('black')
        tri3.draw(self.win)
        tri4 = Polygon(Point(157, 372), Point(107, 459), Point(207, 459))
        tri4.setWidth(3)
        tri4.setOutline('black')
        tri4.draw(self.win)
        tri5 = Polygon(Point(157, 482), Point(112, 404), Point(202, 404))
        tri5.setOutline('red')
        tri5.setFill('red')
        tri5.setWidth(3)
        tri5.draw(self.win)
        tri6 = Polygon(Point(157, 378), Point(112, 456), Point(202, 456))
        tri6.setOutline('red')
        tri6.setFill('red')
        tri6.setWidth(3)
        tri6.draw(self.win)
        # start: red
        rect = Rectangle(Point(244, 70), Point(302, 128))
        rect.setWidth(3)
        rect.setFill('black')
        rect.draw(self.win)
        circ = Circle(Point(273, 140), 70)
        circ.setFill('black')
        circ.setWidth(3)
        circ.draw(self.win)
        circ2 = Circle(Point(273, 140), 64)
        circ2.setOutline('white')
        circ2.setFill('white')
        circ2.setWidth(3)
        circ2.draw(self.win)
        circ3 = Circle(Point(273, 140), 58)
        circ3.setFill('red')
        circ3.setWidth(3)
        circ3.draw(self.win)
        # safety zone: green
        for i in range(5):
            rect = Rectangle(Point(70 + i*58, 824), Point(128 + i*58, 766))
            rect.setWidth(3)
            rect.draw(self.win)
        rect = Rectangle(Point(360, 824), Point(418, 766))
        rect.setFill('black')
        rect.setWidth(3)
        rect.draw(self.win)
        for i in range(5):
            rect = Rectangle(Point(73 + i*58, 821), Point(125 + i*58, 769))
            rect.setWidth(3)
            rect.setOutline('white')
            rect.draw(self.win)
        for i in range(5):
            rect = Rectangle(Point(76 + i*58, 818), Point(122 + i*58, 772))
            rect.setFill('green')
            rect.draw(self.win)
        circ = Circle(Point(430, 795), 70)
        circ.setFill('black')
        circ.draw(self.win)
        circ2 = Circle(Point(430, 795), 64)
        circ2.setOutline('white')
        circ2.setWidth(3)
        circ2.setFill('black')
        circ2.draw(self.win)
        # star of david: green
        tri = Polygon(Point(366, 795), Point(462, 740), Point(462, 850))
        tri.setWidth(3)
        tri.setOutline('white')
        tri.draw(self.win)
        tri2 = Polygon(Point(494, 795), Point(398, 740), Point(398, 850))
        tri2.setWidth(3)
        tri2.setOutline('white')
        tri2.draw(self.win)
        tri3 = Polygon(Point(372, 795), Point(459, 745), Point(459, 845))
        tri3.setWidth(3)
        tri3.setOutline('black')
        tri3.draw(self.win)
        tri4 = Polygon(Point(488, 795), Point(401, 745), Point(401, 845))
        tri4.setWidth(3)
        tri4.setOutline('black')
        tri4.draw(self.win)
        tri5 = Polygon(Point(378, 795), Point(456, 750), Point(456, 840))
        tri5.setOutline('green')
        tri5.setFill('green')
        tri5.setWidth(3)
        tri5.draw(self.win)
        tri6 = Polygon(Point(482, 795), Point(404, 750), Point(404, 840))
        tri6.setOutline('green')
        tri6.setFill('green')
        tri6.setWidth(3)
        tri6.draw(self.win)
        # start: green
        rect = Rectangle(Point(70, 708), Point(128, 650))
        rect.setWidth(3)
        rect.setFill('black')
        rect.draw(self.win)
        circ = Circle(Point(140, 679), 70)
        circ.setFill('black')
        circ.setWidth(3)
        circ.draw(self.win)
        circ2 = Circle(Point(140, 679), 64)
        circ2.setOutline('white')
        circ2.setFill('white')
        circ2.setWidth(3)
        circ2.draw(self.win)
        circ3 = Circle(Point(140, 679), 58)
        circ3.setFill('green')
        circ3.setWidth(3)
        circ3.draw(self.win)
        # safety zone: blue
        for i in range(5):
            rect = Rectangle(Point(824 - i*58, 186), Point(882 - i*58, 128))
            rect.setWidth(3)
            rect.draw(self.win)
        rect = Rectangle(Point(534, 186), Point(592, 128))
        rect.setFill('black')
        rect.setWidth(3)
        rect.draw(self.win)
        for i in range(5):
            rect = Rectangle(Point(827 - i*58, 183), Point(879 - i*58, 131))
            rect.setWidth(3)
            rect.setOutline('white')
            rect.draw(self.win)
        for i in range(5):
            rect = Rectangle(Point(830 - i*58, 180), Point(876 - i*58, 134))
            rect.setFill('blue3')
            rect.draw(self.win)
        circ = Circle(Point(522, 157), 70)
        circ.setFill('black')
        circ.draw(self.win)
        circ2 = Circle(Point(522, 157), 64)
        circ2.setOutline('white')
        circ2.setWidth(3)
        circ2.setFill('black')
        circ2.draw(self.win)
        # star of david: blue
        tri = Polygon(Point(458, 157), Point(554, 102), Point(554, 212))
        tri.setWidth(3)
        tri.setOutline('white')
        tri.draw(self.win)
        tri2 = Polygon(Point(586, 157), Point(490, 102), Point(490, 212))
        tri2.setWidth(3)
        tri2.setOutline('white')
        tri2.draw(self.win)
        tri3 = Polygon(Point(464, 157), Point(551, 107), Point(551, 207))
        tri3.setWidth(3)
        tri3.setOutline('black')
        tri3.draw(self.win)
        tri4 = Polygon(Point(580, 157), Point(493, 107), Point(493, 207))
        tri4.setWidth(3)
        tri4.setOutline('black')
        tri4.draw(self.win)
        tri5 = Polygon(Point(470, 157), Point(548, 112), Point(548, 202))
        tri5.setOutline('blue3')
        tri5.setFill('blue3')
        tri5.setWidth(3)
        tri5.draw(self.win)
        tri6 = Polygon(Point(574, 157), Point(496, 112), Point(496, 202))
        tri6.setOutline('blue3')
        tri6.setFill('blue3')
        tri6.setWidth(3)
        tri6.draw(self.win)
        # start: blue
        rect = Rectangle(Point(824, 302), Point(882, 244))
        rect.setWidth(3)
        rect.setFill('black')
        rect.draw(self.win)
        circ = Circle(Point(812, 273), 70)
        circ.setFill('black')
        circ.setWidth(3)
        circ.draw(self.win)
        circ2 = Circle(Point(812, 273), 64)
        circ2.setOutline('white')
        circ2.setFill('white')
        circ2.setWidth(3)
        circ2.draw(self.win)
        circ3 = Circle(Point(812, 273), 58)
        circ3.setFill('blue3')
        circ3.setWidth(3)
        circ3.draw(self.win)
        # slides: yellow
        rec = Rectangle(Point(679, 911 + 8), Point(863, 911 - 8))
        rec.setWidth(2)
        rec.setFill('yellow')
        rec.draw(self.win)
        tri = Polygon(Point(833, 911), Point(873, 891), Point(873, 931))
        tri.setWidth(2)
        tri.setFill('yellow')
        tri.draw(self.win)
        cir = Circle(Point(679, 911), 20)
        cir.setWidth(2)
        cir.setFill('yellow')
        cir.draw(self.win)
        rec2 = Rectangle(Point(157, 911 + 8), Point(399, 911 - 8))
        rec2.setWidth(2)
        rec2.setFill('yellow')
        rec2.draw(self.win)
        tri2 = Polygon(Point(369, 911), Point(409, 891), Point(409, 931))
        tri2.setWidth(2)
        tri2.setFill('yellow')
        tri2.draw(self.win)
        cir2 = Circle(Point(157, 911), 20)
        cir2.setWidth(2)
        cir2.setFill('yellow')
        cir2.draw(self.win)
        # slides: green
        rec = Rectangle(Point(41 + 8, 679), Point(41 - 8, 863))
        rec.setWidth(2)
        rec.setFill('green')
        rec.draw(self.win)
        tri = Polygon(Point(41, 833), Point(61, 873), Point(21, 873))
        tri.setWidth(2)
        tri.setFill('green')
        tri.draw(self.win)
        cir = Circle(Point(41, 679), 20)
        cir.setWidth(2)
        cir.setFill('green')
        cir.draw(self.win)
        rec2 = Rectangle(Point(41 + 8, 157), Point(41 - 8, 399))
        rec2.setWidth(2)
        rec2.setFill('green')
        rec2.draw(self.win)
        tri2 = Polygon(Point(41, 369), Point(61, 409), Point(21, 409))
        tri2.setWidth(2)
        tri2.setFill('green')
        tri2.draw(self.win)
        cir2 = Circle(Point(41, 157), 20)
        cir2.setWidth(2)
        cir2.setFill('green')
        cir2.draw(self.win)
        # slides: red
        rec = Rectangle(Point(273, 41 + 8), Point(89, 41 - 8))
        rec.setWidth(2)
        rec.setFill('red')
        rec.draw(self.win)
        tri = Polygon(Point(119, 41), Point(79, 61), Point(79, 21))
        tri.setWidth(2)
        tri.setFill('red')
        tri.draw(self.win)
        cir = Circle(Point(273, 41), 20)
        cir.setWidth(2)
        cir.setFill('red')
        cir.draw(self.win)
        rec2 = Rectangle(Point(795, 41 + 8), Point(553, 41 - 8))
        rec2.setWidth(2)
        rec2.setFill('red')
        rec2.draw(self.win)
        tri2 = Polygon(Point(583, 41), Point(543, 61), Point(543, 21))
        tri2.setWidth(2)
        tri2.setFill('red')
        tri2.draw(self.win)
        cir2 = Circle(Point(795, 41), 20)
        cir2.setWidth(2)
        cir2.setFill('red')
        cir2.draw(self.win)
        # slides: blue
        rec = Rectangle(Point(911 + 8, 273), Point(911 - 8, 89))
        rec.setWidth(2)
        rec.setFill('blue3')
        rec.draw(self.win)
        tri = Polygon(Point(911, 119), Point(891, 79), Point(931, 79))
        tri.setWidth(2)
        tri.setFill('blue3')
        tri.draw(self.win)
        cir = Circle(Point(911, 273), 20)
        cir.setWidth(2)
        cir.setFill('blue3')
        cir.draw(self.win)
        rec2 = Rectangle(Point(911 + 8, 795), Point(911 - 8, 553))
        rec2.setWidth(2)
        rec2.setFill('blue3')
        rec2.draw(self.win)
        tri2 = Polygon(Point(911, 583), Point(891, 543), Point(931, 543))
        tri2.setWidth(2)
        tri2.setFill('blue3')
        tri2.draw(self.win)
        cir2 = Circle(Point(911, 795), 20)
        cir2.setWidth(2)
        cir2.setFill('blue3')
        cir2.draw(self.win)
        # display deck of cards
        self.display_draw_pile()
        self.display_sorry_text()

    def display_draw_pile(self):
        """
        Does: undraws then draws draw pile image
        """
        self.draw_pile.undraw()
        self.draw_pile.draw(self.win)

    def undraw_draw_pile(self):
        """
        Does: undraws draw pile (when empty)
        """
        self.draw_pile.undraw()

    def display_discard(self, gif_name):
        """
        Does: displays discard and adds image to discard pile
        """
        img = Image(Point(476, 476 + 128), gif_name)
        img.draw(self.win)
        self.discard_pile.append(img)

    def undraw_discard_pile(self):
        """
        Does: undraws all cards in discard pile
        """
        if self.discard_pile:
            for card in self.discard_pile:
                card.undraw()
        self.discard_pile = []

    def display_sorry_text(self):
        """
        Does: prints 'SORRY!' to main_text
        """
        self.main_text.undraw()
        self.main_text.setText('SORRY!')
        self.main_text.setFace('courier')
        self.main_text.setSize(36)
        self.main_text.setStyle('bold')
        self.main_text.draw(self.win)
        update()

    def display_text(self, string):
        """
        Does: prints given string to main_text area
        """
        self.main_text.undraw()
        self.main_text.setText(string)
        self.main_text.setFace('courier')
        self.main_text.setSize(14)
        self.main_text.setStyle('bold')
        self.main_text.draw(self.win)
        update()


    def display_yellow_start(self, num):
        """
        Does: displays the appropriate number of pieces in start
        """
        if self.yellow_start:
            for piece in self.yellow_start:
                piece.undraw()
        self.yellow_start = []
        for i in range(num):
            if i == 0:
                c_point = Point(679 - 28, 812 - 28)
            elif i == 1:
                c_point = Point(679 + 28, 812 - 28)
            elif i == 2:
                c_point = Point(679 - 28, 812 + 28)
            elif i == 3:
                c_point = Point(679 + 28, 812 + 28)
            piece = Circle(c_point, 24)
            piece.setFill('yellow3')
            piece.draw(self.win)
            self.yellow_start.append(piece)

    def display_green_start(self, num):
        """
        Does: displays the appropriate number of pieces in start
        """
        if self.green_start:
            for piece in self.green_start:
                piece.undraw()
        self.green_start = []
        for i in range(num):
            if i == 0:
                c_point = Point(140 + 28, 679 - 28)
            elif i == 1:
                c_point = Point(140 + 28, 679 + 28)
            elif i == 2:
                c_point = Point(140 - 28, 679 - 28)
            elif i == 3:
                c_point = Point(140 - 28, 679 + 28)
            piece = Circle(c_point, 24)
            piece.setFill('green4')
            piece.draw(self.win)
            self.green_start.append(piece)

    def display_red_start(self, num):
        """
        Does: displays the appropriate number of pieces in start
        """
        if self.red_start:
            for piece in self.red_start:
                piece.undraw()
        self.red_start = []
        for i in range(num):
            if i == 0:
                c_point = Point(273 + 28, 140 + 28)
            elif i == 1:
                c_point = Point(273 - 28, 140 + 28)
            elif i == 2:
                c_point = Point(273 + 28, 140 - 28)
            elif i == 3:
                c_point = Point(273 - 28, 140 - 28)
            piece = Circle(c_point, 24)
            piece.setFill('red3')
            piece.draw(self.win)
            self.red_start.append(piece)

    def display_blue_start(self, num):
        """
        Does: displays the appropriate number of pieces in start
        """
        if self.blue_start:
            for piece in self.blue_start:
                piece.undraw()
        self.blue_start = []
        for i in range(num):
            if i == 0:
                c_point = Point(812 - 28, 273 + 28)
            elif i == 1:
                c_point = Point(812 - 28, 273 - 28)
            elif i == 2:
                c_point = Point(812 + 28, 273 + 28)
            elif i == 3:
                c_point = Point(812 + 28, 273 - 28)
            piece = Circle(c_point, 24)
            piece.setFill('blue4')
            piece.draw(self.win)
            self.blue_start.append(piece)

    def get_block(self, x, y):
        """
        Does: returns block from x, y coordinates
        Returns: block number
        """
        for i in range(0, 11):
            if 882 - (i + 4) * 58 <= x <= 940 - (i + 4) * 58 and 882 <= y <= 940:
                return i
        for i in range(11, 26):
            if 12 <= x <= 70 and 882 - (i - 11) * 58 <= y <= 940 - (i - 11) * 58:
                return i
        for i in range(26, 41):
            if 12 + (i - 26) * 58 <= x <= 70 + (i - 26) * 58 and 12 <= y <= 70:
                return i
        for i in range(41, 56):
            if 882 <= x <= 940 and 12 + (i - 41) * 58 <= y <= 70 + (i - 41) * 58:
                return i
        for i in range(56, 60):
            if 882 - (i - 56) * 58 <= x <= 940 - (i - 56) * 58 and 882 <= y <= 940:
                return i
        for i in range(100, 105):
            if 766 <= x <= 834 and 824 - (i - 100) * 58 <= y <= 882 - (i - 100) * 58:
                return i
        for i in range(200, 205):
            if 70 + (i - 200) * 58 <= x <= 128 + (i - 200) * 58 and 766 <= y <= 824:
                return i
        for i in range(300, 305):
            if 128 <= x <= 186 and 70 + (i - 300) * 58 <= y <= 128 + (i - 300) * 58:
                return i
        for i in range(400, 405):
            if 824 - (i - 400) * 58 <= x <= 882 - (i - 400) * 58 and 128 <= y <= 186:
                return i
        if 384 <= x <= 567 and 281 <= y <= 413:
            return 500
        # yellow start
        if math.sqrt((679 - x)**2 + (812 - y)**2) <= 71:
            return 106
        # green start
        if math.sqrt((140 - x)**2 + (679 - y)**2) <= 71:
            return 206
        # red start
        if math.sqrt((273 - x)**2 + (140 - y)**2) <= 71:
            return 306
        # blue start
        if math.sqrt((812 - x)**2 + (273 - y)**2) <= 71:
            return 406
        # yellow home
        if math.sqrt((795 - x)**2 + (522 - y)**2) <= 71:
            return 105
        # green home
        if math.sqrt((430 - x)**2 + (795 - y)**2) <= 71:
            return 205
        # red home
        if math.sqrt((157 - x)**2 + (430 - y)**2) <= 71:
            return 305
        # blue home
        if math.sqrt((522 - x)**2 + (157 - y)**2) <= 71:
            return 405
        return 600

    def get_block_from_list(self, board_list, square):
        """
        Does: returns the block number from list and square
        Returns: block number
        """
        if board_list is self.yellow_safety:
            return 100 + square
        elif board_list is self.green_safety:
            return 200 + square
        elif board_list is self.red_safety:
            return 300 + square
        elif board_list is self.blue_safety:
            return 400 + square
        elif board_list is self.main_board:
            return square

    def draw_yellow_home(self):
        for i in range(self.yellow_safety[5].get_num_pieces()):
            if i == 0:
                c_point = Point(795 - 28, 522 - 28)
            elif i == 1:
                c_point = Point(795 + 28, 522 - 28)
            elif i == 2:
                c_point = Point(795 - 28, 522 + 28)
            elif i == 3:
                c_point = Point(795 + 28, 522 + 28)
            piece = Circle(c_point, 24)
            piece.setFill('yellow3')
            piece.draw(self.win)

    def draw_green_home(self):
        for i in range(self.green_safety[5].get_num_pieces()):
            if i == 0:
                c_point = Point(430 + 28, 795 - 28)
            elif i == 1:
                c_point = Point(430 + 28, 795 + 28)
            elif i == 2:
                c_point = Point(430 - 28, 795 - 28)
            elif i == 3:
                c_point = Point(430 - 28, 795 + 28)
            piece = Circle(c_point, 24)
            piece.setFill('green4')
            piece.draw(self.win)

    def draw_red_home(self):
        for i in range(self.red_safety[5].get_num_pieces()):
            if i == 0:
                c_point = Point(157 + 28, 430 + 28)
            elif i == 1:
                c_point = Point(157 - 28, 430 + 28)
            elif i == 2:
                c_point = Point(157 + 28, 430 - 28)
            elif i == 3:
                c_point = Point(157 - 28, 430 - 28)
            piece = Circle(c_point, 24)
            piece.setFill('red3')
            piece.draw(self.win)

    def draw_blue_home(self):
        for i in range(self.blue_safety[5].get_num_pieces()):
            if i == 0:
                c_point = Point(522 - 28, 157 + 28)
            elif i == 1:
                c_point = Point(522 - 28, 157 - 28)
            elif i == 2:
                c_point = Point(522 + 28, 157 + 28)
            elif i == 3:
                c_point = Point(522 + 28, 157 - 28)
            piece = Circle(c_point, 24)
            piece.setFill('blue4')
            piece.draw(self.win)

    def move_piece(self, from_list, from_sq, to_list, to_sq, forward = True):
        """
        Does: moves piece from square to square and removes piece if necessary,
        uses helper function animate_piece() and get_block_from_list()
        """
        if forward == True:
            # move piece forward
            if from_list is to_list:
                # simply move piece forward checking for passing 59
                if to_sq > from_sq:
                    # move piece forward
                    piece = from_list[from_sq].remove_piece()
                    for i in range(to_sq - from_sq):
                        self.animate_piece(self.get_block_from_list(from_list, from_sq) + i,
                                           self.get_block_from_list(from_list, from_sq) + 1 + i,
                                           piece)
                    if to_list[to_sq].is_occupied() and not to_list[to_sq].is_home():
                        piece2 = to_list[to_sq].remove_piece()
                        piece2.undraw()
                    to_list[to_sq].add_piece(piece)
                    if to_list is self.yellow_safety and to_list[to_sq].is_home():
                        piece.undraw()
                        self.draw_yellow_home()
                    elif to_list is self.green_safety and to_list[to_sq].is_home():
                        piece.undraw()
                        self.draw_green_home()
                    elif to_list is self.red_safety and to_list[to_sq].is_home():
                        piece.undraw()
                        self.draw_red_home()
                    elif to_list is self.blue_safety and to_list[to_sq].is_home():
                        piece.undraw()
                        self.draw_blue_home()
                else:
                    # move piece to 59, then to 0, then complete move
                    piece = from_list[from_sq].remove_piece()
                    for i in range(59 - from_sq):
                        self.animate_piece(from_sq + i, from_sq + i + 1, piece)
                    self.animate_piece(59, 0, piece)
                    for i in range(to_sq - 0):
                        self.animate_piece(i, i + 1, piece)
                    if to_list[to_sq].is_occupied():
                        piece2 = to_list[to_sq].remove_piece()
                        piece2.undraw()
                    to_list[to_sq].add_piece(piece)
            elif to_list is self.yellow_safety:
                # move piece to 58, then 100, then complete move
                piece = from_list[from_sq].remove_piece()
                for i in range(58 - from_sq):
                    self.animate_piece(from_sq + i, from_sq + i + 1, piece)
                self.animate_piece(58, 100, piece)
                for i in range(self.get_block_from_list(to_list, to_sq) - 100):
                    self.animate_piece(self.get_block_from_list(to_list, 0) + i,
                                       self.get_block_from_list(to_list, 1) + i,
                                       piece)
                to_list[to_sq].add_piece(piece)
                if to_list[to_sq].is_home():
                    piece.undraw()
                    self.draw_yellow_home()
            elif to_list is self.green_safety:
                # move piece to 13, then 200, then complete move
                piece = from_list[from_sq].remove_piece()
                for i in range(13 - from_sq):
                    self.animate_piece(from_sq + i, from_sq + i + 1, piece)
                self.animate_piece(13, 200, piece)
                for i in range(self.get_block_from_list(to_list, to_sq) - 200):
                    self.animate_piece(self.get_block_from_list(to_list, 0) + i,
                                       self.get_block_from_list(to_list, 1) + i,
                                       piece)
                to_list[to_sq].add_piece(piece)
                if to_list[to_sq].is_home():
                    piece.undraw()
                    self.draw_green_home()
            elif to_list is self.red_safety:
                # move piece to 28, then 300, then complete move
                piece = from_list[from_sq].remove_piece()
                for i in range(28 - from_sq):
                    self.animate_piece(from_sq + i, from_sq + i + 1, piece)
                self.animate_piece(28, 300, piece)
                for i in range(self.get_block_from_list(to_list, to_sq) - 300):
                    self.animate_piece(self.get_block_from_list(to_list, 0 + i),
                                       self.get_block_from_list(to_list, 1 + i),
                                       piece)
                to_list[to_sq].add_piece(piece)
                if to_list[to_sq].is_home():
                    piece.undraw()
                    self.draw_red_home()
            elif to_list is self.blue_safety:
                # move piece to 43, then 400, then complete move
                piece = from_list[from_sq].remove_piece()
                for i in range(43 - from_sq):
                    self.animate_piece(from_sq + i, from_sq + i + 1, piece)
                self.animate_piece(43, 400, piece)
                for i in range(self.get_block_from_list(to_list, to_sq) - 400):
                    self.animate_piece(self.get_block_from_list(to_list, 0) + i,
                                       self.get_block_from_list(to_list, 1) + i,
                                       piece)
                to_list[to_sq].add_piece(piece)
                if to_list[to_sq].is_home():
                    piece.undraw()
                    self.draw_blue_home()
        elif forward == False:
            # move piece backward
            if from_list is to_list:
                # check for passing 0
                if from_sq > to_sq:
                    # complete the move
                    piece = from_list[from_sq].remove_piece()
                    for i in range(from_sq - to_sq):
                        self.animate_piece(self.get_block_from_list(from_list, from_sq) - i,
                                           self.get_block_from_list(from_list, from_sq) - 1 - i,
                                           piece)
                    if to_list[to_sq].is_occupied():
                        piece2 = to_list[to_sq].remove_piece()
                        piece2.undraw()
                    to_list[to_sq].add_piece(piece)
                else:
                    # piece passes from 0 to 59, then completes move
                    piece = from_list[from_sq].remove_piece()
                    for i in range(from_sq, -1, -1):
                        self.animate_piece(i, (i + 60 - 1)%60, piece)
                    for i in range(59 - to_sq):
                        self.animate_piece(59 - i, 59 - i - 1, piece)
                    if to_list[to_sq].is_occupied():
                        piece2 = to_list[to_sq].remove_piece()
                        piece2.undraw()
                    to_list[to_sq].add_piece(piece)
            elif from_list is self.yellow_safety:
                # move to 100, then 58, then complete move
                piece = from_list[from_sq].remove_piece()
                for i in range(from_sq):
                    self.animate_piece(100 + from_sq - i, 100 + from_sq - 1 - i, piece)
                self.animate_piece(100, 58, piece)
                for i in range(58 - to_sq):
                    self.animate_piece(58 - i, 58 - i - 1, piece)
                if to_list[to_sq].is_occupied():
                    piece2 = to_list[to_sq].remove_piece()
                    piece2.undraw()
                to_list[to_sq].add_piece(piece)
            elif from_list is self.green_safety:
                # move to 200, then 13, then complete move
                piece = from_list[from_sq].remove_piece()
                for i in range(from_sq):
                    self.animate_piece(200 + from_sq - i, 200 + from_sq - 1 - i, piece)
                self.animate_piece(200, 13, piece)
                for i in range(13 - to_sq):
                    self.animate_piece(13 - i, 13 - i - 1, piece)
                if to_list[to_sq].is_occupied():
                    piece2 = to_list[to_sq].remove_piece()
                    piece2.undraw()
                to_list[to_sq].add_piece(piece)
            elif from_list is self.red_safety:
                # move to 300, then 28, then complete move
                piece = from_list[from_sq].remove_piece()
                for i in range(from_sq):
                    self.animate_piece(300 + from_sq - i, 300 + from_sq - 1 - i, piece)
                self.animate_piece(300, 28, piece)
                for i in range(28 - to_sq):
                    self.animate_piece(28 - i, 28 - i - 1, piece)
                if to_list[to_sq].is_occupied():
                    piece2 = to_list[to_sq].remove_piece()
                    piece2.undraw()
                to_list[to_sq].add_piece(piece)
            elif from_list is self.blue_safety:
                # move to 400, then 43, then complete move
                piece = from_list[from_sq].remove_piece()
                for i in range(from_sq):
                    self.animate_piece(400 + from_sq - i, 400 + from_sq - 1 - i, piece)
                self.animate_piece(400, 43, piece)
                for i in range(43 - to_sq):
                    self.animate_piece(43 - i, 43 - i - 1, piece)
                if to_list[to_sq].is_occupied():
                    piece2 = to_list[to_sq].remove_piece()
                    piece2.undraw()
                to_list[to_sq].add_piece(piece)

    def move_piece_from_start(self, start_list, to_sq):
        """
        Does: animates move from start to square on the main board
        """
        if start_list is self.yellow_start:
            piece = self.yellow_start.pop()
            if to_sq == 0:
                center_point = piece.getCenter()
                x = center_point.getX()
                y = center_point.getY()
                x2, y2 = self.get_coor(to_sq)
                delta_x = x2 - x
                delta_y = y2 - y
                self.fast_animate(delta_x, delta_y, piece)
                if self.main_board[to_sq].is_occupied():
                    piece2 = self.main_board[to_sq].remove_piece()
                    piece2.undraw()
                self.main_board[to_sq].add_piece(piece)
            else:
                center_point = piece.getCenter()
                x = center_point.getX()
                y = center_point.getY()
                x2, y2 = self.get_coor(to_sq)
                delta_x = x2 - x
                delta_y = y2 - y
                self.slow_animate(delta_x, delta_y, piece)
                if self.main_board[to_sq].is_occupied():
                    piece2 = self.main_board[to_sq].remove_piece()
                    piece2.undraw()
                self.main_board[to_sq].add_piece(piece)
        elif start_list is self.green_start:
            piece = self.green_start.pop()
            if to_sq == 15:
                center_point = piece.getCenter()
                x = center_point.getX()
                y = center_point.getY()
                x2, y2 = self.get_coor(to_sq)
                delta_x = x2 - x
                delta_y = y2 - y
                self.fast_animate(delta_x, delta_y, piece)
                if self.main_board[to_sq].is_occupied():
                    piece2 = self.main_board[to_sq].remove_piece()
                    piece2.undraw()
                self.main_board[to_sq].add_piece(piece)
            else:
                center_point = piece.getCenter()
                x = center_point.getX()
                y = center_point.getY()
                x2, y2 = self.get_coor(to_sq)
                delta_x = x2 - x
                delta_y = y2 - y
                self.slow_animate(delta_x, delta_y, piece)
                if self.main_board[to_sq].is_occupied():
                    piece2 = self.main_board[to_sq].remove_piece()
                    piece2.undraw()
                self.main_board[to_sq].add_piece(piece)
        elif start_list is self.red_start:
            piece = self.red_start.pop()
            if to_sq == 30:
                center_point = piece.getCenter()
                x = center_point.getX()
                y = center_point.getY()
                x2, y2 = self.get_coor(to_sq)
                delta_x = x2 - x
                delta_y = y2 - y
                self.fast_animate(delta_x, delta_y, piece)
                if self.main_board[to_sq].is_occupied():
                    piece2 = self.main_board[to_sq].remove_piece()
                    piece2.undraw()
                self.main_board[to_sq].add_piece(piece)
            else:
                center_point = piece.getCenter()
                x = center_point.getX()
                y = center_point.getY()
                x2, y2 = self.get_coor(to_sq)
                delta_x = x2 - x
                delta_y = y2 - y
                self.slow_animate(delta_x, delta_y, piece)
                if self.main_board[to_sq].is_occupied():
                    piece2 = self.main_board[to_sq].remove_piece()
                    piece2.undraw()
                self.main_board[to_sq].add_piece(piece)
        elif start_list is self.blue_start:
            piece = self.blue_start.pop()
            if to_sq == 45:
                center_point = piece.getCenter()
                x = center_point.getX()
                y = center_point.getY()
                x2, y2 = self.get_coor(to_sq)
                delta_x = x2 - x
                delta_y = y2 - y
                self.fast_animate(delta_x, delta_y, piece)
                if self.main_board[to_sq].is_occupied():
                    piece2 = self.main_board[to_sq].remove_piece()
                    piece2.undraw()
                self.main_board[to_sq].add_piece(piece)
            else:
                center_point = piece.getCenter()
                x = center_point.getX()
                y = center_point.getY()
                x2, y2 = self.get_coor(to_sq)
                delta_x = x2 - x
                delta_y = y2 - y
                self.slow_animate(delta_x, delta_y, piece)
                if self.main_board[to_sq].is_occupied():
                    piece2 = self.main_board[to_sq].remove_piece()
                    piece2.undraw()
                self.main_board[to_sq].add_piece(piece)

    def fast_animate(self, delta_x, delta_y, piece):
        """
        Does: helper function to animate from start
        """
        move_x = delta_x / FRAMES2
        move_y = delta_y / FRAMES2
        for i in range(FRAMES2):
            piece.move(move_x, move_y)
            update()

    def slow_animate(self, delta_x, delta_y, piece):
        """
        Does: helper function to animate from start and trading pieces
        """
        move_x = delta_x / FRAMES3
        move_y = delta_y / FRAMES3
        for i in range(FRAMES3):
            piece.move(move_x, move_y)
            update()

    def trade_pieces(self, from_sq, to_sq):
        """
        Does: animates the trading of pieces on the main board
        """
        piece1 = self.main_board[from_sq].remove_piece()
        piece2 = self.main_board[to_sq].remove_piece()
        x1, y1 = self.get_coor(from_sq)
        x2, y2 = self.get_coor(to_sq)
        delta_x1 = x2 - x1
        delta_y1 = y2 - y1
        delta_x2 = x1 - x2
        delta_y2 = y1 - y2
        self.slow_animate(delta_x1, delta_y1, piece1)
        self.main_board[to_sq].add_piece(piece1)
        self.slow_animate(delta_x2, delta_y2, piece2)
        self.main_board[from_sq].add_piece(piece2)

    def animate_piece(self, from_block, to_block, piece):
        """
        Does: helper method that animates movement of piece by one space
        """
        if from_block == 59 and to_block == 0:
            # move left
            self.move_left(piece)
            return
        if from_block == 0 and to_block == 59:
            # move right
            self.move_right(piece)
            return
        if from_block == 58 and to_block == 100:
            # move up
            self.move_up(piece)
            return
        if from_block == 100 and to_block == 58:
            # move down
            self.move_down(piece)
            return
        if from_block == 13 and to_block == 200:
            # move right
            self.move_right(piece)
            return
        if from_block == 200 and to_block == 13:
            # move left
            self.move_left(piece)
            return
        if from_block == 28 and to_block == 300:
            # move down
            self.move_down(piece)
            return
        if from_block == 300 and to_block == 28:
            # move up
            self.move_up(piece)
            return
        if from_block == 43 and to_block == 400:
            # move left
            self.move_left(piece)
            return
        if from_block == 400 and to_block == 43:
            # move right
            self.move_right(piece)
            return
        if to_block > from_block:
            # moving forward
            if 0 <= from_block <= 10:
                # move left
                self.move_left(piece)
            elif 11 <= from_block <= 25:
                # move up
                self.move_up(piece)
            elif 26 <= from_block <= 40:
                # move right
                self.move_right(piece)
            elif 41 <= from_block <= 55:
                # move down
                self.move_down(piece)
            elif 56 <= from_block <= 58:
                # move left
                self.move_left(piece)
            elif 100 <= from_block <= 105:
                # move up
                self.move_up(piece)
            elif 200 <= from_block <= 205:
                # move right
                self.move_right(piece)
            elif 300 <= from_block <= 305:
                # move down
                self.move_down(piece)
            elif 400 <= from_block <= 405:
                # move left
                self.move_left(piece)
        elif to_block < from_block:
            # moving backward
            if 1 <= from_block <= 11:
                # move right
                self.move_right(piece)
            elif 12 <= from_block <= 26:
                # move down
                self.move_down(piece)
            elif 27 <= from_block <= 41:
                # move left
                self.move_left(piece)
            elif 42 <= from_block <= 56:
                # move up
                self.move_up(piece)
            elif 57 <= from_block <= 59:
                # move right
                self.move_right(piece)
            elif 100 <= from_block <= 104:
                # move down
                self.move_down(piece)
            elif 200 <= from_block <= 204:
                # move left
                self.move_left(piece)
            elif 300 <= from_block <= 304:
                # move up
                self.move_up(piece)
            elif 400 <= from_block <= 404:
                # move right
                self.move_right(piece)
        return

    def move_left(self, piece):
        """
        Does: helper for animate_piece()
        """
        x = - 58 / FRAMES
        y = 0
        for i in range(FRAMES):
            piece.move(x, y)
            update()

    def move_right(self, piece):
        """
        Does: helper for animate_piece()
        """
        x = 58 / FRAMES
        y = 0
        for i in range(FRAMES):
            piece.move(x, y)
            update()

    def move_up(self, piece):
        """
        Does: helper for animate_piece()
        """
        x = 0
        y = - 58 / FRAMES
        for i in range(FRAMES):
            piece.move(x, y)
            update()

    def move_down(self, piece):
        """
        Does: helper for animate_piece()
        """
        x = 0
        y = 58 / FRAMES
        for i in range(FRAMES):
            piece.move(x, y)
            update()

    def get_coor(self, block):
        """
        Does: returns x, y coordinates of center of block, needed for SORRY moves
        and trading pieces
        Returns: x, y coordinates
        """
        for i in range(0, 12):
            if block == i:
                return 679 - 58 * i, 911
        for i in range(12, 27):
            if block == i:
                return 41, 853 - 58 * (i - 12)
        for i in range(27, 42):
            if block == i:
                return 99 + 58 * (i - 27), 41
        for i in range(42, 57):
            if block == i:
                return 911, 99 + 58 * (i - 42)
        for i in range(57, 60):
            if block == i:
                return 853 - 58 * (i - 57), 911

    def slide(self, from_sq, num_spaces):
        """
        Does: performs a slide for given number of spaces
        """
        for i in range(num_spaces):
            new_sq = (from_sq + i) % 60
            self.move_piece(self.main_board, new_sq, self.main_board,
                            (new_sq + 1) % 60)




