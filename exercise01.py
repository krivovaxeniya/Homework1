from time import sleep
class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        for el in TrafficLight.__color:
            print(el)
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            else:
                sleep(10)
            i += 1

a = TrafficLight()
a.running()
