"""
Нам неоюходимо проверить, находится ли фамилия пользователя в списке запрещенных.

Задания:
    1. Cоздайте класс юзера, у которого параметры: имя, фамилия, возраст.
    2. Добавьте ему метод should_be_banned, который проверяет, должен ли быть пользователь забанен.
       Пользователя стоит забанить, если его фамилия находится в SURNAMES_TO_BAN.
"""

import dataclasses

SURNAMES_TO_BAN = ['Vaughn', 'Wilhelm', 'Santaros', 'Porter', 'Smith']

@dataclasses.dataclass()
class User:
    name: str
    surname: str
    age: int

    def should_be_banned(self):
        return self.surname in SURNAMES_TO_BAN
    
if __name__ == '__main__':
    john = User("John", "Smith", 30)
    john_2 = User("John", "Doe", 25)

    print(john.should_be_banned())
    print(john_2.should_be_banned())