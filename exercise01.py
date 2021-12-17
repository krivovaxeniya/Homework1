class Data:
    def __init__(self, data):
        self.data = data.split('-')

    @classmethod
    def data_int(cls, data):
        day, month, year = [int(i) for i in data.split('-')]
        print(day, month, year)

    @staticmethod
    def data_valid(data):
        day, month, year = [int(i) for i in data.split('-')]
        if day > 31 or day < 1 or month < 1 or month > 12 or year < 0:
            print('Некорректная дата!')
        else:
            print(data)


Data.data_int('19-10-2021')
Data.data_valid('39-10-2021')
