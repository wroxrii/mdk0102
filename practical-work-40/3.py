import statistics
import sys

heights = []

for line in sys.stdin:
    heights.append(int(line.strip('\n')))

if len(heights) == 0:
    sys.stdout.write('Нет учеников!')
else:
    sys.stdout.write(f'Рост самого низкого ученика: {min(heights)}\n')
    sys.stdout.write(f'Рост самого высокого ученика: {max(heights)}\n')
    sys.stdout.write(f'Средний рост: {statistics.mean(heights)}')