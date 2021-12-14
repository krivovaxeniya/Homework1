class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        return '\n'.join(map(str, self.my_list))

    def __add__(self, other):
        sum_list = []
        for i in range(len(self.my_list)):
            sum_list.append([])
            for j in range(len(other.my_list[i])):
                sum_list[i].append(self.my_list[i][j] + other.my_list[i][j])
        return '\n'.join(map(str, sum_list))

matrix_1 = Matrix([[1, 2, 3], [-1, -3, 0], [2, 0, -2]])
matrix_2 = Matrix([[3, 2, 1], [0, -1, 2], [-1, 0, 1]])
print(matrix_1 + matrix_2)
