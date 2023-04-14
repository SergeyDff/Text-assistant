import random
import time
from datetime import datetime
import main

#===============================MATH GAME====================================================
def math_test():
    mid_result = []
    for i in range(5):
        first_number = random.randint(1, 10)
        second_number = random.randint(1, 10)
        sing_number = random.randint(0, 3)

        if sing_number == 0:
            start_time = datetime.now()
            result = first_number * second_number
            player_result = int(input(f'{first_number} * {second_number} '))
            finish_time = datetime.now()

        if sing_number == 1:
            start_time = datetime.now()
            result = first_number / second_number
            player_result = int(input(f'{first_number} / {second_number} '))
            finish_time = datetime.now()

        if sing_number == 2:
            start_time = datetime.now()
            result = first_number + second_number
            player_result = int(input(f'{first_number} + {second_number} '))
            finish_time = datetime.now()


        if sing_number == 3:
            start_time = datetime.now()
            result = first_number - second_number
            player_result = int(input(f'{first_number} - {second_number} '))
            finish_time = datetime.now()

        if result == player_result:
            print('Правильно!')
            mid_result.append(finish_time - start_time)
        else:
            print('Неправильно!')
    print('Твой результат за 5 примеров. Среднее время реакции: ')
    print(sum(mid_result)/len)
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
    ap_heroes = input('Напиши героя, которого ты хочешь добавить в список')
    heroes.append(ap_heroes)
    picker()
  if command == 2:
    pik_rand = random.randint(0, len(heroes) - 1) 
    print(*heroes)
    print(*heroes[pik_rand])
    picker()
  if command == 3:
    main.game_choice()
    
if __name__ == '__main__':
    picker()
#===========================================================================================