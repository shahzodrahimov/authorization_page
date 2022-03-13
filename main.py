import sys
from os import system


class Authorization:
    def __init__(self, user_file="users.txt"):      # Name
        self.login = None
        self.password = None
        self.file_name = user_file
        self.initial_page()

    # Asosiy sahifa -> Shahzod
    def initial_page(self):
        ent_sys = input(self.welcome_msg())

        while not self.file_empty() and ent_sys not in ['1', '2', '3'] or self.file_empty() and ent_sys not in ['1', '2']:
            system("clear")
            print("Invalid input!")
            ent_sys = input(self.welcome_msg()).strip()

        if ent_sys == '1':
            self.register()
        elif not self.file_empty() and ent_sys == '2':
            self.log_in()
        else:
            sys.exit()

    # Registratsiya qismi -> Name
    def register(self):
        print("Register page")

    # Log in qismi -> Name
    def log_in(self):
        print("Log in page")

    # Log out qismi -> Shahzod
    def log_out(self):
        pass

    # Loginni yangilash qismi -> Name
    def update_login(self):
        pass

    # Parolni yangilash qismi -> Name
    def update_password(self):
        pass

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

    def file_empty(self):
        with open(self.file_name) as file:
            txt = file.read()
        return txt == ""


account = Authorization()
