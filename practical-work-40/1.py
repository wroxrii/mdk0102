import sys

strings = []

for line in sys.stdin:
    strings.append(''.join([i for i in line.strip('\n')[::-1]]))

for item in strings:
    sys.stdout.write(f'{item}\n')
