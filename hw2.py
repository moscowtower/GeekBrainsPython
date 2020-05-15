#1----------------------------------------------------------------------------------------------------------------------
list = [1, 1.0, "String", True, None, ([] or {} or 0)]

def check_type(element):
    string = str(type(element))
    index = string.index("'")
    print(f"Тип {element}'а - {string[index+1:-2]}")

for element in list:
    check_type(element)

#2----------------------------------------------------------------------------------------------------------------------
list = []

def swap(list, a, b):
    list[a], list[b] = list[b], list[a]

while True:
    user_input = input("Введите значение для нового элемента или 'q' для завершения: ")
    if user_input == 'q':
        break
    else:
        list.append(user_input)
print('Начальный список: ', list)
try:
    for i in range(0, len(list), 2):
        swap(list, i, i+1)
except IndexError:  # плохая практика, но в этом случае не важно
    pass
print('Измененный список: ', list)

#3.1--------------------------------------------------------------------------------------------------------------------
# Решение через list
list = ["Зиме", "Весне", "Лету", "Осени"]
user_input = int(input('Введите номер месяца: '))
if user_input <= 0 or user_input > 12:
    print("Ошибка")
elif user_input < 3 or user_input == 12:
    print(f"{user_input}'й месяц относится к {list[0]}")
elif user_input < 6:
    print(f"{user_input}'й месяц относится к {list[1]}")
elif user_input < 9:
    print(f"{user_input}'й месяц относится к {list[2]}")
else:
    print(f"{user_input}'й месяц относится к {list[3]}")

#3.2--------------------------------------------------------------------------------------------------------------------
# Решение через dict
slovar = {"Зиме":[12, 1, 2], "Весне":[3, 4, 5], "Лету":[6, 7, 8], "Осени":[9, 10, 11]}

user_input = int(input("Введите номер месяца: "))

for key, value in slovar.items():
    if user_input in value:
        result = (f"{user_input}'s месяц относится к ", key)
        break
    else:
        result = 'Ошибка'
        continue
print("".join(result))

#4----------------------------------------------------------------------------------------------------------------------
lines = input("Введите несколько слов через пробел: ")
lines = lines.split()
for ind, line in enumerate(lines, 1):
    print(ind, line[:10])

#5----------------------------------------------------------------------------------------------------------------------
rating = [7, 5, 3, 3, 2]
print('Начальный рейтинг: ',rating)
new_element = int(input("Введите новый элемент для списка: "))

def put_new_element(element, list):
    if element > list[0]:
        list.insert(0, element)
    elif element < list[-1]:
        list.append(element)
    else:
        for i in range(len(list)):
            if element > list[i]:
                list.insert(i, element)
                break

if new_element in rating:
    position = rating.index(new_element) + rating.count(new_element)
    rating.insert(position, new_element)
else:
    put_new_element(new_element, rating)
print('Измененный рейтинг: ', rating)
#6----------------------------------------------------------------------------------------------------------------------
warehouse = []

def add_item(name='Без имени', price='Бесценно', amount='0', measuring='шт'):
    new_item={}
    new_item["Название"] = name
    new_item["Цена"] = price
    new_item["Количество"] = amount
    new_item["Ед. Изм."] = measuring
    return new_item

while True: #Ввод товаров
    name = input('Введите название товара: ')
    price = int(input('Введите цену товара: '))
    amount = int(input('Введите количество товара: '))
    measuring = input('Введите единицу измерения товара: ')
    warehouse.append(add_item(name, price, amount, measuring))
    fin = input('Товар добавлен. Добавить еще один товар? (д/н): ')
    if fin.lower() == 'н':
        break
warehouse = list(enumerate(warehouse, 1))
print("Структура: ", warehouse)
analysis = {}
names, prices, amounts, measurings = [], [], [], []
for i in range(len(warehouse)):
    names.append(warehouse[i][1].get("Название"))
    prices.append(warehouse[i][1].get("Цена"))
    amounts.append(warehouse[i][1].get("Количество"))
    measurings.append(warehouse[i][1].get("Ед. Изм."))

analysis["Название"] = names
analysis["Цена"] = prices
analysis["Количество"] = amounts
analysis["Единица Измерения"] = list(set(measurings))

print("Аналитика: ", analysis)
