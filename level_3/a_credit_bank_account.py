"""
У нас есть класс кредитного банковского аккаунта со свойствами: полное имя владельца и баланс.

Задания:
    1. Нужно вынести методы, которые не относится непосредственно к кредитам в отдельны класс BankAccount.
    2. CreditAccount нужно отнаследовать от BankAccount.
    3. Создать экземпляр класс BankAccount и вызвать у него каждый из возможных методов.
    4. Создать экземпляр класс CreditAccount и вызвать у него каждый из возможных методов.
"""

# код писать тут
class BankAccount:
    def __init__(self, owner_full_name: str, balance: float):
        self.owner_full_name = owner_full_name
        self.balance = balance
    def increase_balance(self, amount: float):
        if amount > 0:
            self.balance += amount
        else: 
            print("пополнение должно быть положительным")

    def decrease_balance(self, amount: float):
        self.balance -= amount

class CreditAccount(BankAccount):
    def is_eligible_for_credit(self):
        return self.balance > 1000


if __name__ == '__main__':
    bank_acc = BankAccount("John Smith", 50000)
    print(bank_acc.balance)
    bank_acc.increase_balance(50000)
    print(bank_acc.balance)
    bank_acc.decrease_balance(1000)
    print(bank_acc.balance)

    credit_acc = CreditAccount("Richard Roe", 15000)
    print(credit_acc.is_eligible_for_credit())
    credit_acc.decrease_balance(14500)
    print(credit_acc.is_eligible_for_credit())

