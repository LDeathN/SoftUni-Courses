# First Problem

num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
result = (num1 + num2) // num3 * num4
print(f"{result:.0f}")



# Second Problem

first = str(input())
second = str(input())
third = str(input())

print(f"{first}{second}{third}")



# Third Problem

from math import ceil
total = int(input())
people = int(input())

courses = total / people
print(ceil(courses))



# Fourth Problem

n = int(input())
total = 0
for i in range(1, n + 1):
    symbol = str(input())
    for j in range(33, 128):
        if ord(symbol) == j:
            total += j

print(f"The sum equals: {total}")



# Fifth Problem

start = int(input())
end = int(input())
for i in range(start, end + 1):
    print(f"{chr(i)} ", end="")



# Sixth Problem

n = int(input())
for i in range(97, 97 + n):
    for j in range(97, 97 + n):
        for h in range(97, 97 + n):
            print(f"{chr(i)}{chr(j)}{chr(h)}")



# Seventh Problem

n = int(input())
capacity = 255
total = 0
inside = 0
for i in range(1, n + 1):
    poured = int(input())
    total += poured
    if capacity < total:
        total -= poured
        print("Insufficient capacity!")
    elif capacity >= total:
        inside += poured
print(inside)



# Eighth Problem

group = int(input())
days = int(input())
coins = 0
left = 0
spend = 0
for i in range(1, days + 1):
    if i % 10 == 0:
        group -= 2
    if i % 15 == 0:
        group += 5
    coins += 50
    spend += 2 * group
    if i % 3 == 0:
        spend += 3 * group
    if i % 5 == 0:
        coins += 20 * group
        if i % 3 == 0:
            spend += 2 * group

left += coins - spend
each = left // group
print(f"{group} companions received {each} coins each.")



# Ninth Problem

n = int(input())
maximum = 0
save1 = 0
save2 = 0
save3 = 0
for i in range(1, n + 1):
    weight = int(input())
    time = int(input())
    quality = int(input())
    value = (weight / time) ** quality
    if value > maximum:
        maximum = value
        save1 = weight
        save2 = time
        save3 = quality
print(f"{save1} : {save2} = {maximum:.0f} ({save3})")



# Tenth Problem

loses = int(input())
price1 = float(input())
price2 = float(input())
price3 = float(input())
price4 = float(input())
helmet = 0
sword = 0
shield = 0
armor = 0
for i in range(1, loses + 1):
    if i % 2 == 0:
        helmet += 1
    if i % 3 == 0:
        sword += 1
    if i % 2 == 0 and i % 3 == 0:
        shield += 1
        if shield % 2 == 0 and shield != 0:
            armor += 1

total = helmet * price1 + sword * price2 + shield * price3 + armor * price4
print(f"Gladiator expenses: {total:.2f} aureus")