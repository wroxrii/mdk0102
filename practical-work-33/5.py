import re

domains = {
    'yandex.ru': 1,
    'gmail.com': 1,
    'mail.ru': 1,
}

email = input()

domain = re.search(r'(?<=@)\w+\.\w+', email).group()

try:
    domains[domain] += 1
    with open('email.txt', 'w+', encoding='utf-8') as file:
        file.write(email)
    print('Почта успешно записана в файл email.txt!')
except KeyError:
    print('Почта должна относиться к почтовому серверу yandex.ru, gmail.com, mail.ru!')
