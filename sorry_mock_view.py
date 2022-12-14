# sorry_mock_view.py
# This is a mock up view for sorry

from graphics import *

class sorryMockView():
    def __init__(self):
        self.win = GraphWin("Sorry", 952, 952)
        self.win.setBackground('lightblue')
        self.draw_board()
        self.main_text = Text(Point(476, 476), 'Sorry!')

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

    def display_cards(self):
        img = Image(Point(476, 476 + 128), 'one_card.gif')
        img.draw(self.win)
        img2 = Image(Point(476, 476 - 128), 'back_of_card.gif')
        img2.draw(self.win)

    def display_main_text(self):
        self.main_text.undraw()
        self.main_text.setText('SORRY!')
        self.main_text.setFace('courier')
        self.main_text.setSize(36)
        self.main_text.setStyle('bold')
        self.main_text.draw(self.win)
        
        


def main():
    view = sorryMockView()
    view.display_cards()
    view.display_main_text()

main()
