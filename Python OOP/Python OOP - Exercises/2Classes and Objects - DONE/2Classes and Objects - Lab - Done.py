# First Problem

class Vehicle:

    def __init__(self, mileage, max_speed=150):
        self.max_speed = max_speed
        self.mileage = mileage
        self.gadgets = []



# Second Problem

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

    def __str__(self):
        return f"The point has coordinates ({self.x},{self.y})"



# Third Problem

class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_area(self):
        return (self.radius ** 2) * self.pi

    def get_circumference(self):
        return self.radius * 2 * self.pi



# Fourth Problem

class Glass:

    capacity = 250

    def __init__(self):
        self.content = 0

    def fill(self, ml):
        if self.content + ml <= self.capacity:
            self.content += ml
            return f"Glass filled with {ml} ml"
        else:
            return f"Cannot add {ml} ml"

    def empty(self):
        self.content = 0
        return f"Glass is now empty"

    def info(self):
        return f"{self.capacity - self.content} ml left"



# Fifth Problem

class Smartphone:
    def __init__(self, memory):
        self.memory = memory
        self.apps = []
        self.is_on = False

    def power(self):
        if not self.is_on:
            self.is_on = True
        elif self.is_on:
            self.is_on = False

    def install(self, app, app_memory):
        if self.is_on and app_memory <= self.memory:
            self.memory -= app_memory
            self.apps.append(app)
            return f"Installing {app}"
        elif app_memory <= self.memory:
            return f"Turn on your phone to install {app}"
        else:
            return f"Not enough memory to install {app}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"