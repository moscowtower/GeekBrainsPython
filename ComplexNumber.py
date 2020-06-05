
class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        return f'{self.real} + {self.imaginary}i'

    def __add__(self, other):
        return f'{self.real + other.real} + {self.imaginary + other.imaginary}i'

    def __sub__(self, other):
        return f'{self.real - other.real} + {self.imaginary - other.imaginary}i'

    def __mul__(self, other):
        first_part = f'{(self.real * other.real) - (self.imaginary * other.imaginary)}'
        second_part = f'{(self.real * other.imaginary) + (self.imaginary * other.real)}i'
        return  first_part + ('+' if second_part[0]!='-' else '') + second_part
x = ComplexNumber(4, -7)
y = ComplexNumber(2, -3)
print(x*y)
print(complex(4, -7) * complex(2, -3))