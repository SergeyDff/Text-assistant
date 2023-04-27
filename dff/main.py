import games 
import keyboard
def game_choice():
    print('Вот что я умею: ')
    print('1. Выбрать героя')
    print('2. Математическая игра')
    if int(keyboard.read_key()) == 1:
        games.picker()
    if int(keyboard.read_key()) == 2:
        games.math_test()
        
if __name__ == '__main__':
    game_choice()

