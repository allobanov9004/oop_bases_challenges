"""
Мы научились увеличивать баланс у банковского аккаунта, но иногда нам нужно и уменьшать его.

Задания:
    1. Возьмите итоговый класс из прошлого примера и добавьте ему метод, который уменьшает баланс.
       Если итоговое значение будет отрицательным, то нужно будет вызывать исключение ValueError.
    2. Создайте экземпляр класса и уменьшите баланс до положительного значения и распечатайте результат.
    3. Затем уменьшите баланс до отрицательного значения и посмотрите на результат
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float):
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, income: float):
        if income > 0:
            self.balance += income

    def decrease_balance(self, consumption: float):
        if consumption > self.balance:
            raise ValueError
        else:
            if consumption > 0:
                self.balance -= consumption


if __name__ == '__main__':
    account = BankAccount("John Smith", 8000)
    print(account.balance)
    account.decrease_balance(6500)
    print(account.balance)
    account.decrease_balance(3000)

