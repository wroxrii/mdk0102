import sys

numbers = []

for line in sys.stdin:
    numbers.append(int(line))

reversed_array = numbers[::-1]
progressive = reversed_array[0] - reversed_array[1]
size = len(numbers)

isProgressive = True

for i in range(size - 1):
    if reversed_array[i] - reversed_array[i + 1] == progressive:
        isProgressive = True
    else:
        isProgressive = False

if isProgressive:
    sys.stdout.write('Арифметическая прогрессия')
else:
    sys.stdout.write('Не прогрессия')