class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина тронулась с места.')

    def stop(self):
        print('Машина остановилась.')

    def turn(self, direction):
        print(f'Машина повернула {direction}.')

    def show_speed(self):
        print(f'Скорость = {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if int(self.speed) > 60:
            print('Превышение скорости.')

class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if int(self.speed) > 40:
            print('Превышение скорости.')

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)

class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

base_car = Car(15, 'white', 'Телега')
print('Базовый класс: ')
base_car.go()
base_car.stop()
base_car.turn('налево')
base_car.show_speed()

for key, value in base_car.__dict__.items():
    print(f'Аттрибут: {key}, Значение: {value}')
print('\n')

town_car = TownCar(100, 'black', 'Toyota')
print('Town Car: ')
town_car.go()
town_car.stop()
town_car.turn('налево')
town_car.show_speed()

for key, value in town_car.__dict__.items():
    print(f'Аттрибут: {key}, Значение: {value}')
print('\n')

work_car = WorkCar(39, 'yellow', 'Kia')
print('Work Car: ')
work_car.go()
work_car.stop()
work_car.turn('налево')
work_car.show_speed()

for key, value in work_car.__dict__.items():
    print(f'Аттрибут: {key}, Значение: {value}')
print('\n')

police_car = PoliceCar(666,'black and white', 'Жигули')
print('Police Car: ')
police_car.go()
police_car.stop()
police_car.turn('налево')
police_car.show_speed()

for key, value in police_car.__dict__.items():
    print(f'Аттрибут: {key}, Значение: {value}')