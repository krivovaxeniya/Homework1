class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} едет')

    def stop(self):
        print(f'{self.name} стоит')

    def turn(self, direction):
        self.direction = direction
        print(f'{self.name} повернула {direction}')

    def show_speed(self):
        print(f'Скорость {self.name} = {self.speed}')

class TownCar(Car):
    def show_speed(self):
        if int(self.speed) > 60:
            print(f'Скорость {self.name} первышена!')
        else:
            print(f'Скорость {self.name} = {self.speed}')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if int(self.speed) > 40:
            print(f'Скорость {self.name} первышена!')
        else:
            print(f'Скорость {self.name} = {self.speed}')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police = True):
        super().__init__(speed, color, name, is_police)

town = TownCar('70', 'white', 'Kia', False)
town.go()
town.show_speed()
town.turn('налево')
town.stop()

work = WorkCar('30', 'white', 'ВАЗ', False)
work.go()
work.show_speed()
work.turn('направо')
work.stop()
