import math


def quadratic_equation(a, b, c):
    d = 0
    try:
        a = int(a)
        b = int(b)
        c = int(c)
    except ValueError:
        print('Введены не корректные данные!')
        return False
    try:
        d = b ** 2 - 4 * a * c
        d2 = math.sqrt(d)
        x1 = (-b + d2) / int(2 * a)
        x2 = (-b - d2) / int(2 * a)
        print(f'x1 = {x1}, x2 = {x2}')
    except ValueError:
        print(f'd = {d}, так как d < 0, решений нет')
    except ZeroDivisionError:
        print(f'a = 0, уравнение не является квадратным')


quadratic_equation('c', 'b', 7)
quadratic_equation(1, 2, 7)
quadratic_equation(1, 2, 0)
quadratic_equation(0, 2, 8)
