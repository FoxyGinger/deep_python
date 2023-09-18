# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.


def number_to_hex(number):
    if number == 0:
        return "0x0"

    prefix = "0x"
    if number < 0:
        prefix = "-" + prefix
        number = abs(number)

    hex_digits = "0123456789abcdef"
    result = ""
    while number > 0:
        result = hex_digits[number % 16] + result
        number = number // 16

    return prefix + result


for number in [0, 127, -127, 32267, -32201]:
    hex1 = number_to_hex(number)
    hex2 = hex(number)
    print(f'{hex1} = {hex2}(builtin)')
