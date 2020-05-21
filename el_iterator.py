from itertools import cycle
from random import randint

""" Запускается без параметров"""

cycle_list = [i + randint(0, 10) for i in range(10)]
i = 1
print('Дарю тебе 10 случайных интов:')
for el in cycle(cycle_list):
    if i > 10:
        break
    print(f'{i}: ', el)
    i += 1