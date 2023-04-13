import time
import random
def dice():
    i = 0
    correct_number = random.randint(1,6)
    player1 = int(input('Игрок 1 введите число от 1 до 6: '))
    player2 = int(input('Игрок 2 введите число от 1 до 6: '))
    if player1 == player2:
        print('====НИЧЬЯ====')
    if player1 :
        print('====ИГРОК1_ВЫЙГРАЛ====')
    if player2 == correct_number:
        print('====ИГРОК2_ВЫЙГРАЛ====')
    print('===ЧИСЛО_КОТОРОЕ_ВЫПАЛО===')
    while True:
        i = random.randint(1,10)
        print(f'==={i}===')
        time.sleep(1)
        if i == correct_number:
            break
        print ("\033[A                             \033[A")
        
if __name__ == '__main__':
    dice()