import games 

def game_choice():
    command = input('1. Игры')
    if command == 'Давай поиграем':
        print('Вот игры в которые я умею играть: ')
        print('1. Выбрать героя')
        print('2. Математическая игра')
        game = int(input('Выбери игру напишите её порядковый номер: '))
    if game == 1:
        games.picker()
    if game == 2:
        games.math_test()
        
if __name__ == '__main__':
    game_choice()
    