from datetime import datetime

'''                                                 
    БОЛЬШОЕ СПАСИБО МАРИЯ ЗА ВСЕ ВАШИ ЛЕКЦИИ
    ВЫ ПОТРЯСАЮЩЕ ЖОНГЛИРУЕТЕ ПЕДАГОГИЧЕСКИМИ ПРОЦЕССАМИ
'''

class Date:
    date = None
    def __init__(self, date):
        self.date = date
        Date.validate(Date.get_int_date(date))

    @classmethod
    def get_int_date(cls, date):
        cls.date = date
        temp = date.split('-')
        day, month, year = int(temp[0]), int(temp[1]), int(temp[2])
        return day, month, year

    @staticmethod
    def validate(date):
        day = date[0]
        month = date[1]
        year = date[2]
        try:
            if day > 31 or day < 1:
                raise UserWarning('Invalid day notation')
            if month > 12 or month < 1:
                raise UserWarning('Invalid day notation')
            if year < 1 or year > datetime.today().year:
                raise UserWarning('Years range from 0 to current year')
        except UserWarning as e:
            print(e)


date = Date('11-01-1997')
bad_date = Date('11-1111-111111')
print('Значение атрибута объекта:', date.date)
print('Проверка на int`овость: ', type(date.get_int_date('11-01-1997')[0]))
print('Значение атрибута класса:', Date.date)

