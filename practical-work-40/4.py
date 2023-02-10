import re
import sys

sys.stdin = open('code_example.py', encoding='utf-8')

comments = 0

for line in sys.stdin:
    if re.findall(r'^\s+#|^#', line):
        comments += 1

sys.stdout.write(f'{comments}')
