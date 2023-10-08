'''
Напишите программу банкомат.
Начальная сумма равна нулю.
Допустимые действия: пополнить, снять, выйти.
Сумма пополнения и снятия кратны 50 у.е.
Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
После каждой третей операции пополнения или снятия начисляются проценты - 3%.
Нельзя снять больше, чем на счёте.
При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной.
Любое действие выводит сумму денег.
2. Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список.
'''
from typing import List


def bank(**kwargs):
    money = 0
    counter = 0
    while True:
        print("\n1.Пополнить счет")
        print("2.Снять средства")
        print("3.Выход")
        action = int(input("> Выберите действие: "))
        if action == 1:
            replenishment = []
            money += int(input("Сумма пополнения счета: "))
            if money <= 0:
                print('Недостаточно средств на счету.')
            elif money%50 == 0:
                counter += 1
                print('Сумма пополнения составила:', money)
                replenishment.append(money)
                if counter == 3:
                    money += money*0.03
                    print('Сумма с учетом 3% за попонение составляет: ', money)
                    replenishment.append(money)
                    counter = 0
            elif money%50 != 0:
                print('Сумма пополнения должна быть кратной 50 у.е.')

        elif action == 2:
            withdraw = []
            money -= int(input("Сколько снять средства: "))
            if money <= 0:
                print('Сумма снятия должна быть меньше или равной 0')
            elif money%50 == 0:
                counter += 1
                money -= money*0.015
                print('Сумма снятия c учетом процентов за снятие в 1.5% составила: ', money)
                withdraw.append(money)
                if counter == 3:
                    money += money*0.03
                    print('Сумма с учетом начисления в 3% за снятие составляет: ', money)
                    withdraw.append(money)
                    counter = 0
                if money >= 5000000:
                    money -= money*0.10
                    print('Сумма с учетом начисления налога на богатство в 10% составляет: ', money)
                    withdraw.append(money)
            elif money%50 != 0:
                print('Сумма снятия должна быть кратной 50 у.е.')

        elif action == 3:
            break
        else:
            print("Неверная операция. Попробуйте снова.")

    return [money, replenishment, withdraw in kwargs]

print(bank())
print(replenishment=bank())
print(withdraw=bank())