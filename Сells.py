class Cell:
    def __init__(self, amount: int = 0):
        self.amount = amount

    def __add__(self, other):
        return self.amount + other.amount

    def __sub__(self, other):
        return self.amount - other.amount if self.amount - other.amount > 0 \
            else UserWarning('Разность двух клеток меньше 0')

    def __mul__(self, other):
        return self.amount * other.amount

    def __truediv__(self, other):
        return round(self.amount / other.amount)

    def make_order(self, cells: int = 0):
        return ('*' * cells + '\n') * (self.amount//cells) + '*' * (self.amount % cells)

cell1 = Cell(10)
cell2 = Cell(20)
cell3 = Cell(-1)

print(Cell.make_order(cell1, 6))