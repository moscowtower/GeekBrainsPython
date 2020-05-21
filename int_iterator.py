from itertools import count
from sys import argv

""" Запускается с тремя параметрами - имя, начальное число и финальное"""

script_name, start, end = argv

for el in count(int(start)):
    if el <= int(end):
        print(el)
    else:
        break