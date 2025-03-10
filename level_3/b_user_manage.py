"""
У нас есть класс UserManager, который содержит в себе список юзернэймов пользователей и может расширять этот список.

Задания:
    1. Создайте класс AdminManager, который будет наследником UserManager.
       У него должен быть свой уникальный метод ban_username, который по переданному в него юзернэйму будет удалять
       юзернэйм из списка. Если такого юзернэйма в списке нет - должно печататься сообщение: "Такого пользователя не существует."
    2. Создайте класс SuperAdminManager, который будет наследником AdminManager.
       У него должен быть свой уникальный метод ban_all_users, который будет удалять все юзернэймы из списка.
    3. Создайте экземпляры каждого из трех классов и у каждого экземпляра вызовите все возможные методы.
"""


class UserManager:
    def __init__(self):
        self.usernames = []

    def add_user(self, username):
        self.usernames.append(username)

    def get_users(self):
        return self.usernames


class AdminManager(UserManager):
    def ban_username(self, username: str):
        if username in self.usernames:
            self.usernames.remove(username)
        else:
            print('Такого пользователя не существует.')
    
class SuperAdminManager(AdminManager):
    def ban_all_users(self):
        return self.usernames.clear()


if __name__ == '__main__':
    user = UserManager()
    user.add_user("1")
    user.add_user("2")

    print(user.get_users())

    admin = AdminManager()
    admin.add_user("3")
    admin.add_user("4")
    admin.ban_username("2")
    admin.ban_username("3")
    print(admin.get_users())

    superadmin = SuperAdminManager()
    superadmin.add_user("5")
    superadmin.add_user("6")
    superadmin.add_user("7")
    print(superadmin.get_users())
    superadmin.ban_username("6")
    print(superadmin.get_users())
    superadmin.ban_all_users()
    print(superadmin.get_users())
