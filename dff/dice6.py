import math

a = float(input('Введите коэффициент a: '))
b = float(input('Введите коэффициент b: '))
c = float(input('Введите коэффициент c: '))
d = b**2 - 4*a*c

if d < 0:
    print("Уравнение не имеет действительных корней")
elif d == 0:
    x1 = -b / (2*a)
    print("Уравнение имеет один корень: x =", x1)
else:
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    print("Уравнение имеет два корня: x1 =", x1, "x2 =", x2)
