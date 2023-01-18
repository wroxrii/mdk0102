n = int(input('Введите количесвто книг: '))
arr = [[x for x in input().split(': ')] for z in range(n)]
d = {k: v for k, v in arr}
print(d)
