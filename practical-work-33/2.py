fileName = input('Введите название файла: ')

try:
    with open(fileName, encoding='utf-8') as file:
        print(file.read(), '\n')
        print('Чтение из файла прошло успешно!')
except FileNotFoundError:
    print('Файл не найден.')

# В папке с файлами должен быть файл nothing.txt
# Формат ввода 1
# nothing.txt
# Формат ввода 2
# grades.txt
