import os
from generators import Generators
from gui import Gui
from model import Model



if __name__ == '__main__':
    path = os.path.abspath(os.path.dirname(__file__))

    for index, model in enumerate(Generators.__all__):
        print(f'{index+1:<{4}} : {model}')
    
    try:
        choice = int(input('\n> '))
    except ValueError:
        exit(print('choice must be an int'))
    finally:
        if not 0 < choice < len(Generators.__all__)+1:
            exit(print('choice out of range'))

        model = getattr(Generators, Generators.__all__[choice-1])()

    gui = Gui(path)
    gui.add_model(Model(**model))
    gui.main_loop()