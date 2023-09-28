# First Problem (a)

from math import ceil, floor
price = float(input())
number1 = int(input())
number2 = int(input())

money1 = price * number1
money2 = price / 6 * number2
money3 = (money2 + money1) * 0.20
total = money3 + money1 + money2
print(f"Price to be paid by Djokovic {floor(total / 8)}")
print(f"Price to be paid by sponsors {ceil(total * 7 / 8)}")



# First Problem (b)

tax = int(input())

trainers = tax - (tax * 0.40)
suit = trainers - (trainers * 0.20)
ball = suit / 4
accs = ball / 5

total = tax + trainers + suit + ball + accs
print(f"{total:.2f}")



# Second Problem (a)

match1 = str(input())
match2 = str(input())
match3 = str(input())
wins = 0
loses = 0
draws = 0
if match1[0] == match1[2]:
    draws += 1
elif match1[0] > match1[2]:
    wins += 1
elif match1[0] < match1[2]:
    loses += 1

if match2[0] == match2[2]:
    draws += 1
elif match2[0] > match2[2]:
    wins += 1
elif match2[0] < match2[2]:
    loses += 1

if match3[0] == match3[2]:
    draws += 1
elif match3[0] > match3[2]:
    wins += 1
elif match3[0] < match3[2]:
    loses += 1

print(f"Team won {wins} games.")
print(f"Team lost {loses} games.")
print(f"Drawn games: {draws}")



# Second Problem (b)

record = int(input())
seconds = int(input())
distance = float(input())
seconds_for_100 = int(input())

record = record * 60 + seconds
waste = distance / 120
wasted_time = waste * 2.5
total = (distance / 100) * seconds_for_100 - wasted_time

if total <= record:
    print(f"Marin Bangiev won an Olympic quota!")
    print(f"His time is {total:.3f}.")
elif total > record:
    more = total - record
    print(f"No, Marin failed! He was {more:.3f} second slower.")



# Third Problem (a)

country = str(input())
types = str(input())

if country == "Russia" and types == "ribbon":
    diff = 9.100
    per = 9.400
    grade = diff + per
elif country == "Russia" and types == "hoop":
    diff = 9.300
    per = 9.800
    grade = diff + per
elif country == "Russia" and types == "rope":
    diff = 9.600
    per = 9.000
    grade = diff + per
elif country == "Bulgaria" and types == "ribbon":
    diff = 9.600
    per = 9.400
    grade = diff + per
elif country == "Bulgaria" and types == "hoop":
    diff = 9.550
    per = 9.750
    grade = diff + per
elif country == "Bulgaria" and types == "rope":
    diff = 9.500
    per = 9.400
    grade = diff + per
elif country == "Italy" and types == "ribbon":
    diff = 9.200
    per = 9.500
    grade = diff + per
elif country == "Italy" and types == "hoop":
    diff = 9.450
    per = 9.350
    grade = diff + per
elif country == "Italy" and types == "rope":
    diff = 9.700
    per = 9.150
    grade = diff + per

print(f"The team of {country} get {grade:.3f} on {types}.")
print(f"{100 - (grade / 20 * 100):.2f}%")



# Third Problem (b)

place = str(input())
types = str(input())
tickets = int(input())
picture = str(input())
price = 0
if place == "Quarter final" and types == "Standard":
    price = 55.50
elif place == "Semi final" and types == "Standard":
    price = 75.88
elif place == "Final" and types == "Standard":
    price = 110.10
elif place == "Quarter final" and types == "Premium":
    price = 105.20
elif place == "Semi final" and types == "Premium":
    price = 125.22
elif place == "Final" and types == "Premium":
    price = 160.66
elif place == "Quarter final" and types == "VIP":
    price = 118.90
elif place == "Semi final" and types == "VIP":
    price = 300.40
elif place == "Final" and types == "VIP":
    price = 400.00

money = price * tickets
if money > 4000:
    total = money - (money * 0.25)
elif 2500 < money <= 4000:
    total = money - (money * 0.10)
elif money <= 2500:
    total = money

