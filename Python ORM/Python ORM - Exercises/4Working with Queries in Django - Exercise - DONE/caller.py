import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import ArtworkGallery
from main_app.models import Laptop
from main_app.models import ChessPlayer
from main_app.models import Meal
from main_app.models import Dungeon
from main_app.models import Workout

#First
def show_highest_rated_art():
    arts = ArtworkGallery.objects.all()
    sorted_arts = sorted(arts, key=lambda art: (-art.rating, art.id))
    art = sorted_arts[0]
    return f"{art.art_name} is the highest-rated art with a {art.rating} rating!"

def bulk_create_arts(first_art, second_art):
    first_art.save()
    second_art.save()

def delete_negative_rated_arts():
    arts = ArtworkGallery.objects.all()
    for art in arts:
        if art.rating < 0:
            art.delete()

#Second
def show_the_most_expensive_laptop():
    laptops = Laptop.objects.all()
    sorted_laptops = sorted(laptops, key=lambda x: (-x.price, -x.id))
    laptop = sorted_laptops[0]
    return f"{laptop.brand} is the most expensive laptop available for {laptop.price}$!"

def bulk_create_laptops(*args):
    for arg in args:
        for laptop in arg:
            new_laptop = Laptop(brand=laptop.brand, processor=laptop.processor, memory=laptop.memory, storage=laptop.storage, operation_system=laptop.operation_system, price=laptop.price)
            new_laptop.save()

def update_to_512_GB_storage():
    laptops = Laptop.objects.all()
    for laptop in laptops:
        if laptop.brand == "Asus" or laptop.brand == "Lenovo":
            laptop.storage = 512
        laptop.save()

def update_to_16_GB_memory():
    laptops = Laptop.objects.all()
    for laptop in laptops:
        if laptop.brand == "Apple" or laptop.brand == "Dell":
            laptop.memory = 16
        laptop.save()

def update_operation_systems():
    laptops = Laptop.objects.all()
    for laptop in laptops:
        if laptop.brand == "Asus":
            laptop.operation_system = "Windows"
        elif laptop.brand == "Apple":
            laptop.operation_system = "MacOS"
        elif laptop.brand == "Dell" or laptop.brand == "Acer":
            laptop.operation_system = "Linux"
        elif laptop.brand == "Lenovo":
            laptop.operation_system = "Chrome OS"
        laptop.save()

def delete_inexpensive_laptops():
    laptops = Laptop.objects.all()
    for laptop in laptops:
        if laptop.price < 1200:
            laptop.delete()

#Third
def bulk_create_chess_players(*args):
    for arg in args:
        for player in arg:
            new_player = ChessPlayer(username=player.username, title=player.title, rating=player.rating, games_played=player.games_played, games_won=player.games_won, games_lost=player.games_lost, games_drawn=player.games_drawn)
            new_player.save()

def delete_chess_players():
    players = ChessPlayer.objects.all()
    for player in players:
        if player.title == "no title":
            player.delete()

def change_chess_games_won():
    players = ChessPlayer.objects.all()
    for player in players:
        if player.title == "GM":
            player.games_won = 30
        player.save()

def change_chess_games_lost():
    players = ChessPlayer.objects.all()
    for player in players:
        if player.title == "no title":
            player.games_lost = 25
        player.save()

def change_chess_games_drawn():
    players = ChessPlayer.objects.all()
    for player in players:
        player.games_drawn = 10
        player.save()

def grand_chess_title_GM():
    players = ChessPlayer.objects.all()
    for player in players:
        if player.rating >= 2400:
            player.title = "GM"
        player.save()

def grand_chess_title_IM():
    players = ChessPlayer.objects.all()
    for player in players:
        if 2300 <= player.rating <= 2399:
            player.title = "IM"
        player.save()

def grand_chess_title_FM():
    players = ChessPlayer.objects.all()
    for player in players:
        if 2200 <= player.rating <= 2299:
            player.title = "FM"
        player.save()

def grand_chess_title_regular_player():
    players = ChessPlayer.objects.all()
    for player in players:
        if 0 <= player.rating <= 2199:
            player.title = "regular player"
        player.save()

#Fourth
def set_new_chefs():
    meals = Meal.objects.all()
    for meal in meals:
        if meal.meal_type == "Breakfast":
            meal.chef = "Gordon Ramsay"
        elif meal.meal_type == "Lunch":
            meal.chef = "Julia Child"
        elif meal.meal_type == "Dinner":
            meal.chef = "Jamie Oliver"
        elif meal.meal_type == "Snack":
            meal.chef = "Thomas Keller"
        meal.save()

def set_new_preparation_times():
    meals = Meal.objects.all()
    for meal in meals:
        if meal.meal_type == "Breakfast":
            meal.preparation_time = "10 minutes"
        elif meal.meal_type == "Lunch":
            meal.preparation_time = "12 minutes"
        elif meal.meal_type == "Dinner":
            meal.preparation_time = "15 minutes"
        elif meal.meal_type == "Snack":
            meal.preparation_time = "5 minutes"
        meal.save()

def update_low_calorie_meals():
    meals = Meal.objects.all()
    for meal in meals:
        if meal.meal_type == "Breakfast" or meal.meal_type == "Dinner":
            meal.calories = 400
        meal.save()

