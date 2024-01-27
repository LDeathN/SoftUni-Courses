# First Problem

number = int(input())
for i in range(number, 1, -1):
    print(" " * (i - 1), end="")
    for j in range(number - i):
        print("* ", end="")
    print("*")
for i in range(number - 1):
    print("* ", end="")
print("*")
for i in range(1, number):
    print(" " * i, end="")
    for j in range(number - (i + 1)):
        print("* ", end="")
    print("*")



# Second Problem

string = """
global
outer: local
inner: nonlocal
outer: nonlocal
global: changed!
"""
print(string)



# Third Problem

class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages



# Fourth Problem

class Car:
    def __init__(self, name, model, engine):
        self.name = name
        self.model = model
        self.engine = engine
    def get_info(self):
        return f"This is {self.name} {self.model} with engine {self.engine}"



# Fifth Problem

class Music:
    def __init__(self, title, artist, lyrics):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics


    def print_info(self):
        return f'This is "{self.title}" from "{self.artist}"'


    def play(self):
        return f"{self.lyrics}"
