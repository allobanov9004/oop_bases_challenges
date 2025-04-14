"""
У нас есть различные типы классы для различных типов продуктов. Но мы ничего не знаем о том что происходит, когда мы вызываем
эти методы, хотелось бы простейшего логирования

Задания:
    1. Создайте класс PrintLoggerMixin и метод log у него, который будет принтить переданное в него сообщение.
    2. Используйте этот миксин, чтобы залогировать все методы у PremiumProduct и DiscountedProduct.
       Добавьте миксин и используйте новый метод во всех методах основных классов.
    3. Вызовите у экземпляров PremiumProduct и DiscountedProduct все возможные методы и убедитесь, что вызовы логируются.
"""


class Product:
    def __init__(self, title: str, price: float):
        self.title = title
        self.price = price

    def get_info(self):
        return f'Product {self.title} with price {self.price}'

class PrintLoggerMixin:
    def log(self, message: str)-> None:
        print(message)

class PremiumProduct(PrintLoggerMixin, Product):
    def increase_price(self):
        self.price *= 1.2
        self.log(f"increased price: {self.price}")

    def get_info(self):
        base_info = super().get_info()
        self.log(f"info: {base_info}")
        return f'{base_info} (Premium)'


class DiscountedProduct(PrintLoggerMixin, Product):
    def decrease_price(self):
        self.price /= 1.2
        self.log(f"decreased price: {self.price}")

    def get_info(self):
        base_info = super().get_info()
        self.log(f"info: {base_info}")
        return f'{base_info} (Discounted)'


if __name__ == '__main__':
    premium_p = PremiumProduct(title="iphone", price=1000)
    premium_p.increase_price()
    premium_p.get_info()

    discounted_p = DiscountedProduct(title="Nexus5", price=300)
    discounted_p.decrease_price()
    discounted_p.get_info()

