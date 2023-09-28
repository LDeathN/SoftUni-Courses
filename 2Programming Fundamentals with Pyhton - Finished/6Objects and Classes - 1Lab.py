# First Problem

class Comment:
    def __init__(self, username, content, likes = 0):
        self.username = username
        self.content = content
        self.likes = likes



# Second Problem

class Party:
    def __init__(self):
        self.people = []

party = Party()
line = input()
while line != "End":
    party.people.append(line)
    line = input()
print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")



# Third Problem

class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

emails = []
while True:
    line = input()
    if line == "Stop":
        break
    tokens = line.split(" ")
    sender = tokens[0]
    receiver = tokens[1]
    content = tokens[2]
    email = Email(sender, receiver, content)
    emails.append(email)

send_emails = list(map(lambda x: int(x), input().split(", ")))

for x in send_emails:
    emails[x].send()

for email in emails:
    print(email.get_info())



# Fourth Problem

class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append((name))
        elif species == "bird":
            self.birds.append((name))

        Zoo.__animals += 1
    def get_info(self, species):
        result = ""
        if species == "mammal":
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif species == "fish":
            result += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        elif species == "bird":
            result += f"Birds in {self.name}: {', '.join(self.birds)}\n"

        result += f"Total animals: {Zoo.__animals}"
        return result

zoo_name = str(input())
zoo = Zoo(zoo_name)
number = int(input())

for i in range(1, number + 1):
    animal_input = str(input())
    tokens = animal_input.split(" ")
    species = tokens[0]
    name = tokens[1]
    zoo.add_animal(species, name)
info = input()
print(zoo.get_info(info))



# Fifth Problem

class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter

    def calculate_circumference(self):
        circumference = self.__pi * self.diameter
        return circumference

    def calculate_area(self):
        area = self.__pi * (self.diameter / 2) ** 2
        return area

    def calculate_area_of_sector(self, angle):
        area_of_sector = (self.__pi * (self.diameter / 2) ** 2) * angle / 360
        return area_of_sector
