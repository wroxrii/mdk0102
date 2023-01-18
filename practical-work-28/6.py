s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 7:box 17:star'
sp = [x.split(':') for x in s.split()]
r = {x[1]: int(x[0]) for x in sp}
print(r)
