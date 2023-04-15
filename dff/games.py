import random
import time
from datetime import datetime
import main

    
#===============================MATH GAME====================================================
def math_test():
    for i in range(5):
        first_number = random.randint(1, 10)
        second_number = random.randint(1, 10)
        sing_number = random.randint(0, 3)

        if sing_number == 0:
            result = first_number * second_number
            player_result = int(input(f'{first_number} * {second_number} '))

        if sing_number == 1:
            result = first_number / second_number
            player_result = int(input(f'{first_number} / {second_number} '))

        if sing_number == 2:
            result = first_number + second_number
            player_result = int(input(f'{first_number} + {second_number} '))


        if sing_number == 3:
            result = first_number - second_number
            player_result = int(input(f'{first_number} - {second_number} '))

        if result == player_result:
            print('Правильно!')
        else:
            print('Неправильно!')
    print('1. Играть еще')
    print('2. Выйти')
    next_com = input('Что делать дальше: ')
    if next_com == 1:
       math_test()
    else:
       main.game_choice()

if __name__ == '__main__':
    math_test()
#==================================PICKER===================================================
heroes = []
def picker():
  print('===КОМАНДЫ===') 
  print('1. ДОБАВИТЬ ГЕРОЯ')
  print('2. PICK')
  print('3. ESC')
  command = int(input('Выберите команду: '))
  if command == 1:
    ap_heroes = input(f'Напиши героя, которого ты хочешь добавить в список \n')
    heroes.append(ap_heroes)
    picker()
  if command == 2:
    pik_rand = random.randint(0, len(heroes) - 1) 
    print(heroes)
    print(heroes[pik_rand])
    picker()
  if command == 3:
    main.game_choice()
    
if __name__ == '__main__':
    picker()
#=============================================================================================