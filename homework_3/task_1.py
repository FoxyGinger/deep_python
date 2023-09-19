# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
# [1, 2, 3, 1, 2] -> [1, 2]


def get_duplicates(collection):
    return list(set([elem for elem in collection if collection.count(elem) > 1]))


print(get_duplicates([1, 2, 3, 1, 2]))  # [1, 2]
print(get_duplicates([3, 3, 3, 1, 2]))  # [3]
print(get_duplicates([3, 1, 2]))  # []