def update_high_calorie_meals():
    meals = Meal.objects.all()
    for meal in meals:
        if meal.meal_type == "Lunch" or meal.meal_type == "Snack":
            meal.calories = 700
        meal.save()

def delete_lunch_and_snack_meals():
    meals = Meal.objects.all()
    for meal in meals:
        if meal.meal_type == "Lunch" or meal.meal_type == "Snack":
            meal.delete()

#Fifth
def show_hard_dungeons():
    dungeons = Dungeon.objects.all()
    result = []
    hard_dungeons = [dungeon for dungeon in dungeons if dungeon.difficulty == "Hard"]
    sorted_dungeons = sorted(hard_dungeons, key=lambda dungeon: dungeon.location)
    for dungeon in sorted_dungeons:
        result.append(f"{dungeon.name} is guarded by {dungeon.boss_name} who has {dungeon.boss_health} health points!")
    return "\n".join(result)

def bulk_create_dungeons(*args):
    for arg in args:
        for dungeon in arg:
            new_dungeon = Dungeon(name=dungeon.name, difficulty=dungeon.difficulty, location=dungeon.location, boss_name=dungeon.boss_name, recommended_level=dungeon.recommended_level, boss_health=dungeon.boss_health, reward=dungeon.reward)
            new_dungeon.save()

def update_dungeon_names():
    dungeons = Dungeon.objects.all()
    for dungeon in dungeons:
        if dungeon.difficulty == "Easy":
            dungeon.name = "The Erased Thombs"
        elif dungeon.difficulty == "Medium":
            dungeon.name = "The Coral Labyrinth"
        elif dungeon.difficulty == "Hard":
            dungeon.name = "The Lost Haunt"
        dungeon.save()

def update_dungeon_bosses_health():
    dungeons = Dungeon.objects.all()
    for dungeon in dungeons:
        if dungeon.difficulty != "Easy":
            dungeon.boss_health = 500
        dungeon.save()

def update_dungeon_recommended_levels():
    dungeons = Dungeon.objects.all()
    for dungeon in dungeons:
        if dungeon.difficulty == "Easy":
            dungeon.recommended_level = 25
        elif dungeon.difficulty == "Medium":
            dungeon.recommended_level = 50
        elif dungeon.difficulty == "Hard":
            dungeon.recommended_level = 75
        dungeon.save()

def update_dungeon_rewards():
    dungeons = Dungeon.objects.all()
    for dungeon in dungeons:
        if dungeon.boss_health == 500:
            dungeon.reward = "1000 Gold"
        if dungeon.location[0] == "E":
            dungeon.reward = "New dungeon unlocked"
        if dungeon.location[len(dungeon.location) - 1] == "s":
            dungeon.reward = "Dragonheart Amulet"
        dungeon.save()

def set_new_locations():
    dungeons = Dungeon.objects.all()
    for dungeon in dungeons:
        if dungeon.recommended_level == 25:
            dungeon.location = "Enchanted Maze"
        elif dungeon.recommended_level == 50:
            dungeon.location = "Grimstone Mines"
        elif dungeon.recommended_level == 75:
            dungeon.location = "Shadowed Abyss"
        dungeon.save()

#Sixth
def show_workouts():
    workouts = Workout.objects.all()
    result = []
    for workout in workouts:
        if workout.workout_type == "Calisthenics" or workout.workout_type == "CrossFit":
            result.append(f"{workout.name} from {workout.workout_type} type has {workout.difficulty} difficulty!")
    return "\n".join(result)

def get_high_difficulty_cardio_workouts():
    workouts = Workout.objects.all()
    high_cardio_workouts = [workout for workout in workouts if workout.workout_type == "Cardio" and workout.difficulty == "High"]
    return sorted(high_cardio_workouts, key=lambda workout: workout.instructor)

def set_new_instructors():
    workouts = Workout.objects.all()
    for workout in workouts:
        if workout.workout_type == "Cardio":
            workout.instructor = "John Smith"
        elif workout.workout_type == "Strength":
            workout.instructor = "Michael Williams"
        elif workout.workout_type == "Yoga":
            workout.instructor = "Emily Johnson"
        elif workout.workout_type == "CrossFit":
            workout.instructor = "Sarah Davis"
        elif workout.workout_type == "Calisthenics":
            workout.instructor = "Chris Heria"
        workout.save()

def set_new_duration_times():
    workouts = Workout.objects.all()
    for workout in workouts:
        if workout.instructor == "John Smith":
            workout.duration = "15 minutes"
        elif workout.instructor == "Michael Williams":
            workout.duration = "1 hour"
        elif workout.instructor == "Emily Johnson":
            workout.duration = "1 hour and 30 minutes"
        elif workout.instructor == "Sarah Davis":
            workout.duration = "30 minutes"
        elif workout.instructor == "Chris Heria":
            workout.duration = "45 minutes"
        workout.save()

def delete_workouts():
    workouts = Workout.objects.all()
    for workout in workouts:
        if workout.workout_type != "Calisthenics" and workout.workout_type != "Strength":
            workout.delete()


