class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
    def calc_asphalt_mass(self, thickness):
        try:
            result = self._length * self._width * 25 * int(thickness) // 1000
            print('Требуемая масса асфальта:', result, 'тонн')
        except ValueError as e:
            print(e)

Doroga = Road(20, 5000)
Doroga.calc_asphalt_mass(input('Введите желаемую толщину асфальта(см): '))