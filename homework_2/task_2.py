# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
from fractions import Fraction


def parse_fractional(fractional_str):
    numerator, denominator = fractional_str.split('/')

    return int(numerator), int(denominator)


def addition_and_multiplication(fractional_str1, fractional_str2):
    numerator1, denominator1 = parse_fractional(fractional_str1)
    numerator2, denominator2 = parse_fractional(fractional_str2)

    if denominator1 == 0 or denominator2 == 0:
        print("Знаменатель дроби не должен быть равен 0")
        return

    addition_result = (numerator1 * denominator2 + numerator2 * denominator1) / (denominator1 * denominator2)
    multiplication_result = (numerator1 * numerator2) / (denominator1 * denominator2)

    fract1 = Fraction(fractional_str1)
    fract2 = Fraction(fractional_str2)

    print(f'{fractional_str1} + {fractional_str2} = {addition_result}, fractions: {float((fract1 + fract2))}')
    print(f'{fractional_str1} * {fractional_str2} = {multiplication_result}, fractions: {float((fract1 * fract2))}')


addition_and_multiplication("1/2", "1/2")
addition_and_multiplication("-3/7", "11/17")
addition_and_multiplication("-5/9", "-6/11")
addition_and_multiplication("3/0", "1/2")
addition_and_multiplication("3/7", "-1/0")
