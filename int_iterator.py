from itertools import count
from sys import argv

""" Запускается с тремя параметрами - имя, начальное число и финальное"""

try:
    script_name, start, end = argv

    for el in count(int(start)):
        if el <= int(end):
            print(el)
        else:
            break
except ValueError:
    print("Требуется три параметра - имя, начальное число и финальное!")