# sorry_main
# This is the 'main' function which starts a multi-player game of SORRY!

from sorry_model import *
from sorry_view import *
from sorry_controller import *


def main():
    num_players = 0
    while not (num_players == 2 or num_players == 3 or num_players == 4):
        input_str = input('Please enter number of players: 2, 3, or 4\n')
        if input_str == '2' or input_str == '3' or input_str == '4':
            num_players = int(input_str)
            
    model = sorryModel(num_players)
    view = sorryView()
    controller = sorryController(model, view, num_players)

    update()
    
    try:
        controller.play_sorry()
    except GraphicsError:
        print("Window closed.")
    except:
        import traceback
        # printing stack trace
        traceback.print_exc()


main()
