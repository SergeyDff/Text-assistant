import random
import time
from datetime import datetime

#==============================GUESS NUMBER=================================================
def guess_number(attemp = 0):
    random_number = random.randint(1, 10)
    my_number = 0
    while random_number != my_number:
        my_number = input('Отгадай число от 1 до 10, которое я загадал ')
        if random_number == my_number:
            print('Ты угадал : )')
        else:
            print('Ты проиграл : (')
            if attemp < 9:
                print('Попробуй еще раз')
        attemp += 1
        if attemp == 9:
            print('Слишком много попыток. Число которое я загадал это ', random_number)
            break

if __name__ == '__main__':
    guess_number()
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

    print(sum(mid_result)/len)
if __name__ == '__main__':
    math_test()
#==================================PICKER===================================================
def picker():
  heroes = []
  print('===КОМАНДЫ===') 
  print('1. ДОБАВИТЬ ГЕРОЯ')
  print('2. PICK')
  command = input('Выберите команду: ') 
  if command == 1:
    ap_heroes = input('Напиши героя, которого ты хочешь добавить в список')
    heroes.append(ap_heroes)
  if command == 2:
    pik_rand = random.randint(0, len(heroes) - 1) 
    print(*heroes)
    print(*heroes[pik_rand])

if __name__ == '__main__':
    picker()
#===========================================================================================