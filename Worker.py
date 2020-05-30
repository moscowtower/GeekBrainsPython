class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage':wage, 'bonus':bonus}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'Имя - {self.name}, Фамилия - {self.surname}'

    def get_total_income(self):
        return f'Зарплата: {self._income["wage"]}, Премия: {self._income["bonus"]}'

Positia = Position('Vasya', 'Pupkin', 'Coder', 500, 50)

print(Positia.get_full_name())
print(Positia.get_total_income())