import re
import sys

sys.stdin = open('code_example2.py', encoding='utf-8')

for line in sys.stdin:
    if re.findall(r'^\s+#|^#', line):
        pass
    else:
        sys.stdout.write(f'{line}')
