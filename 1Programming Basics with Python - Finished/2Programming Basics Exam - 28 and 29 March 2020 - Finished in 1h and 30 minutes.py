# First Problem (a)

price = float(input())
cake = price * 0.20
drinks = cake - (cake * 0.45)
animator = price / 3
money = price + cake + drinks + animator
print(money)



# First Problem (b)

bitcoin = int(input())
china = float(input())
commission = float(input())
leva = 0
leva += bitcoin * 1168
dollar = china * 0.15
leva += dollar * 1.76
euro = leva / 1.95
takeaway = euro * commission / 100
total = euro - takeaway
print(f"{total:.2f}")



# Second Problem (a)

minutes = int(input())
times = int(input())
cal = int(input())
burn = minutes * 5
total = burn * times
if total >= cal / 2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {total}.")
elif total < cal / 2:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total}.")



# Second Problem (b)

record = float(input())
distance = float(input())
speed = float(input())

factor = distance // 50
slowness = factor * 30
time = (speed * distance) + slowness

if time >= record:
    difference = abs(time - record)
    print(f"No! He was {difference:.2f} seconds slower.")
if time < record:
    print(f"Yes! The new record is {time:.2f} seconds.")



# Third Problem (a)

fruit = str(input())
types = str(input())
bought = int(input())
money = 0
if fruit == "Watermelon" and types == "small":
    money = 56.00 * 2
elif fruit == "Watermelon" and types == "big":
    money = 28.70 * 5
elif fruit == "Mango" and types == "small":
    money = 36.66 * 2
elif fruit == "Mango" and types == "big":
    money = 19.60 * 5
elif fruit == "Pineapple" and types == "small":
    money = 42.10 * 2
elif fruit == "Pineapple" and types == "big":
    money = 24.80 * 5
elif fruit == "Raspberry" and types == "small":
    money = 20.00 * 2
elif fruit == "Raspberry" and types == "big":
    money = 15.20 * 5

total = money * bought
if 400 <= total <= 1000:
    total = total - (total * 0.15)
elif total > 1000:
    total = total / 2
else:
    total = total

print(f"{total:.2f} lv.")



# Third Problem (b)

budget = float(input())
gender = str(input())
age = int(input())
sport = str(input())
money = 0
if gender == "m" and sport == "Gym":
    money = 42
elif gender == "m" and sport == "Boxing":
    money = 41
elif gender == "m" and sport == "Yoga":
    money = 45
elif gender == "m" and sport == "Zumba":
    money = 34
elif gender == "m" and sport == "Dances":
    money = 51
elif gender == "m" and sport == "Pilates":
    money = 39
elif gender == "f" and sport == "Gym":
    money = 35
elif gender == "f" and sport == "Boxing":
    money = 37
elif gender == "f" and sport == "Yoga":
    money = 42
elif gender == "f" and sport == "Zumba":
    money = 31
elif gender == "f" and sport == "Dances":
    money = 53
elif gender == "f" and sport == "Pilates":
    money = 37

if age <= 19:
    money = money - (money * 0.20)
elif age > 19:
    money = money

if budget >= money:
    print(f"You purchased a 1 month pass for {sport}.")
elif budget < money:
    more = money - budget
    print(f"You don't have enough money! You need ${more:.2f} more.")



# Fourth Problem (a)

days = int(input())
food = float(input())
count = 0
biscuits = 0
total_dog = 0
total_cat = 0
for i in range(1, days + 1):
    count += 1
    dog = int(input())
    cat = int(input())
    total_dog += dog
    total_cat += cat
    if count % 3 == 0:
        biscuits += dog / 10
        biscuits += cat / 10

print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{(total_cat + total_dog) / food * 100:.2f}% of the food has been eaten.")
print(f"{total_dog / (total_cat + total_dog) * 100:.2f}% eaten from the dog.")
print(f"{total_cat / (total_cat + total_dog) * 100:.2f}% eaten from the cat.")



# Fourth Problem (b)

groups = int(input())
place1 = 0
place2 = 0
place3 = 0
place4 = 0
place5 = 0
total = 0
for i in range(1, groups + 1):
    people = int(input())
    if people <= 5:
        place1 += people
        total += people
    elif 5 < people <= 12:
        place2 += people
        total += people
    elif 12 < people <= 25:
        place3 += people
        total += people
    elif 25 < people <= 40:
        place4 += people
        total += people
    elif people > 40:
        place5 += people
        total += people

print(f"{place1 / total * 100:.2f}%")
print(f"{place2 / total * 100:.2f}%")
print(f"{place3 / total * 100:.2f}%")
print(f"{place4 / total * 100:.2f}%")
print(f"{place5 / total * 100:.2f}%")



# Fifth Problem (a)

food = int(input())
food = food * 1000
eaten = input()
dog = 0
while eaten != "Adopted":
    dog += int(eaten)
    eaten = input()

if food >= dog:
    left = food - dog
    print(f"Food is enough! Leftovers: {left} grams.")
elif food < dog:
    more = dog - food
    print(f"Food is not enough. You need {more} grams more.")



# Fifth Problem (b)

capacity = float(input())
volume = input()
count = 0
total = 0
condition = False
while volume != "End" or condition:
    count += 1
    space = float(volume)
    if count % 3 == 0:
        space = space * 1.10
    total += space
    if total > capacity:
        condition = True
        count -= 1
        break
    volume = input()

if volume == "End":
    print("Congratulations! All suitcases are loaded!")
elif condition:
    print("No more space!")

print(f"Statistic: {count} suitcases loaded.")



# Sixth Problem

days = int(input())
wins = 0
loses = 0
money = 0
total = 0
days_won = 0
days_lost = 0
for i in range(1, days + 1):
    sport = str(input())
    while sport != "Finish":
        result = str(input())
        if result == "win":
            wins += 1
            money += 20
        elif result == "lose":
            loses += 1
        sport = str(input())
    sport = ""
    if wins > loses:
        money = money * 1.10
        days_won += 1
    elif wins < loses:
        money = money
        days_lost += 1
    total += money
    money = 0
    wins = 0
    loses = 0
if days_won > days_lost:
    total = total * 1.20
    print(f"You won the tournament! Total raised money: {total:.2f}")
elif days_won < days_lost:
    total = total
    print(f"You lost the tournament! Total raised money: {total:.2f}")