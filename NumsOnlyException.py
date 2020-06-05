class NumsOnlyError(TypeError):
    def __init__(self, message='Элемент не является числом'):
        self.message = message
        self.the_list = []

    def work(self):
        while True:
            el = input('Введите число или "q" для выхода: ')
            if el == 'q':
                break
            try:
                if not el.isdigit():
                    raise NumsOnlyError(self.message)
                else:
                    self.the_list.append(el)
            except NumsOnlyError as e:
                print(e)
                continue
        print(self.the_list)

num = NumsOnlyError().work()