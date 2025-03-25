"""
У нас есть класс Product, который подходит для многих продуктов, но не для еды.
В пищевом продукте нам нужно хранить еще срок годности, который будет влиять и на другие методы

Задания:
    1. Переопределите частично метод __init__ у FoodProduct так, чтобы там хранилось еще свойство expiration_date.
       Используйте super() для этого.
    2. Переопределите у FoodProduct полностью метод get_full_info, чтобы он возвращал еще и информацию о сроке годности
    3. Переопределите частично метод is_available у FoodProduct, чтобы там учитывался еще и срок годности. Если он
       меньше чем текущая дата - то is_available должен возвращать False. Используйте super() для этого.
    3. Создайте экземпляры каждого из двух классов и вызовите у них все доступные методы
"""
from datetime import datetime, date


class Product:
    def __init__(self, title, quantity):
        self.title = title
        self.quantity = quantity

    def get_full_info(self):
        return f'Product {self.title}, {self.quantity} in stock.'

    def is_available(self):
        return self.quantity > 0


class FoodProduct(Product):
    def __init__(self, title: str, quantity: int, expiration_date: datetime.date)-> None: 
        super().__init__(title, quantity)
        self.expiration_date = expiration_date

    def get_full_info(self)-> str:
        full_food_info = super().get_full_info()
        full_food_info += f'expiration date: {self.expiration_date}'
        return full_food_info
    
    def is_available(self)-> bool:
        time = datetime.now().date()
        return super().is_available() and self.expiration_date > time


if __name__ == '__main__':
    phone = Product('iphone', 20)
    printer = Product('canon', 0)
    print(phone.get_full_info())
    print(phone.is_available())
    print(printer.get_full_info())
    print(printer.is_available())

    cheese = FoodProduct('maasdam', 10, date(2025, 12, 31))
    bread = FoodProduct('pan', 5, date(2001, 1, 1))
    print(cheese.get_full_info())
    print(cheese.is_available())
    print(bread.get_full_info())
    print(bread.is_available())