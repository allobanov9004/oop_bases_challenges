"""
У любого продукта есть такие свойства: название, описание, цена, вес

Задания:
    1. Создайте класс продукта.
    2. Создайте экземпляр этого продукта и наполинте своими данными.
    3. Распечатайте о нем иформацию в таком виде: Информация о продукте: название, описание, цена, вес
"""


class Product:
    def __init__(self, name: str, overview: str, price: float, weight: float):
        self.name = name
        self.overview = overview
        self.price = price
        self.weight = weight

    def get_product_info(self):
        return f"Информация о продукте: {self.name}, {self.overview}, {self.price}, {self.weight}"
        


if __name__ == '__main__':
    box = Product("box", "container", 5, 1)
    box_data = box.get_product_info()
    print(box_data)
