# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где
# ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем,
# используйте его строковое представление.
# reverse_kwargs(rev=True, acc="YES", stroka=4) -> {True: "rev", "YES": 'acc', 4: "stroka"}

def reverse_kwargs(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if value.__hash__ is None:
            str_value = str(value)
            result[str_value] = key
        else:
            result[value] = key

    return result


print(reverse_kwargs(rev=True, acc="YES", stroka=4, dddict={"1": 2}))
