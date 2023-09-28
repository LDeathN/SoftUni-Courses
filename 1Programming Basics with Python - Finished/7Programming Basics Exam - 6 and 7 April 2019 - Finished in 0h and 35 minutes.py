# First Problem

tax = int(input())
statues = tax * 0.70
service = statues * 0.85
music = service / 2
total = tax + statues + service + music
print(f"{total:.2f}")



# Second Problem

budget = float(input())
decoration = budget * 0.10
people = int(input())
price = float(input())
money = price * people
if people > 150:
    money = money * 0.90
total = money + decoration
if budget >= total:
    print(f"Action!")
    print(f"Wingard starts filming with {budget - total:.2f} leva left.")
elif budget < total:
    print(f"Not enough money!")
    print(f"Wingard needs {total - budget:.2f} leva more.")



# Third Problem

name = str(input())
types = str(input())
tickets = int(input())

if name == "A Star Is Born":
    if types == "normal":
        price = 7.50
    elif types == "luxury":
        price = 10.50
    elif types == "ultra luxury":
        price = 13.50
elif name == "Bohemian Rhapsody":
    if types == "normal":
        price = 7.35
    elif types == "luxury":
        price = 9.45
    elif types == "ultra luxury":
        price = 12.75
elif name == "Green Book":
    if types == "normal":
        price = 8.15
    elif types == "luxury":
        price = 10.25
    elif types == "ultra luxury":
        price = 13.25
elif name == "The Favourite":
    if types == "normal":
        price = 8.75
    elif types == "luxury":
        price = 11.55
    elif types == "ultra luxury":
        price = 13.95

money = price * tickets
print(f"{name} -> {money:.2f} lv.")



# Fourth Problem

budget = int(input())
bought = ""
tickets = 0
other = 0
total = 0
while bought != "End":
    bought = str(input())
    if bought == "End":
        continue
    if len(bought) > 8:
        total += ord(bought[0]) + ord(bought[1])
        if budget >= total:
            tickets += 1
        else:
            break
    elif len(bought) <= 8:
        total += ord(bought[0])
        if budget >= total:
            other += 1
        else:
            break

print(f"{tickets}")
print(f"{other}")



# Fifth Problem

films = int(input())
maximum = 0
minimum = 10
total = 0
biggest = ""
lowest = ""
for i in range(1, films + 1):
    name = str(input())
    rating = float(input())
    total += rating
    if rating > maximum:
        maximum = rating
        biggest = name
    if rating < minimum:
        minimum = rating
        lowest = name

print(f"{biggest} is with highest rating: {maximum:.1f}")
print(f"{lowest} is with lowest rating: {minimum:.1f}")
print(f"Average rating: {total / films:.1f}")



# Sixth Problem

name = ""
student = 0
standard = 0
kid = 0
total = 0
count = 0
while name != "Finish":
    types = ""
    total += count
    count = 0
    name = str(input())
    if name == "Finish":
        continue
    spaces = int(input())

    while types != "End" and count < spaces:
        types = str(input())
        if types == "End":
            continue
        count += 1
        if types == "student":
            student += 1
        elif types == "standard":
            standard += 1
        elif types == "kid":
            kid += 1
    print(f"{name} - {count / spaces * 100:.2f}% full.")

print(f"Total tickets: {total}")
print(f"{student / total * 100:.2f}% student tickets.")
print(f"{standard / total * 100:.2f}% standard tickets.")
print(f"{kid / total * 100:.2f}% kids tickets.")