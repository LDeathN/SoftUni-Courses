# First Bonus Problem

budget = float(input())
type = str(input())
number = int(input())

if 1 <= number <= 4:
    transport = budget * 0.75
    left = budget - transport
elif 5 <= number <= 9:
    transport = budget * 0.60
    left = budget - transport
elif 10 <= number <= 24:
    transport = budget * 0.50
    left = budget - transport
elif 25 <= number <= 49:
    transport = budget * 0.40
    left = budget - transport
elif 50 <= number <= 200:
    transport = budget * 0.25
    left = budget - transport

if type == "VIP":
    money = number * 499.99
elif type == "Normal":
    money = number * 249.99

if left >= money:
    change = left - money
    print(f"Yes! You have {change:.2f} leva left.")
elif left < money:
    more = money - left
    print(f"Not enough money! You need {more:.2f} leva.")



# Second Bonus Problem

young = int(input())
old = int(input())
type = str(input())

if type == "trail":
    money = young * 5.50 + old * 7
elif type == "cross-country":
    money = young * 8 + old * 9.50
    if young + old >= 50:
        money = money - (money * 0.25)
elif type == "downhill":
    money = young * 12.25 + old * 13.75
elif type == "road":
    money = young * 20 + old * 21.50

total = money - (money * 0.05)
print(f"{total:.2f}")



# Third Bonus Problem

flower1 = int(input())
flower2 = int(input())
flower3 = int(input())
season = str(input())
condition = str(input())

if season == "Spring" or season == "Summer":
    money1 = flower1 * 2.00
    money2 = flower2 * 4.10
    money3 = flower3 * 2.50
    money = money3 + money2 + money1
elif season == "Autumn" or season == "Winter":
    money1 = flower1 * 3.75
    money2 = flower2 * 4.50
    money3 = flower3 * 4.15
    money = money3 + money2 + money1

if condition == "Y":
    total = money + (money * 0.15)
elif condition == "N":
    total = money

if flower3 > 7 and season == "Spring":
    total = total - (total * 0.05)
if flower2 >= 10 and season == "Winter":
    total = total - (total * 0.10)
if flower1 + flower2 + flower3 > 20:
    total = total - (total * 0.20)

total = total + 2
print(f"{total:.2f}")



# Fourth Bonus Problem

budget = float(input())
season = str(input())

if budget <= 100:
    types = "Economy class"
    if season == "Summer":
        car = "Cabrio"
        money = budget * 0.35
    elif season == "Winter":
        car = "Jeep"
        money = budget * 0.65
elif 100 < budget <= 500:
    types = "Compact class"
    if season == "Summer":
        car = "Cabrio"
        money = budget * 0.45
    elif season == "Winter":
        car = "Jeep"
        money = budget * 0.80
elif 500 < budget:
    types = "Luxury class"
    car = "Jeep"
    money = budget * 0.90

print(types)
print(f"{car} - {money:.2f}")



# Fifth Bonus Problem

budget = float(input())
season = str(input())

if budget <= 1000:
    place = "Camp"
    if season == "Summer":
        location = "Alaska"
        money = budget * 0.65
    elif season == "Winter":
        location = "Morocco"
        money = budget * 0.45
if 1000 < budget <= 3000:
    place = "Hut"
    if season == "Summer":
        location = "Alaska"
        money = budget * 0.80
    elif season == "Winter":
        location = "Morocco"
        money = budget * 0.60
if 3000 < budget:
    place = "Hotel"
    if season == "Summer":
        location = "Alaska"
        money = budget * 0.90
    elif season == "Winter":
        location = "Morocco"
        money = budget * 0.90

print(f"{location} - {place} - {money:.2f}")



# Sixth Bonus Problem

season = str(input())
km = float(input())

if km <= 5000 and (season == "Spring" or season == "Autumn"):
    month = km * 0.75
    money = month * 4
elif km <= 5000 and season == "Summer":
    month = km * 0.90
    money = month * 4
elif km <= 5000 and season == "Winter":
    month = km * 1.05
    money = month * 4
elif 5000 < km <= 10000 and (season == "Spring" or season == "Autumn"):
    month = km * 0.95
    money = month * 4
elif 5000 < km <= 10000 and season == "Summer":
    month = km * 1.10
    money = month * 4
elif 5000 < km <= 10000 and season == "Winter":
    month = km * 1.25
    money = month * 4
elif 10000 < km <= 20000:
    month = km * 1.45
    money = month * 4

total = money - (money * 0.10)
print(f"{total:.2f}")



# Seventh Bonus Problem

season = str(input())
kids = str(input())
number = int(input())
nights = int(input())

if season == "Winter":
    if kids == "boys":
        sport = "Judo"
    elif kids == "girls":
        sport = "Gymnastics"
    elif kids == "mixed":
        sport = "Ski"

    if kids == "boys" or kids == "girls":
        money = number * 9.60 * nights
    elif kids == "mixed":
        money = number * 10.00 * nights

elif season == "Spring":
    if kids == "boys":
        sport = "Tennis"
    elif kids == "girls":
        sport = "Athletics"
    elif kids == "mixed":
        sport = "Cycling"

    if kids == "boys" or kids == "girls":
        money = number * 7.20 * nights
    elif kids == "mixed":
        money = number * 9.50 * nights

elif season == "Summer":
    if kids == "boys":
        sport = "Football"
    elif kids == "girls":
        sport = "Volleyball"
    elif kids == "mixed":
        sport = "Swimming"

    if kids == "boys" or kids == "girls":
        money = number * 15.00 * nights
    elif kids == "mixed":
        money = number * 20.00 * nights

if number >= 50:
    total = money - (money * 0.50)
elif 20 <= number < 50:
    total = money - (money * 0.15)
elif 10 <= number < 20:
    total = money - (money * 0.05)
else:
    total = money
print(f"{sport} {total:.2f} lv.")



# Eighth Bonus Problem

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())

if ((x1 == x3 or x3 == x2) and y1 < y3 < y2) or ((x1 == x3 or x3 == x2) and (y1 == y3 or y3 == y2)):
    print("Border")
elif x1 < x3 < x2 and (y1 == y3 or y3 == y2) or ((x1 == x3 or x3 == x2) and (y1 == y3 or y3 == y2)):
    print("Border")
else:
    print("Inside / Outside")



# Ninth Bonus Problem

i = 1
while i <= 10:
    print(i)
    i += 1



# Tenth Bonus Problem

condition = True
while condition:
    num = float(input())
    if num < 0:
        condition = False
        continue
    result = num * 2
    print(f"Result: {result:.2f}")
print("Negative number!")