# там хижина изба машина и снова хижина машина или так
n = input().split()
arr = {x for x in n if len(x) > 3}
print(arr)
print(len(arr))
