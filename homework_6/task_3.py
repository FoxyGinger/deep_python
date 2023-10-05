# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
#
# Под "успешной расстановкой ферзей" в данном контексте подразумевается такая расстановка ферзей на шахматной доске,
# в которой ни один ферзь не бьет другого. Другими словами, ферзи размещены таким образом, что они не находятся на одной вертикали, горизонтали или диагонали.
#
# Список из 4х комбинаций координат сохраните в board_list. Дополнительно печатать его не надо.
import random
from itertools import combinations


def is_attacking(q1, q2):
    # Проверяем, бьют ли ферзи друг друга
    return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])


def check_queens(queens):
    # Проверяем все возможные пары ферзей
    for q1, q2 in combinations(queens, 2):
        if is_attacking(q1, q2):
            return False

    return True


def generate_boards():
    positions_x = list(range(1, 9))
    positions_y = positions_x.copy()
    boards = []
    while len(boards) != 4:
        random.shuffle(positions_x)
        random.shuffle(positions_y)
        board = [(positions_x[i], positions_y[i]) for i in range(0, len(positions_x))]
        if check_queens(board):
            boards.append(board)

    return boards


assert len(generate_boards()) == 4


