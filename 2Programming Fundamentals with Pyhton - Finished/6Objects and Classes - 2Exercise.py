# First Problem

class Storage:

    def __init__(self, capacity):
        self.capacity = int(capacity)
        self.storage = []

    def add_product(self, product: str):
        if self.capacity > 0:
            self.storage.append(product)
            self.capacity -= 1

    def get_products(self):
        return self.storage



# Second Problem

class Weapon:

    def __init__(self, bullets):
        self.bullets = bullets

    def shoot(self):
        if self.bullets > 0:
            self.bullets -= 1
            return f"shooting..."
        elif self.bullets <= 0:
            return f"no bullets left"

    def __repr__(self):
        return f"Remaining bullets: {self.bullets}"



# Third Problem

class Catalogue:

    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        filtered_products = [product for product in self.products if product.startswith(first_letter)]
        return filtered_products

    def __repr__(self):
        sorted_products = sorted(self.products)
        result = f"Items in the {self.name} catalogue:\n"
        for product in sorted_products:
            result += f"{product}\n"

        return result.strip()



# Fourth Problem

class Town:

    def __init__(self, name):
        self.name = name
        self.latitude = "0°N"
        self.longitude = "0°E"

    def set_latitude(self, latitude):
        self.latitude = latitude

    def set_longitude(self, longitude):
        self.longitude = longitude

    def __repr__(self):
        return f"Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}"



# Fifth Problem

class Class:

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    __students_count = 22

    def add_student(self, name: str, grade: float):
        if self.__students_count > 0:
            self.students.append(name)
            self.grades.append(grade)
            self.__students_count -= 1

    def get_average_grade(self):
        total = 0
        for grade in self.grades:
            total += grade
        average_grade = total / len(self.grades)
        return round(average_grade, 2)

    def __repr__(self):
        total = 0
        for grade in self.grades:
            total += grade
        average_grade = total / len(self.grades)
        return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {average_grade:.2f}"



# Sixth Problem

class Inventory:

    def __init__(self, __capacity: int):
        self.capacity = __capacity
        self.items = []
        self.left = __capacity
    def add_item(self, item: str):

        if self.left > 0:
            self.items.append(item)
            self.left -= 1
        elif self.left <= 0:
            return f"not enough room in the inventory"

    def get_capacity(self):
        return self.capacity

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.left}"



# Seventh Problem

class Article:

    def __init__(self, title: str, content: str, author: str):
        self.title = title
        self.content = content
        self.author = author

    def edit(self, new_content: str):
        self.content = new_content

    def change_author(self, new_author: str):
        self.author = new_author

    def rename(self, new_title: str):
        self.title = new_title

    def __repr__(self):
        return f"{self.title} - {self.content}: {self.author}"



# Eighth Problem

class Vehicle:

    def __init__(self, type, model, price):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money: int, owner: str):
        if money >= self.price and self.owner == None:
            change = money - self.price
            self.owner = owner
            return f"Successfully bought a {self.type}. Change: {change:.2f}"
        elif money < self.price:
            return f"Sorry, not enough money"
        elif self.owner != None:
            return f"Car already sold"

    def sell(self):
        if self.owner != None:
            self.owner = None
        elif self.owner == None:
            return f"Vehicle has no owner"

    def __repr__(self):
        if self.owner != None:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        elif self.owner == None:
            return f"{self.model} {self.type} is on sale: {self.price}"



# Ninth Problem

class Movie:

    __watched_movies = 0

    def __init__(self, name, director):
        self.name = name
        self.director = director
        self.watched = False

    def change_name(self, new_name: str):
        self.name = new_name

    def change_director(self, new_director: str):
        self.director = new_director

    def watch(self):
        if not self.watched:
            self.watched = True
            Movie.__watched_movies += 1

    def __repr__(self):
        return f"Movie name: {self.name}; Movie director: {self.director}. Total watched movies: {self.__watched_movies}"