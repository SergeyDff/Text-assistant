import games 
import keyboard
def game_choice():
    print('Вот что я умею: ')
    print('1. Выбрать героя')
    print('2. Математическая игра')
    print('3. Поиск буквы')
    command = int(input())
    if command == 1:
        games.picker()
    if command == 2:
        games.math_test()
    if command == 3:
        games.letter_pick()

if __name__ == '__main__':
    game_choice()