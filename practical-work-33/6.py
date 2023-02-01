import re

ats = {
    '@': 1,
}

email = input()

try:
    at = re.search(r'@', email).group()
    ats[at] += 1
    with open('email.txt', 'w+', encoding='utf-8') as file:
        file.write(email)
    print('Почта успешно записана в файл email.txt!')
except AttributeError:
    print('Почта долна содержать символ @')
