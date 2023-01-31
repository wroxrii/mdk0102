result = {
    'int': 0,
    'no_int': 0,
}

for i in range(int(input())):
    try:
        result['int'] += float(input())
    except ValueError:
        result['no_int'] += 1

print(result['int'])
print(result['no_int'])