if picture == "Y" and money <= 4000:
    total = total + (tickets * 40)
elif picture == "N":
    total = total
print(f"{total:.2f}")



# Fourth Problem (a)

name1 = str(input())
name2 = str(input())
points1 = 0
points2 = 0
card = input()
card1 = int(input())


while card != "End of game":
    card2 = int(card)
    if card1 > card2:
        diff = card1 - card2
        points1 += diff
    elif card2 > card1:
        diff = card2 - card1
        points2 += diff
    elif card2 == card1:
        print("Number wars!")
        card1 = int(input())
        card2 = int(input())
        if card1 > card2:
            win = name1
            print(f"{win} is winner with {points2} points")
            break
        elif card2 > card1:
            win = name2
            print(f"{win} is winner with {points1} points")
            break
    card = input()
    if str(card) == "End of game":
        break
    card1 = int(input())

if card == "End of game":
    print(f"{name1} has {points2} points")
    print(f"{name2} has {points1} points")



# Fourth Problem (b)

total = 301
count = 0
miss = 0
name = str(input())
hit = str(input())
while hit != "Retire" and total != 0:
    points = int(input())
    if hit == "Single":
        points = points
    elif hit == "Double":
        points = points * 2
    elif hit == "Triple":
        points = points * 3

    if points <= total:
        total -= points
        count += 1
        if total == 0:
            break
    elif points > total:
        miss += 1
    hit = str(input())

if total == 0:
    print(f"{name} won the leg with {count} shots.")
elif hit == "Retire":
    print(f"{name} retired after {miss} unsuccessful shots.")



# Fifth Problem (a)

from math import floor
number = int(input())
starting = int(input())
total = 0
wins = 0
count = 0
for i in range(1, number + 1):
    place = str(input())
    if place == "W":
        total += 2000
        wins += 1
    elif place == "F":
        total += 1200
        count += 1
    elif place == "SF":
        total += 720
        count += 1

average = total / (count + wins)
finish = total + starting
win = wins / number * 100
print(f"Final points: {finish}")
print(f"Average points: {floor(average)}")
print(f"{win:.2f}%")



# Fifth Problem (b)

people = int(input())
back = 0
chest = 0
legs = 0
abs = 0
protein_shake = 0
protein_bar = 0
for i in range(1, people + 1):
    doing = str(input())
    if doing == "Back":
        back += 1
    elif doing == "Chest":
        chest += 1
    elif doing == "Legs":
        legs += 1
    elif doing == "Abs":
        abs += 1
    elif doing == "Protein shake":
        protein_shake += 1
    elif doing == "Protein bar":
        protein_bar += 1

protein = protein_shake + protein_bar
train = back + chest + legs + abs

print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{train / people * 100:.2f}% - work out")
print(f"{protein / people * 100:.2f}% - protein")



# Sixth Problem (a)

goal = int(input())
count = 0
total = 0
current = 0
height = goal - 30
condition = True
while condition:
    count = 0
    if current > goal and height > goal:
        condition = False
        break
    for i in range(1, 4):
        total += 1
        current = int(input())
        if current > height:
           height += 5
           break
        elif current <= height:
            count += 1

        if count == 3:
            condition = False

if current > goal and height > goal:
    print(f"Tihomir succeeded, he jumped over {goal}cm after {total} jumps.")
elif current <= goal:
    print(f"Tihomir failed at {height}cm after {total} jumps.")



# Sixth Problem (b)

name = ""
wins = 0
loses = 0
total = 0
while name != "End of tournaments":
    name = str(input())
    if name == "End of tournaments":
        continue
    matches = int(input())
    for i in range(1, matches + 1):
        total += 1
        points1 = int(input())
        points2 = int(input())
        if points1 > points2:
            wins += 1
            print(f"Game {i} of tournament {name}: win with {points1 - points2} points.")
        elif points2 > points1:
            loses += 1
            print(f"Game {i} of tournament {name}: lost with {points2 - points1} points.")


print(f"{wins / total  * 100:.2f}% matches win")
print(f"{loses / total * 100:.2f}% matches lost")