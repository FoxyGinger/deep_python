# Вы работаете над разработкой программы для проверки корректности даты, введенной пользователем.
# На вход будет подаваться дата в формате "день.месяц.год". Ваша задача - создать программу, которая проверяет,
# является ли введенная дата корректной или нет.
#
# Ваша программа должна предоставить ответ "True" (дата корректна)
# или "False" (дата некорректна) в зависимости от результата проверки.
import datetime


def validate_date(date: str):
    valid = True
    try:
        datetime.datetime.strptime(date, '%d.%m.%Y')
    except ValueError:
        valid = False

    return valid


assert validate_date('15.4.2023')
assert not validate_date('31.6.2022')
assert not validate_date('0.5.2022')
assert not validate_date('12.0.2022')
assert not validate_date('12.5.-2022')
assert validate_date('29.2.2020')
assert validate_date('12.5.2022')
assert validate_date('28.2.2021')
assert validate_date('31.12.9999')
assert not validate_date('32.5.2022')
assert not validate_date('12.13.2022')
assert not validate_date('29.2.2021')
assert not validate_date('30.2.2020')



