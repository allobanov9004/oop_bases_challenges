"""
Задания:
    1. Создайте экземпляр класса юзера, наполнив любыми данными.
    2. Распечатайте информацию о нем в таком виде: Информация о пользователе: имя, юзернэйм, возраст, телефон.
"""


class User:
    def __init__(self, name: str, username: str, age: int, phone: str):
        self.name = name
        self.username = username
        self.age = age
        self.phone = phone


if __name__ == '__main__':
    user_1 = User("Name", "Username", 20, "111-22-33")
    print(f"Информация о пользователе: {user_1.name}, {user_1.username}, {user_1.age}, {user_1.phone}")
