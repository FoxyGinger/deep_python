# Напишите функцию для транспонирования матрицы. Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]


def transpose_matrix(matrix):
    if len(matrix) == 0:
        return []

    line_size = len(matrix[0])
    for line in matrix:
        if len(line) != line_size:
            print(f'{matrix} - не является матрицей')
            return []

    new_matrix = []
    for i in range(len(matrix[0])):
        line = []
        for j in range(len(matrix)):
            line.append(matrix[j][i])

        new_matrix.append(line)

    return new_matrix


print(transpose_matrix([[1, 2, 3], [4, 5, 6]]))  # [[1,4], [2,5], [3, 6]]
print(transpose_matrix([]))  # []
print(transpose_matrix([[1, 2, 3], [4, 5], [1]]))  # не является матрицей
