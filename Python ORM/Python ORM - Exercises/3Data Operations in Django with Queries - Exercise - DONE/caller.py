import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Pet
from main_app.models import Artifact
from main_app.models import Location
from main_app.models import Car
from main_app.models import Task
from main_app.models import HotelRoom
from main_app.models import Character
# Create queries within functions
# First
def create_pet(name: str, species: str):
    new_pet = Pet(name=name, species=species)
    new_pet.save()
    return f"{name} is a very cute {species}!"

# Second
def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):
    new_artifact = Artifact(name=name, origin=origin, age=age, description=description, is_magical=is_magical)
    new_artifact.save()
    return f"The artifact {name} is {age} years old!"

def delete_all_artifacts():
    all_artifacts = Artifact.objects.all()
    for artifact in all_artifacts:
        artifact.delete()

# Third
def show_all_locations():
    result = []
    locations = Location.objects.order_by('-id')
    for location in locations:
        result.append(f'{location.name} has a population of {location.population}!')
    return "\n".join(result)

def new_capital():
    first_location = Location.objects.first()
    first_location.is_capital = True
    first_location.save()

def get_capitals():
    capitals = Location.objects.filter(is_capital=True).values('name')
    return capitals

def delete_first_location():
    first_location = Location.objects.first()
    first_location.delete()

# Fourth
def apply_discount():
    cars = Car.objects.all()
    for car in cars:
        discount_percentage = sum(int(digit) for digit in str(car.year))
        discount_amount = (car.price * discount_percentage) / 100
        car.price_with_discount = max(0, car.price - discount_amount)
        car.save()

def get_recent_cars():
    recent_cars = Car.objects.filter(year__gte=2020).values('model', 'price_with_discount')
    return recent_cars

def delete_last_car():
    last_car = Car.objects.last()
    last_car.delete()

#Fifth
def show_unfinished_tasks():
    # Return all incomplete tasks with title and due date
    unfinished_tasks = Task.objects.filter(is_finished=False)
    result = ""
    for task in unfinished_tasks:
        result += f"Task - {task.title} needs to be done until {task.due_date}!\n"
    return result

def complete_odd_tasks():
    # Make every task with an odd id finished
    tasks = Task.objects.all()
    for i in range(1, len(tasks) + 1):
        if i % 2 != 0:
            tasks[i - 1].is_finished = True
            tasks[i - 1].save()

def encode_and_replace(text: str, task_title: str):
    # Encode the text and replace it in the description for all tasks with the given title
    tasks = Task.objects.filter(title=task_title)
    for task in tasks:
        encoded_text = ''.join(chr(ord(char) - 3) for char in text)
        task.description = encoded_text
        task.save()

#Sixth
def get_deluxe_rooms():
    deluxe_rooms = HotelRoom.objects.filter(room_type='Deluxe')
    result = []
    for i, room in enumerate(deluxe_rooms):
        if i % 2 == 0:
            result.append(f"Deluxe room with number {room.room_number} costs {room.price_per_night}$ per night!")
    return "\n".join(result)

def increase_room_capacity():
    rooms = HotelRoom.objects.order_by('id')
    for i, room in enumerate(rooms):
        if room.is_reserved:
            if i == 0 or i == 1:
                room.capacity += room.id
            else:
                room.capacity += rooms[i - 1].capacity
            room.save()

def reserve_first_room():
    room = HotelRoom.objects.first()
    room.is_reserved = True
    room.save()

def delete_last_room():
    room = HotelRoom.objects.last()
    if room.is_reserved:
        room.delete()

#Seventh
def update_characters():
    characters = Character.objects.all()
    for character in characters:
        if character.class_name == "Mage":
            character.level += 3
            character.intelligence -= 7
        elif character.class_name == "Warrior":
            character.hit_points /= 2
            character.dexterity += 4
        elif character.class_name == "Assassin" or character.class_name == "Scout":
            character.inventory = "The inventory is empty"
        character.save()

def fuse_characters(first_character, second_character):
    mega_character = Character()
    mega_character.name = f"{first_character.name} {second_character.name}"
    mega_character.class_name = "Fusion"
    mega_character.level = int((first_character.level + second_character.level) // 2)
    mega_character.strength = int((first_character.strength + second_character.strength) * 1.2)
    mega_character.dexterity = int((first_character.dexterity + second_character.dexterity) * 1.4)
    mega_character.intelligence = int((first_character.intelligence + second_character.intelligence) * 1.5)
    mega_character.hit_points = (first_character.hit_points + second_character.hit_points)
    if first_character.class_name == "Mage" or first_character.class_name == "Scout":
        mega_character.inventory = f"Bow of the Elven Lords, Amulet of Eternal Wisdom"
    elif first_character.class_name == "Warrior" or first_character.class_name == "Assassin":
        mega_character.inventory = f"Dragon Scale Armor, Excalibur"
    first_character.delete()
    second_character.delete()
    mega_character.save()

def grand_dexterity():
    characters = Character.objects.all()
    for character in characters:
        character.dexterity = 30
        character.save()

def grand_intelligence():
    characters = Character.objects.all()
    for character in characters:
        character.intelligence = 40
        character.save()

def grand_strength():
    characters = Character.objects.all()
    for character in characters:
        character.strength = 50
        character.save()

def delete_characters():
    characters = Character.objects.all()
    for character in characters:
        if character.inventory == "The inventory is empty":
            character.delete()
