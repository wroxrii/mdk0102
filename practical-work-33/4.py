def personal_data(surname, direction, number):
    try:
        surname += ''
    except TypeError:
        print('Фамилия введена некорректно')
        return False
    try:
        direction += ''
    except TypeError:
        print('Направление подготовки задано некорректно')
        return False
    try:
        number += 2
    except TypeError:
        print('Номер зачетной книжки долен быть числом')
        return False
    with open('personal_data.txt', 'w+', encoding='utf-8') as file:
        file.write('{} {} {}'.format(surname, direction, number))


personal_data('Сидоров', 1, 74567)
personal_data(0, 'ПР', 74567)
personal_data('Сидоров', 'РПО', '74567')
personal_data('Сидоров', 'РПО', 74567)