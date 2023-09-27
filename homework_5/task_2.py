# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int, премия str с указанием процентов вида 10.25%.
# В результате result получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
#
# Сумма рассчитывается как ставка умноженная на процент премии.
#
# Не забудьте распечатать в конце результат.

# INPUT
# names = ["Alice", "Bob", "Charlie"]
# salary = [5000, 6000, 7000]
# bonus = ["10%", "5%", "15%"]
# OUTPUT
# {'Alice': 500.0, 'Bob': 300.0, 'Charlie': 1050.0}


def gen_dict(names: list[str], salary: list[int], bonus: list[str]):
    return {name: ((sal * int(bon.strip('%'))) / 100) for name, sal, bon in zip(names, salary, bonus)}


assert gen_dict(["Alice", "Bob", "Charlie"], [5000, 6000, 7000], ["10%", "5%", "15%"]) == {'Alice': 500.0, 'Bob': 300.0, 'Charlie': 1050.0}, gen_dict(["Alice", "Bob", "Charlie"], [5000, 6000, 7000], ["10%", "5%", "15%"])
assert gen_dict(["Eva", "David", "Frank"], [7500, 8000, 9000], ["8%", "12%", "7%"]) == {'Eva': 600.0, 'David': 960.0, 'Frank': 630.0}, gen_dict(["Eva", "David", "Frank"], [7500, 8000, 9000], ["8%", "12%", "7%"])
assert gen_dict(["Grace", "John", "Linda"], [6200, 5800, 7500], ["9%", "3%", "12%"]) == {'Grace': 558.0, 'John': 174.0, 'Linda': 900.0}, gen_dict(["Grace", "John", "Linda"], [6200, 5800, 7500], ["9%", "3%", "12%"])
