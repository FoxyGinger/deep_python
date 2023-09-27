# Создайте функцию генератор чисел Фибоначчи fibonacci.

# INPUT
# f = fibonacci()
# for i in range(10):
#     print(next(f))
# OUTPUT
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


f = fibonacci()
assert next(f) == 0
assert next(f) == 1
assert next(f) == 1
assert next(f) == 2
assert next(f) == 3
assert next(f) == 5
assert next(f) == 8
assert next(f) == 13
assert next(f) == 21
assert next(f) == 34
assert next(f) == 55
