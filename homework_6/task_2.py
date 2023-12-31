# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях, включающий в себя
# функцию is_attacking(q1,q2), проверяющую, бьют ли ферзи друг друга и heck_queens(queens), которая проверяет все возможные пары ферзей.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь. Не забудьте напечатать результат.


def check_queens(queens):
    queens_count = len(queens)
    for i in range(queens_count):
        x1, y1 = queens[i]
        for j in range(i + 1, queens_count):
            x2, y2 = queens[j]
            same_line = x1 == x2
            same_column = y1 == y2
            same_diagonal = x1 - y1 == x2 - y2 or x1 + y1 == x2 + y2
            if same_line or same_column or same_diagonal:
                return False

    return True


assert not check_queens([(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)])
assert not check_queens(queens=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)])
assert not check_queens(queens=[(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8)])
assert not check_queens(queens=[(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1)])
assert check_queens(queens=[])
assert check_queens(queens=[(4, 4)])
