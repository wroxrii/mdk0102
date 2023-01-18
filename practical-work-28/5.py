numbers = [34, 10, 23, 90, 100, 21, 35, 95, 1000, 13456, 360]
print({i: [int(k) for k in str(i)] for i in numbers})
