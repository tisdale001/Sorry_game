# sorry_cards.py
# these are the classes for sorry cards
import random

class oneCard():
    def __init__(self):
        self.name = 'one_card.gif'
        self.face_up = False

    def get_name(self):
        if self.face_up == True:
            return self.name
        else:
            return 'back_of_card.gif'

    def set_face_up(self):
        self.face_up = True

class twoCard():
    def __init__(self):
        self.name = 'two_card.gif'
        self.face_up = False

    def get_name(self):
        if self.face_up == True:
            return self.name
        else:
            return 'back_of_card.gif'

    def set_face_up(self):
        self.face_up = True

class threeCard():
    def __init__(self):
        self.name = 'three_card.gif'
        self.face_up = False

    def get_name(self):
        if self.face_up == True:
            return self.name
        else:
            return 'back_of_card.gif'

    def set_face_up(self):
        self.face_up = True

class fourCard():
    def __init__(self):
        self.name = 'four_card.gif'
        self.face_up = False

    def get_name(self):
        if self.face_up == True:
            return self.name
        else:
            return 'back_of_card.gif'

    def set_face_up(self):
        self.face_up = True

class fiveCard():
    def __init__(self):
        self.name = 'five_card.gif'
        self.face_up = False

    def get_name(self):
        if self.face_up == True:
            return self.name
        else:
            return 'back_of_card.gif'

    def set_face_up(self):
        self.face_up = True

class sevenCard():
    def __init__(self):
        self.name = 'seven_card.gif'
        self.face_up = False

    def get_name(self):
        if self.face_up == True:
            return self.name
        else:
            return 'back_of_card.gif'

    def set_face_up(self):
        self.face_up = True

class eightCard():
    def __init__(self):
        self.name = 'eight_card.gif'
        self.face_up = False

    def get_name(self):
        if self.face_up == True:
            return self.name
        else:
            return 'back_of_card.gif'

    def set_face_up(self):
        self.face_up = True

class tenCard():
    def __init__(self):
        self.name = 'ten_card.gif'
        self.face_up = False

    def get_name(self):
        if self.face_up == True:
            return self.name
        else:
            return 'back_of_card.gif'

    def set_face_up(self):
        self.face_up = True

class elevenCard():
    def __init__(self):
        self.name = 'eleven_card.gif'
        self.face_up = False

    def get_name(self):
        if self.face_up == True:
            return self.name
        else:
            return 'back_of_card.gif'

    def set_face_up(self):
        self.face_up = True

class twelveCard():
    def __init__(self):
        self.name = 'twelve_card.gif'
        self.face_up = False

    def get_name(self):
        if self.face_up == True:
            return self.name
        else:
            return 'back_of_card.gif'

    def set_face_up(self):
        self.face_up = True

class sorryCard():
    def __init__(self):
        self.name = 'sorry_card.gif'
        self.face_up = False

    def get_name(self):
        if self.face_up == True:
            return self.name
        else:
            return 'back_of_card.gif'

    def set_face_up(self):
        self.face_up = True

class deck():
    def __init__(self):
        self.deck = self.shuffle_cards()

    def shuffle_cards(self):
        deck1 = []
        for i in range(4):
            deck1.append(oneCard())
            deck1.append(twoCard())
            deck1.append(threeCard())
            deck1.append(fourCard())
            deck1.append(fiveCard())
            deck1.append(sevenCard())
            deck1.append(eightCard())
            deck1.append(tenCard())
            deck1.append(elevenCard())
            deck1.append(twelveCard())
            deck1.append(sorryCard())
        # shuffle cards
        final_deck = []
        while deck1:
            index = random.randint(0, len(deck1) - 1)
            card = deck1.pop(index)
            final_deck.append(card)
        # return shuffled deck
        return final_deck
            
    def is_empty(self):
        if self.deck:
            return False
        else:
            return True

    def draw_card(self, to_pile):
        if self.deck:
            card = self.deck.pop()
            card.set_face_up()
            to_pile.append(card)
        else:
            print('Cannot draw from an empty deck.')
