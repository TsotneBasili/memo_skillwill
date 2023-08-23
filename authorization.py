import json

class Authorization:
    def __init__(self):
        self.choices = {
            "1": self.log_in,
            "2": self.register
        }

    user_list = []
    current_user = ""

    def menu(self):
        print("""
        choose option
        1. log in
        2. register
        """)

    def register(self):
        username = input("Choose username: ")
        password = input("Choose password: ")
        with open("users.json", "r") as file:
            data = json.load(file)
        usernames = [user_dict["username"] for user_dict in data]
        if username in usernames:
            print("username is taken")
            self.register()
        else:
            print("Registration successful")
            self.user_list.append(username)
            self.current_user = username
            data.append({"username": username, "password": password})

            with open("users.json", "w") as file:
                json.dump(data, file, indent=4)

    def log_in(self):
        username = input("Choose username: ")
        password = input("Choose password: ")
        with open("users.json", "r") as file:
            data = json.load(file)
        usernames = [user_dict["username"] for user_dict in data]
        passwords = [password_dict["password"] for password_dict in data]
        if username not in usernames:
            print("wrong username")
            self.log_in()
        elif password not in passwords:
            print("wrong password")
            self.log_in()
        else:
            self.current_user = username
            print("log in successful")

    def run(self):
        self.menu()
        choice = input("Enter option: ")
        if choice in self.choices:
            action = self.choices[choice]
            action()
        else:
            print("your option doesn't exist")
            self.run()
