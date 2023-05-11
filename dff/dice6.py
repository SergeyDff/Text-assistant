import random
import time


class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100
   
    def attack(self, enemy):
        print(f"{self.name} атакует {enemy.name}")
        enemy.health -= 20
        print(f"{enemy.name} осталось {enemy.health} здоровья")
  

warrior_1 = Warrior('Выдра')
warrior_2 = Warrior('Бобр')

while warrior_1.health > 0 and warrior_2.health > 0:
    attacker, defender = random.sample([warrior_1, warrior_2], k=2)
    attacker.attack(defender)
    time.sleep(0.3)

if warrior_1.health > 0:
    print(f"{warrior_1.name} побеждает!")
else:
    print(f"{warrior_2.name} побеждает!(Бобры лучшие)")
