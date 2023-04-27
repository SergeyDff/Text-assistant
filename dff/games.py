import random
import time
from datetime import datetime
import main
import keyboard
    
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
    time.sleep(1)
    print('1. Играть еще')
    print('2. Выйти')
    if int(input()) == 1:
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
    time.sleep(1)
    command = int(input())
    if  command == 1:
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
#==============================================LETTER PICK=====================================
def letter_pick():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    correct_letter = 0
    for i in range(1,10):
        a = random.randint(1,26)
        time.sleep(1)
        print(letters[a])
        if keyboard.read_key() == letters[a]:
            print('Правильно!')
            correct_letter = int(correct_letter + 1)
        else:
            print('Неправильно!')
    print(f'У вас {correct_letter} правильных нажатий')
    print('1. Играть еще')
    print('2. Выйти')
    if int(input()) == 1:
       letter_pick()
    else:
       main.game_choice()

if __name__ == '__main__':
    letter_pick()
#==============================================NOTES============================================
def notes():
    print('===КОМАНДЫ===') 
    print('1. Добавить заметку')
    print('2. Удалить заметки')
    print('3. Прочесть все заметки')
    command = int(input())
    if command == 1:
        f = open('Notes.txt', 'a')
        f.write(input('Что напишем? '))
        f.close()
        notes()

    if command == 2:
        f = open('Notes.txt', 'w')
        f.close()
        notes()
    if command == 3:
        f = open('Notes.txt', 'r')
        print(f.read())
        f.close()
        notes()