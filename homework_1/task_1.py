# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

ERROR = "Треугольника с такими сторонами не существует"
ISOSCELES = "Треугольник является равнобедренным"
EQUILATERAL = "Треугольник является равносторонним"
SCALENE = "Треугольник является разносторонним"


def check_triangle(a, b, c):
    if not a < (b + c):
        print(ERROR)
    elif not b < (a + c):
        print(ERROR)
    elif not c < (a + b):
        print(ERROR)
    else:
        if a == b == c:
            print(EQUILATERAL)
        elif a == b or b == c or a == c:
            print(ISOSCELES)
        else:
            print(SCALENE)


check_triangle(1, 6, 9)  # ERROR
check_triangle(3, 3, 3)  # EQUILATERAL
check_triangle(4, 4, 3)  # ISOSCELES
check_triangle(2, 4, 5)  # SCALENE
