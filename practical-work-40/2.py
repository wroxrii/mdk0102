import sys
import datetime

dates = []


def str_to_date(string):
    dates.append(datetime.datetime.strptime(string, '%Y-%m-%d'))


for line in sys.stdin:
    str_to_date(line.strip('\n'))

sys.stdout.write(f'{(max(dates) - min(dates)).days}')
