from random import choice

def fn9ne():
    return 'This code was been authored by fN9ne!'


fn9ne()


def critChance(chance):
    arr = [0] * 100
    for item in range(chance):
        arr[item] = 1
    return True if choice(arr) else False


print(critChance(20))
