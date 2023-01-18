n = int(input('Введите количесвто книг: '))
arr = [[x for x in input().split(': ')] for z in range(n)]
# отличие в:
# в 7 задании {k: v for...}
# в 8 задании {k for...} ↓
d = {k for k, v in arr}
print(d)
