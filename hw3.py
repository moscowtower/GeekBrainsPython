#1----------------------------------------------------------------------------------------------------------------------
a = int(input('Введите делимое число: '))
b = int(input('Введите делитель: '))


def divide(a, b):
    """ Возвращает частное от деления и остаток, если он имеется """
    if a == 0 or b == 0:
        return 0
    else:
        divider = divmod(a, b)
        if divider[-1] == 0:
            print(f'Результат деления {a} на {b}: ',str(divider[0]))
        else:
            print(f'Результат деления {a} на {b}: ',str(divider[0]) + ', с остатком ' + str(divider[-1]), ' ≈ ', round(a/b))


divide(a, b)


#2----------------------------------------------------------------------------------------------------------------------
def profile(name, surname, yob, location, email, mobile):
    """ Возвращает однострочное представление введенных данных """
    print(f'Имя: {name}, Фамилия: {surname}, Год рождения: {yob}, Местоположение: {location}, E-mail: {email}, Телефон: {mobile}')


profile(mobile=88005553535, email='dont@me.com', location='поверхность Марса', yob=1337, surname='Сюр-нейм', name='НеСюр-нейм')


#3----------------------------------------------------------------------------------------------------------------------
def my_func(num1, num2, num3):
    """Возвращает сумму наибольших двух аргументов"""
    try:
        num1, num2, num3 = float(num1), float(num2), float(num3) #ради точности и случаев когда один из аргументов - float
        a = num1 if num1>num2 else num2
        b = num2 if num2>num3 else num3
        result = int(a + b)
        return result
    except ValueError:
        print("Ошибка: Аргументы должны быть численными")


result = my_func(-1, -5, -10)
print('Результат сложения двух самых больших аргументов: ', result)


#4.1--------------------------------------------------------------------------------------------------------------------
def my_func(x, y):
    """Возвращает x в степени -y"""
    x = int(x)
    y = abs(int(y))
    result = 1 / (x ** y)
    return result


print('Результат возведения числа x в степень y: ', my_func(5, -2))


#4.2--------------------------------------------------------------------------------------------------------------------
def my_func2(x, y):
    """Возвращает x в степени -y"""
    x = int(x)
    y = abs(int(y))
    for x in range(y):
        x *= x
    result = 1 / x
    return result


print('Результат возведения числа x в степень y: ', my_func(5, -2))


#5----------------------------------------------------------------------------------------------------------------------
def number_line():
    """Возвращает сумму введенных аргументов и прерывается после нахождения 'q' в input'е"""
    isGoing = True
    sum = 0

    while isGoing:
        line = input('Введите несколько чисел через пробел и нажмите Enter, чтобы получить их сумму. Введите q для выхода:')
        line = list(line.strip().split())

        if 'q' in line:
            line.pop(line.index('q'))
            isGoing = False
        for arg in line:
            sum += int(arg)
        print('Сумма = ', sum)
        continue
    return sum


number_line()


#6----------------------------------------------------------------------------------------------------------------------
def int_func(text):
    """Реализует функцию .title(), но через utf-8 штучки"""
    charlist = list(text)
    new_letter = chr(ord(text[0])-32)
    new_text = new_letter + text[1:]
    return str(new_text)


textline = list(input("Введите строку слов на латинице через пробел: ").lower().strip().split())
new_textline = ''
for el in textline:
    new_textline += int_func(el) + ' '
print(new_textline)

