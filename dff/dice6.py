import random
import time


class Car:
    def __init__(self, name, speed, distance=500) -> None:
        self.name = name
        self.speed = speed
        self.distance = distance

    def __del__(self):
        print(f'{self.name} попадает в аварию и покидает гонку')

    def drive(self):
        self.distance -= self.speed

    def __str__(self) -> str:
        return f'{self.name} победил'


cars = [
    Car('BMW M5', random.randint(20, 28)),
    Car('Lamborghini', random.randint(24, 30)),
    Car('Honda NSX', random.randint(22, 32)),
    Car('Chevrolet Camaro', random.randint(20, 30))
]

while 
flag = True
while flag:
    for car in cars:
        car.drive()
        if car.distance < 0:
            print(car)
            flag = False
            break
