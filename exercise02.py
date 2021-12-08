class Road:
    _length = 0
    _width = 0
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.massa = 25
        self.count = 5

    def calc(self):
        all_massa = (self._length * self._width * self.massa * self.count)/1000
        print(f'Для покрытия дорожного полотна необходимо: {all_massa} тонн асфальта')

a = Road(5000, 20)
a.calc()
