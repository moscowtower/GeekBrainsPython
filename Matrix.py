class Matrix:
    def __init__(self, some_list):
        self.some_list = some_list

    def __str__(self):
        return '\n'.join(' '.join(map(str, row)) for row in self.some_list)

    def __add__(self, other):
        if len(self.some_list) != len(other.some_list):
            return UserWarning('Запрещено складывать матрицы разных размеров!')
        numbers = [other.some_list[i][j] + self.some_list[i][j] for i in range(len(self.some_list)) for j in
                   range(len(self.some_list[0]))]
        result = [numbers[i:i+len(self.some_list[0])] for i in range(0, len(self.some_list[0])*len(self.some_list), len(self.some_list[0]))]
        return Matrix(result)

user_matrix = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
bad_matrix = Matrix([[5, 2, 3], [6, 5, 3]])
print(user_matrix + bad_matrix)
print(user_matrix + user_matrix)
