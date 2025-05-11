"""

Задания:
    1. Создайте класс Developer, который будет наследоваться от класса ItDepartmentEmployee и класса SuperAdminMixin.
    2. Переопределите у класса Developer метод __init__ таким образом, чтобы он на вход принимал еще и язык программирования.
    3. Переопределите метод get_info у класса Developer таким образом, чтобы там выводился еще и язык программирования.
    4. Вызовите у экземпляра класса Developer все возможные методы.
"""


class Employee:
    def __init__(self, name: str, surname: str, age: int, salary: float):
        self.name = name
        self.surname = surname
        self.age = age
        self.salary = salary

    def get_info(self):
        return f'{self.name} with salary {self.salary}'


class ItDepartmentEmployee(Employee):
    def __init__(self, name: str, surname: str, age: int, salary: float):
        super().__init__(name, surname, age, salary)
        self.salary *= 2


class AdminMixin:
    def increase_salary(self, employee: Employee, amount: float):
        employee.salary += amount


class SuperAdminMixin(AdminMixin):
    def decrease_salary(self, employee: Employee, amount: float):
        employee.salary -= amount


class Developer(SuperAdminMixin, ItDepartmentEmployee):
    def __init__(self, name: str, surname: str, age: int, salary: float, lang: str):
        super().__init__(name, surname, age, salary)
        self.lang = lang
    def get_info(self):
        return super().get_info() + f". Programming language: {self.lang}"


if __name__ == '__main__':
    john = Developer(name="John", surname="Doe", age=30, salary=1000, lang="C++")
    print(john.get_info())
    john.increase_salary(employee=john, amount=200)
    print(john.get_info())
    john.decrease_salary(employee=john, amount=100)
    print(john.get_info())
    

