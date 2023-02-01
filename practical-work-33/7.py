import math as p

try:
    a = float(input())
    print(round(p.sin(a), 4))
except ValueError:
    print('Вычислить синус из строки невозможно')
finally:
    print('Спасибо, что использовали наш сервис!')

# Формат ввода 1
# строка
# Формат ввода 2
# 3.14
