# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.


WITHDRAW_PERCENT = 1.5
WITHDRAW_PERCENT_MIN_SUM = 30
WITHDRAW_PERCENT_MAX_SUM = 600
OPERATION_PERCENT = 3.0
OPERATION_PERCENT_COUNT = 3
TAX_SUM = 5000000
TAX_PERCENT = 10.0

ACCOUNT = 0
CURRENT_OPERATION_COUNT = 0
OPERATIONS = []


def get_operation_commission(summ):
    commission = 0
    if CURRENT_OPERATION_COUNT > OPERATION_PERCENT_COUNT:
        commission = (summ * OPERATION_PERCENT) / 100

    return commission


def get_withdraw_commission(summ):
    commission = (summ * WITHDRAW_PERCENT) / 100
    if commission < WITHDRAW_PERCENT_MIN_SUM:
        commission = WITHDRAW_PERCENT_MIN_SUM
    if commission > WITHDRAW_PERCENT_MAX_SUM:
        commission = WITHDRAW_PERCENT_MAX_SUM

    return commission


def withdraw(summ):
    global ACCOUNT
    update_account(summ)
    total_summ = summ + get_withdraw_commission(summ) + get_operation_commission(summ)
    if ACCOUNT < total_summ:
        print(f'Не хватает денег на счету для снятия {summ} + {total_summ - summ} комиссия')
        return

    ACCOUNT -= total_summ
    print(f'Снятие {summ} + {total_summ - summ} комиссия')
    OPERATIONS.append(f'Снятие: -{summ}')


def top_up(summ):
    global ACCOUNT
    update_account(summ)
    total_summ = summ - get_operation_commission(summ)

    ACCOUNT += total_summ
    print(f'Баланс пополнен на {total_summ} - {summ - total_summ} комиссия')
    OPERATIONS.append(f'Пополнение: +{summ}')


def update_account(summ):
    global ACCOUNT
    if ACCOUNT > TAX_SUM:
        tax = (summ * TAX_PERCENT) / 100
        if tax <= ACCOUNT:
            ACCOUNT -= tax
            print(f'Списан налог на богатство в размере: {tax}')


def menu():
    current_operation = 0
    while current_operation != 3:
        current_operation = int(input("Выберите операцию:\n1. Пополнение\n2. Снять\n3. Выйти\n"))
        if current_operation == 1:
            summ = int(input("Внесите сумму кратную 50: "))
            top_up(summ)
        elif current_operation == 2:
            summ = int(input("Введите сумму снятия кратную 50: "))
            withdraw(summ)

        print(f"Текущий баланс: {ACCOUNT}")

    print("До свидания!")


menu()
