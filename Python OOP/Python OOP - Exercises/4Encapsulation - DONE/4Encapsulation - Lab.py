# First Problem

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


# Second Problem

class Mammal:
    def __init__(self, name, type, sound):
        self.__kingdom = "animals"
        self.name = name
        self.type = type
        self.sound = sound

    def make_sound(self):
        return f"{self.name} makes {self.sound}"

    def get_kingdom(self):
        return self.__kingdom

    def info(self):
        return f"{self.name} is of type {self.type}"


# Third Problem

class Profile:
    def __init__(self, username: str, password: str):
        self._set_username = username
        self._set_password = password

        if 5 <= len(username) <= 15:
            self.username = username
        else:
            raise ValueError("The username must be between 5 and 15 characters.")

        if len(password) >= 8 and any(c.isupper() for c in password) and any(c.isdigit() for c in password):
            self.password = password
        else:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __str__(self):
        return f"You have a profile with username: \"{self.username}\" and password: {'*' * len(self.password)}"


# Fourth Problem

class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        if self.min_length <= len(name):
            return True
        else:
            return False

    def __is_mail_valid(self, mail):
        if mail in self.mails:
            return True
        else:
            return False

    def __is_domain_valid(self, domain):
        if domain in self.domains:
            return True
        else:
            return False

    def validate(self, email):
        name, rest = email.split("@")
        mail, domain = rest.split(".")
        condition1 = self.__is_name_valid(name)
        condition2 = self.__is_mail_valid(mail)
        condition3 = self.__is_domain_valid(domain)
        if condition1 and condition2 and condition3:
            return True
        else:
            return False


# Fifth Problem

class Account:
    def __init__(self, id, balance, pin):
        self.__id = id
        self.__pin = pin
        self.balance = balance

    def get_id(self, pin):
        if self.__pin == pin:
            return self.__id
        else:
            return f"Wrong pin"

    def change_pin(self, old_pin, new_pin):
        if self.__pin == old_pin:
            self.__pin = new_pin
            return f"Pin changed"
        else:
            return f"Wrong pin"


