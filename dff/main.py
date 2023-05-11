import games


def game_choice():
    print('Вот что я умею: ')
    print('1. Выбрать героя')
    print('2. Математическая игра')
    print('3. Поиск буквы')
    print('4. Заметки')
    command = int(input())
    if command == 1:
        games.picker()
    if command == 2:
        games.math_test()
    if command == 3:
        games.letter_pick()
    if command == 4:
        games.notes()


if __name__ == '__main__':
    game_choice()