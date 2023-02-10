import sys
import re

sys.stdin = open('news.txt', encoding='utf-8')

rows = []

for line in sys.stdin:
    rows.append(line.strip('\n'))

category = rows[-1]

for row in rows:
    try:
        if re.search(r'(?<=/ )\w+(?= /)', row).group() == category:
            result = re.search(r'.+(?= / \w+ )', row).group()
            sys.stdout.write(f'{result}\n')
    except AttributeError:
        pass
