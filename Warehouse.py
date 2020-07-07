from random import choice

class Warehouse:
    types = ['Printer', 'Scanner', 'Xerox']
    sklad = {}
    departments = ['HR', 'R&D', 'Маркетинг', 'Бухгалтерия', 'Финансов', 'Контроля Качества']

    @classmethod
    def tech_reception(cls, other):
        try:
            if other.type not in cls.types:
                raise UserWarning('Мы такое не складируем.')
            else:
                if other.model in cls.sklad:
                    cls.sklad[other.model][1]+=other.amount
                else:
                    cls.sklad[other.model] = [other.type, other.amount]
                print(f'Техника {other.model} принята на склад. '
                      f'Количество этой техники на складе: {cls.sklad[other.model][1]}')
        except UserWarning as e:
            print(e)

    @classmethod
    def tech_distribution(cls):
        for model, item in cls.sklad.items():
            the_type = item[0]
            if the_type == 'Printer':
                if cls.sklad[model][1] == 0:
                    print(f'Нет техники {model} для отправки')
                else:
                    cls.sklad[model][1]-=1
                    print(f'Техника {model} упакована и отправлена в отдел {choice(cls.departments)}')
            if the_type == 'Scanner':
                if cls.sklad[model][1] == 0:
                    print(f'Нет техники {model} для отправки')
                else:
                    cls.sklad[model][1]-=1
                    print(f'Техника {model} упакована и отправлена в отдел {choice(cls.departments)}')
            if the_type == 'Xerox':
                if cls.sklad[model][1] == 0:
                    print(f'Нет техники {model} для отправки')
                else:
                    cls.sklad[model][1] -= 1
                    print(f'Техника {model} упакована и отправлена в отдел {choice(cls.departments)}')
        print()



class OfficeTech():
    def __init__(self, model, amount, type):
        self.model = model
        self.type = type
        # StackOverflow единогласно аппелирует за выдачу встроенной ValueError при проблемах в __init__
        # Также обработка ошибки приводит к AttributeError в методе Warehouse.tech_reception
        self.amount = int(amount)



class Printer(OfficeTech):
    def __init__(self, model, colored_ink_level, black_ink_level, amount, type='Printer'):
        super().__init__(model, amount, type=type)
        self.colored_ink_level = colored_ink_level
        self.black_ink_level = black_ink_level



class Scanner(OfficeTech):
    def __init__(self, model, speed, amount, type='Scanner'):
        super().__init__(model, amount, type=type)
        self.speed = speed
        self.amount = amount


class Xerox(OfficeTech):
    def __init__(self, model, black_ink_level, amount, type='Xerox'):
        super().__init__(model, amount,  type=type)
        self.black_ink_level = black_ink_level
        self.amount = amount


class FakeiPhone(OfficeTech):
    def __init__(self, model, amount, type='Fake iPhone'):
        super().__init__(model, amount,  type=type,)
        self.amount = amount


pri = Printer('Picaso Designer XL', 12, 23, 5)
pri2 = Printer('HP DeskJet', 111, 23, 4)
sca = Scanner('CanScan LiDE 200', 7, 4)
xer = Xerox('Xerox Versant 180 Press', 55, 5)
iph = FakeiPhone('BeijingPhone', 100000)


# Вносим товары в список для отправки на склад
spisok = [pri, pri2, sca, xer, iph]
for el in spisok:
    Warehouse.tech_reception(el)
print()
# Находим максимальное кол-во опредленной техники
# Мы ведь хотим отправить все, правда?

checker = []
for value in Warehouse.sklad.values():
    checker.append(value[1])
iterations = max(checker)

# Прогоняем распределение техники столько раз, сколько требуется для полного распределения склада
for i in range(iterations):
    Warehouse.tech_distribution()

print('\nВся техника отправлена. Склад пуст:')
for el, vel in Warehouse.sklad.items():
    print(el, vel)