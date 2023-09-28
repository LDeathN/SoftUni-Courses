# First Problem (a)

from math import floor
name = str(input())
seasons = int(input())
episodes = int(input())
time = float(input())
total_time = time + (time * 0.20)
special = seasons * 10
absolute = seasons * (episodes * total_time) + special
print(f"Total time needed to watch the {name} series is {floor(absolute)} minutes.")



# First Problem (b)

name = str(input())
days = int(input())
tickets = int(input())
price = float(input())
percentage = int(input())

money = tickets * price
total = money * days
tax = total * percentage / 100
final = total - tax
print(f"The profit from the movie {name} is {final:.2f} lv.")



# Second Problem

time = int(input())
scenes = int(input())
scene_time = int(input())

prep = time * 0.15
needed = scenes * scene_time + prep
if needed <= time:
    left = time - needed
    print(f"You managed to finish the movie on time! You have {round(left)} minutes left!")
elif needed > time:
    more = needed - time
    print(f"Time is up! To complete the movie you need {round(more)} minutes.")



# Third Problem (a)

movie = str(input())
types = str(input())
tickets = int(input())
price = 0
if movie == "John Wick" and types == "Drink":
    price = 12
elif movie == "John Wick" and types == "Popcorn":
    price = 15
elif movie == "John Wick" and types == "Menu":
    price = 19
elif movie == "Star Wars" and types == "Drink":
    price = 18
elif movie == "Star Wars" and types == "Popcorn":
    price = 25
elif movie == "Star Wars" and types == "Menu":
    price = 30
elif movie == "Jumanji" and types == "Drink":
    price = 9
elif movie == "Jumanji" and types == "Popcorn":
    price = 11
elif movie == "Jumanji" and types == "Menu":
    price = 14

total = tickets * price
if movie == "Star Wars" and tickets >= 4:
    total = total - (total * 0.30)
if movie == "Jumanji" and tickets == 2:
    total = total - (total * 0.15)

print(f"Your bill is {total:.2f} leva.")



# Third Problem (b)

budget = float(input())
place = str(input())
season = str(input())
days = int(input())
price = 0
if place == "Dubai" and season == "Winter":
    price = 45000
elif place == "Dubai" and season == "Summer":
    price = 40000
elif place == "Sofia" and season == "Winter":
    price = 17000
elif place == "Sofia" and season == "Summer":
    price = 12500
elif place == "London" and season == "Winter":
    price = 24000
elif place == "London" and season == "Summer":
    price = 20250
total = days * price
if place == "Dubai":
    total = total - (total * 0.30)
if place == "Sofia":
    total = total + (total * 0.25)

if budget >= total:
    left = budget - total
    print(f"The budget for the movie is enough! We have {left:.2f} leva left!")
elif budget < total:
    more = total - budget
    print(f"The director needs {more:.2f} leva more!")



# Fourth Problem (a)

capacity = int(input())
question = str(input())
flag = False
total = 0
money = 0
while question != "Movie time!" and flag == False:
    people = int(question)
    total += people
    if total > capacity:
        print("The cinema is full.")
        print(f"Cinema income - {money} lv.")
        flag = True
        continue
    price = people * 5
    if people % 3 == 0:
        price = price - 5
    money += price
    question = str(input())

if question == "Movie time!":
    left = capacity - total
    print(f"There are {left} seats left in the cinema.")
    print(f"Cinema income - {money} lv.")



# Fourth Problem (b)

budget = float(input())
name = str(input())
flag = False
price = 0
while name != "ACTION" and flag == False:
    if len(name) <= 15:
        price = float(input())
        budget -= price
    elif len(name) > 15:
        price = budget * 0.20
        budget -= price

    if budget < 0:
        flag = True
        more = abs(budget)
        print(f"We need {more:.2f} leva for our actors.")
        continue
    name = str(input())

if name == "ACTION":
    left = budget
    print(f"We are left with {left:.2f} leva.")



# Fifth Problem (a)

budget = float(input())
number = int(input())
total = 0
for i in range(1, number + 1):
    name = str(input())
    price = float(input())
    if name == "Thrones":
        price = price - (price * 0.50)
    if name == "Lucifer":
        price = price - (price * 0.40)
    if name == "Protector":
        price = price - (price * 0.30)
    if name == "TotalDrama":
        price = price - (price * 0.20)
    if name == "Area":
        price = price - (price * 0.10)
    total += price

if budget >= total:
    left = budget - total
    print(f"You bought all the series and left with {left:.2f} lv.")
elif budget < total:
    more = total - budget
    print(f"You need {more:.2f} lv. more to buy the series! ")



# Fifth Problem (b)

actor = str(input())
points = float(input())
graders = int(input())
condition = True
for i in range(1, graders + 1):
    name = str(input())
    given_points = float(input())
    letters = len(name)
    received_points = letters * given_points / 2
    points += received_points
    if points > 1250.5:
        print(f"Congratulations, {actor} got a nominee for leading role with {points:.1f}!")
        condition = False
        break

if condition:
    need = abs(points - 1250.5)
    print(f"Sorry, {actor} you need {need:.1f} more!")



# Sixth Problem (a)

name = str(input())
count = 0
maximum = 0
flag = False
while name != "STOP":
    points = 0
    count += 1
    if count == 7:
        flag = True
        break
    for j in range(0, len(name)):
        points += ord(name[j])
        if 65 <= ord(name[j]) <= 90:
            points -= len(name)
        if 97 <= ord(name[j]) <= 122:
            points -= len(name) * 2

    if points > maximum:
        maximum = points
        winner = name

    name = str(input())
    if name == "STOP":
        break

if flag:
    print(f"The limit is reached.")
print(f"The best movie for you is {winner} with {maximum} ASCII sum.")



# Sixth Problem (b)

a1 = int(input())
a2 = int(input())
n = int(input())
for i in range(a1, a2):
    for j in range(1, n):
        for h in range(1, (n // 2)):
            if i % 2 != 0 and (j + h + i) % 2 != 0:
                print(f"{chr(i)}-{j}{h}{i}")