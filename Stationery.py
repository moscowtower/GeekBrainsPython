class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Рисует ручка!')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Рисует карандаш!')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Рисует фломастер!')

stationery = Stationery('Канцелярные принадлежности')
stationery.draw()

pen = Pen('Ручка')
pen.draw()

pencil = Pencil('Карандаш')
pencil.draw()

handle = Handle('Фломастер')
handle.draw()