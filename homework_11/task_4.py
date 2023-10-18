class Matrix:
    rows: int
    cols: int
    data: list

    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.data = []
        for i in range(self.rows):
            row = [0 for _ in range(self.cols)]
            self.data.append(row)

    def __str__(self):
        output = ''
        for i in range(self.rows):
            for j in range(self.cols):
                output += f'{self.data[i][j]}'
                if j != self.cols - 1:
                    output += ' '

            if i != self.rows - 1:
                output += '\n'

        return output

    def __repr__(self):
        return f'Matrix({self.rows}, {self.cols})'

    def __eq__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            return False

        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j] != other.data[i][j]:
                    return False

        return True

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы имеют разные размеры")

        new_matrix = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                new_matrix.data[i][j] = self.data[i][j] + other.data[i][j]

        return new_matrix

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Количество столбцов в первой матрице не равно количеству строк во второй матрице")

        new_matrix = Matrix(self.rows, self.cols)
        for s in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    # print(f'[{s}][{j}] += {self.data[s][k] * other.data[k][j]} ')
                    new_matrix.data[s][j] += self.data[s][k] * other.data[k][j]

        return new_matrix



# # Создаем матрицы
matrix1 = Matrix(2, 3)
matrix1.data = [[1, 2, 3], [4, 5, 6]]

matrix2 = Matrix(2, 3)
matrix2.data = [[7, 8, 9], [10, 11, 12]]

# Выводим матрицы
print(matrix1)

print(matrix2)

# Сравниваем матрицы
print(matrix1 == matrix2)

# Выполняем операцию сложения матриц
matrix_sum = matrix1 + matrix2
print(matrix_sum)

# Выполняем операцию умножения матриц
matrix3 = Matrix(3, 2)
matrix3.data = [[1, 2], [3, 4], [5, 6]]

matrix4 = Matrix(2, 2)
matrix4.data = [[7, 8], [9, 10]]

print(matrix3)
print('')
print(matrix4)

print('')
result = matrix3 * matrix4
print('')
print(result)




