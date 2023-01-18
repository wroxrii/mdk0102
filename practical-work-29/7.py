n = int(input('Введите количесвто книг: '))
array = [[item for item in input().split(': ')] for i in range(n)]
dictionary = {k: v for k, v in array}

print(dictionary)
