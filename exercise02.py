class Zero:
    def __init__(self, divident, divisor):
        self.divident = divident
        self.divisor = divisor

    @staticmethod
    def div(divident, divisor):
        try:
            print(f'Частное = {divident/divisor}')
        except ValueError:
            print('Необходимо ввести число')
        except TypeError:
            print('Необходимо ввести число')
        except ZeroDivisionError:
            print('На ноль делить нельзя')

Zero.div(10, 0)