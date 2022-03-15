import os
import sys
from os import system


class Authorization:
    def __init__(self, user_file="users.txt"):
        system("clear")
        self.login = None
        self.password = None
        self.file_name = user_file
        self.all_users = []
        self.initial_page()

    # Initial page -> Shahzod
    def initial_page(self):
        ent_sys = input(self.welcome_msg()).strip()

        while not self.file_empty() and ent_sys not in ['1', '2', '3'] or self.file_empty() and ent_sys not in ['1',
                                                                                                                '2']:
            system("clear")
            print("Invalid input!")
            ent_sys = input(self.welcome_msg()).strip()

        if ent_sys == '1':
            self.register()
        elif not self.file_empty() and ent_sys == '2':
            system("clear")
            self.log_in()
        else:
            self.bye()

    # Menu page -> Shahzod
    def menu_page(self):
        ent_otp = input(self.menu_page_msg()).strip()

        while ent_otp not in ['1', '2', '3']:
            system("clear")
            print("Invalid input!")
            ent_otp = input(self.menu_page_msg()).strip()

        if ent_otp == '1':
            self.settings_page()
        elif ent_otp == '2':
            self.log_out()
        else:
            self.bye()

    # Settings page -> Shahzod
    def settings_page(self):
        system("clear")
        enter_opt = input(self.settings_msg()).strip()

        while enter_opt not in ['1', '2', '3', '4', '5']:
            system("clear")
            print("Invalid input!")
            enter_opt = input(self.settings_msg()).strip()

        if enter_opt == '1':
            self.account_info()
        elif enter_opt == '2':
            self.update_login()
        elif enter_opt == '3':
            self.update_password()
        elif enter_opt == '4':
            self.delete_account()
        else:
            system("clear")
            self.menu_page()

    # Registration -> Shahzod
    def register(self):
        self.get_all_users()
        system("clear")
        name = input("Enter your name: ").lower().strip()
        surname = input("Enter your surname: ").lower().strip()
        age = input("Enter your age: ").strip()
        phone = input("Enter your phone number: ").strip()
        login = input("Enter your login: ").strip()

        while not self.login_is_correct(login):
            system("clear")
            self.wrong_log_msg()
            login = input("Your login: ").strip()

        while self.login_is_exist(login):
            system("clear")
            print("This login is exists!")
            login = input("Please write another one: ").strip()

        password = input("Enter your password: ").strip()
        while not self.pasw_is_correct(password):
            system("clear")
            self.wrong_pass_msg()
            password = input("Your password: ").strip()

        with open(self.file_name, 'a') as file:
            file.write(
                f"login={login}|password={password}|name={name}|surname={surname}|age={age}|phone_number={phone}\n")

        system("clear")
        print("You are successfully registered!")
        self.login, self.password = login, password
        self.menu_page()

    # Log in -> Jafar
    def log_in(self):
        a = 1
        while a:
          system("clear")
          login =   input("your login: ").strip()
          password =  input("your password: ").strip()
          self.all_users.clear()
          self.get_all_users()
          for user in self.all_users:
                if user["login"] == login and user["password"] == password:
                    a = 0

        self.menu_page()

    # Log out -> Shahzod
    def log_out(self):
        system("clear")
        self.login = self.password = None
        self.all_users.clear()
        self.initial_page()

    # Update login -> Shahzod
    def update_login(self):
        system("clear")
        new_login = input("Enter your new login: ")

        while not self.login_is_correct(new_login) or new_login == self.login:
            system("clear")
            self.wrong_log_msg()
            new_login = input("New login: ")

        with open(self.file_name) as file:
            users = file.read().replace(f"login={self.login}|password={self.password}",
                                        f"login={new_login}|password={self.password}")

        with open(self.file_name, 'w') as file:
            file.write(users)

        self.login = new_login
        print("Your login is successfully updated!")
        self.settings_page()

    # Update password -> Shahzod
    def update_password(self):
        system("clear")
        new_pass = input("New password: ")

        while not self.pasw_is_correct(new_pass) or new_pass == self.password:
            system("clear")
            self.wrong_pass_msg()
            new_pass = input("New password: ")

        with open(self.file_name) as file:
            users = file.read().replace(f"login={self.login}|password={self.password}",
                                        f"login={self.login}|password={new_pass}")

        with open(self.file_name, 'w') as file:
            file.write(users)

        self.password = new_pass
        print("Your password is successfully updated!")
        self.settings_page()

    # Account info -> Jafar
    def account_info(self):
        self.all_users.clear()
        self.get_all_users()
        for user in self.all_users:
            if user["login"] == self.login and user["password"] == self.password:
                system("clear")
                print(f"Name: {user['name'].title()}\nSurname: {user['surname'].title()}\nAge: {user['age']}\n"
                      f"Phone: +998{user['phone_number']} ")

        input("\nTo back press anything: ")
        self.settings_page()

    # Delete account -> Shahzod
    def delete_account(self):
        with open(self.file_name) as file:
            users = file.readlines()

        for user in users:
            if f"login={self.login}|" in user and f"password={self.password}|" in user:
                users.remove(user)

        with open(self.file_name, 'w') as file:
            for user in users:
                file.write(user)

        system("clear")
        self.initial_page()

    def welcome_msg(self):
        if self.file_empty():
            return '''
            Please select one of the options below:

            [1] Register
            [2] Exit

            Enter number: '''
        else:
            return '''
            Please select one of the options below:

            [1] Register
            [2] Log in
            [3] Exit

            Enter number: '''

    @staticmethod
    def menu_page_msg():
        return '''
            Please select one of the options below:

            [1] Settings
            [2] Log out
            [3] Exit

            Enter number: '''

    @staticmethod
    def settings_msg():
        return '''
            Please select one of the options below:

            [1] Account info
            [2] Update login
            [3] Update password
            [4] Delete account
            [5] Back

            Enter number: '''

    @staticmethod
    def wrong_log_msg():
        print("Login is invalid!")
        print("Login should contain at least 3 characters, [a-z] and/or [0-9]")

    @staticmethod
    def wrong_pass_msg():
        print("Password is invalid!")
        print("Password should contain at least 6 characters")

    @staticmethod
    def bye():
        system("clear")
        print("Bye")
        sys.exit()

    def file_empty(self):
        with open(self.file_name) as file:
            txt = file.read()
        return txt == ""

    def get_all_users(self):
        with open(self.file_name) as file:
            for row in file.read().split():
                self.all_users.append(
                    {
                        "login": row.split("|")[0].split("=")[1],
                        "password": row.split("|")[1].split("=")[1],
                        "name": row.split("|")[2].split("=")[1],
                        "surname": row.split("|")[3].split("=")[1],
                        "age": row.split("|")[4].split("=")[1],
                        "phone_number": row.split("|")[5].split("=")[1]
                    }
                )

    @staticmethod
    def login_is_correct(login_):
        return len(login_) > 3 and login_.isalnum() or '_' in login_

    @staticmethod
    def pasw_is_correct(password_):
        return len(password_) > 5 and ' ' not in password_

    def login_is_exist(self, login_):
        for user in self.all_users:
            if user["login"] == login_:
                return True
        return False


account = Authorization()
