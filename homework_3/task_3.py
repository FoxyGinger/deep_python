# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.


ITEMS = {
    "Палатка": 10,
    "Посуда": 5,
    "Топор": 3,
    "Вода": 2,
    "Аптечка": 1
}


def get_possible_items(max_weight, items):
    possible_items = []
    sorted_items = sorted(items.items(), key=lambda item: item[1], reverse=True)
    for item_name, item_weight in sorted_items:
        if max_weight >= item_weight:
            possible_items.append(item_name)
            max_weight -= item_weight

    return possible_items


print(get_possible_items(21, ITEMS))
print(get_possible_items(20, ITEMS))
print(get_possible_items(19, ITEMS))
print(get_possible_items(18, ITEMS))
