import time
from termcolor import cprint

class TrafficLight:
    __color = 'red'
# Проверка правильности цикла не требуется, тк нет варианта при котором он бы нарушился #
    def running(self):
        while True:
            if self.__color == 'red':
                for i in range(7, -1, -1):
                    cprint(f'\rКрасный! \U0001F6A6 ({i})', 'red', end='')
                    time.sleep(1)
                self.__color = 'yellow'
            elif self.__color == 'yellow':
                for i in range(2, -1, -1):
                    cprint(f'\rЖелтый! \U0001F6A6 ({i})', 'yellow', end='')
                    time.sleep(1)
                self.__color = 'green'
            elif self.__color == 'green':
                for i in range(6, -1, -1):
                    cprint(f'\rЗеленый! \U0001F6A6 ({i})', 'green', end='')
                    time.sleep(1)
                self.__color = 'red'

Svetofor = TrafficLight()
Svetofor.running()