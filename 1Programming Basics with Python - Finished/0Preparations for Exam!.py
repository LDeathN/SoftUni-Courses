# First Prep Exam Problem

money = int(input())
statues = money - money * 0.30
service = statues - statues * 0.15
sound = service / 2
total = money + statues + service + sound
print(f"{total:.2f}")



# Second Prep Exam Problem

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



# Third Prep Exam Problem

stage = str(input())
type = str(input())
amount = int(input())
picture = str(input())
condition = False
if stage == "Quarter final" and type == "Standard":
    price = 55.50
elif stage == "Quarter final" and type == "Premium":
    price = 105.20
if stage == "Quarter final" and type == "VIP":
    price = 118.90
if stage == "Semi final" and type == "Standard":
    price = 75.88
if stage == "Semi final" and type == "Premium":
    price = 125.22
if stage == "Semi final" and type == "VIP":
    price = 300.40
if stage == "Final" and type == "Standard":
    price = 110.10
if stage == "Final" and type == "Premium":
    price = 160.66
if stage == "Final" and type == "VIP":
    price = 400.00

money = price * amount
if money <= 4000:
    condition = True

if money > 4000:
    total = money - money * 0.25
elif 2500 <= money <= 4000:
    total = money - money * 0.10
else:
    total = money

if picture == "Y" and condition:
    total = total + (amount * 40)
elif picture == "N":
    total = total

print(f"{total:.2f}")



# Fourth Prep Exam Problem

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


# Fifth Prep Exam Problem

from math import ceil
height = int(input())
width = int(input())
percentage = int(input())
area = height * width * 4
painting = ceil(area - (area * percentage / 100))
total = 0
condition = True
while condition:
    painted = input()
    if painted == "Tired!":
        need = painting - total
        print(f"{need} quadratic m left.")
        condition = False
        continue
    total += int(painted)
    if total == painting:
        print(f"All walls are painted! Great job, Pesho!")
        condition = False
    elif total > painting:
        left = total - painting
        print(f"All walls are painted and you have {left} l paint left!")
        condition = False



# Sixth Prep Exam Problem

num1 = int(input())
num2 = int(input())
digit1 = num1 // 1000
digit2 = num2 // 1000
digit3 = (num1 % 1000) // 100
digit4 = (num2 % 1000) // 100
digit5 = ((num1 % 1000) % 100) // 10
digit6 = ((num2 % 1000) % 100) // 10
digit7 = ((num1 % 1000) % 100) % 10
digit8 = ((num2 % 1000) % 100) % 10
for i1 in range(digit1, digit2 + 1):
    if i1 % 2 == 0:
        continue
    else:
        position1 = i1
    for i2 in range(digit3, digit4 + 1):
        if i2 % 2 == 0:
            continue
        else:
            position2 = i2
        for i3 in range(digit5, digit6 + 1):
            if i3 % 2 == 0:
                continue
            else:
                position3 = i3
            for i4 in range(digit7, digit8 + 1):
                if i4 % 2 == 0:
                    continue
                else:
                    position4 = i4
                    print(f"{position1}{position2}{position3}{position4}" + " ", end="")