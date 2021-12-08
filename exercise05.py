class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pencil(Stationery):
    def draw(self):
        print(f'Используется {self.title}. Неяркая отрисовка')

class Pen(Stationery):
    def draw(self):
        print(f'Используется {self.title}. Яркая отрисовка')

class Handle(Stationery):
    def draw(self):
        print(f'Используется {self.title}. Яркая отрисовка, вообще жесть!')

pencil = Pencil('карандаш')
pencil.draw()
pen = Pen('ручка')
pen.draw()
handle = Handle('маркер')
handle.draw()
