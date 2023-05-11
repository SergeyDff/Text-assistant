# import keyboard
# import turtle
# import time
# class Car:
#     def __init__(self,name,color,engine = 'Выключен', x = 0):
#         self.name = name
#         self.color = color
#         self.engine = engine
#         self.x = x
#     def engine_on(self):
#         self.engine = 'Включен'
#         self.engine = True
#         print('Двигатель запущен')
#     def engine_off(self):
#         self.engine = 'Выключен'
#         print('Двигатель неактивен')
#     def move(self):
#         if self.engine is True:
#             self.x += 1
#             print(f'Мы проехали 10км и оказались в {self.x}км от дома')
#             turtle.forward(1)
#         else:
#             print('Двигатель не запущен')

# bmw = Car('BMW', 'Black')
# audi = Car('Audi', 'Black')
# # bmw.engine_on()
# # bmw.engine_off()
# # print(f'Марка {bmw.name}, цвет {bmw.color}, статус двигателя {bmw.engine}')
# # bmw.move()
# #===============Управление машиной=================================================
# turtle.backward(300)
# while True:
#     if keyboard.is_pressed('w'):
#         bmw.move()
#         if bmw.engine is True:
#             turtle.forward(1)
#         time.sleep(0.01)
#     if keyboard.is_pressed('a'):
#         bmw.move()
#         if bmw.engine is True:
#             turtle.left(90)
#         time.sleep(0.01)
#     if keyboard.is_pressed('d'):
#         bmw.move()
#         if bmw.engine is True:
#             turtle.left(-90)
#         time.sleep(0.01)

#     if keyboard.is_pressed(','):
#         bmw.engine_on()
#         time.sleep(0.01)
#     if keyboard.is_pressed('.'):
#         bmw.engine_off()
#         time.sleep(0.01)
