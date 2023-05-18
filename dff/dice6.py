import random


class Person:
    def __init__(self, name, room) -> None:
        self.name = name
        self.room = room

    def __del__(self):
        print(f'{self.name} умер в {self.room}')

    def __str__(self) -> str:
        return f'{self.name} находится в {self.room}'

    def __lt__(self, other: 'Person'):
        return self.room == other.room


persons = [
    Person('Валера', 'гостинной'),
    Person('Сергей', 'спальне'),
    Person('Санек', 'столовой')
]

rooms = ['кухне', 'спальне', 'гостинной', 'столовой']
a = ''
while len(persons) != 1:
    for i in range(len(persons) - 1):
        persons[i].room = random.choice(rooms)
        print(persons[i])
        if persons[i].room == a:
            del persons[i]
        a = persons[i].room
        input()
