s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 7:box 17:star'

splitted = [i.split(':') for i in s.split()]
result = {i[1]: int(i[0]) for i in splitted}

print(result)
