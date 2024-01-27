# First Problem

class Shop:
    def __init__(self, name, items):
        self.name = name
        self.items = items

    def get_items_count(self):
        return len(self.items)



# Second Problem

class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health


    def defend(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            return f"{self.name} was defeated"

    def heal(self, amount):
        self.health += amount



# Third Problem

class Employee:
    def __init__(self, id, first_name, last_name, salary):
        self.id = int(id)
        self.first_name = first_name
        self.last_name = last_name
        self.salary = int(salary)


    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


    def get_annual_salary(self):
        return self.salary * 12


    def raise_salary(self, amount):
        self.salary += amount
        return self.salary



# Fourth Problem

class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity


    def fill(self, quantity):
        if self.quantity + quantity <= self.size:
            self.quantity += quantity


    def status(self):
        return self.size - self.quantity



# Fifth Problem

class Flower:
    def __init__(self, name, water_requirements):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = False

    def water(self, quantity):
        if quantity >= self.water_requirements:
            self.is_happy = True
        else:
            self.is_happy = False


    def status(self):
        if self.is_happy:
            return f"{self.name} is happy"
        else:
            return f"{self.name} is not happy"



# Sixth Problem

class SteamUser:
    def __init__(self, username, games):
        self.username = username
        self.games = games
        self.played_hours = 0

    def play(self, game, hours):
        if game in self.games:
            self.played_hours += hours
            return f"{self.username} is playing {game}"
        else:
            return f"{game} is not in library"

    def buy_game(self, game):
        if game not in self.games:
            self.games.append(game)
            return f"{self.username} bought {game}"
        else:
            return f"{game} is already in your library"

    def status(self):
        return f"{self.username} has {len(self.games)} games. Total play time: {self.played_hours}"



# Seventh Problem

class Programmer:
    def __init__(self, name, language, skills):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name, language, skills_earned):
        if language == self.language:
            self.skills += skills_earned
            return f"{self.name} watched {course_name}"
        else:
            return f"{self.name} does not know {language}"

    def change_language(self, new_language, skills_needed):
        if self.skills >= skills_needed and new_language != self.language:
            previous = self.language
            self.language = new_language
            return f"{self.name} switched from {previous} to {new_language}"

        elif self.skills >= skills_needed:
            return f"{self.name} already knows {new_language}"

        else:
            return f"{self.name} needs {skills_needed - self.skills} more skills"
