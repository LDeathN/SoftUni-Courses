# First Bonus Problem

volume = int(input())
pipe1 = int(input())
pipe2 = int(input())
hours = float(input())

volume1 = pipe1 * hours
volume2 = pipe2 * hours

if volume >= volume1 + volume2:
    percentage1 = volume1 / (volume1 + volume2) * 100
    percentage2 = volume2 / (volume1 + volume2) * 100
    percentage = (volume1 + volume2) / volume * 100
    print(f"The pool is {percentage:.2f}% full. Pipe 1: {percentage1:.2f}%. Pipe 2: {percentage2:.2f}%.")
elif volume < volume1 + volume2:
    overflown = volume1 + volume2 - volume
    print(f"For {hours} hours the pool overflows with {overflown:.2f} liters.")



# Second Bonus Problem

free = int(input())
working = 365 - free
time = free * 127 + working * 63

if time > 30000:
    print("Tom will run away")
    difference = time - 30000
    hours = difference // 60
    minutes = difference % 60
    print(f"{hours} hours and {minutes} minutes more for play")
elif time < 30000:
    print("Tom sleeps well")
    difference = 30000 - time
    hours = difference // 60
    minutes = difference % 60
    print(f"{hours} hours and {minutes} minutes less for play")



# Third Bonus Problem

from math import floor, ceil
area = int(input())
grapes = float(input())
needed = int(input())
workers = int(input())

used = area * 0.40
kilos = grapes * used
sake = kilos / 2.5

if sake >= needed:
    print(f"Good harvest this year! Total wine: {floor(sake)} liters.")
    left = sake - needed
    for_worker = left / workers
    print(f"{ceil(left)} liters left -> {ceil(for_worker)} liters per person.")
elif sake < needed:
    more = needed - sake
    print(f"It will be a tough winter! More {floor(more)} liters wine needed.")



# Fourth Bonus Problem

distance = int(input())
time = str(input())
bus = 1000000
train = 1000000
if time == "day":
    taxi = distance * 0.79 + 0.70
    if distance >= 20:
        bus = distance * 0.09
    if distance >= 100:
        train = distance * 0.06
elif time == "night":
    taxi = distance * 0.90 + 0.70
    if distance >= 20:
        bus = distance * 0.09
    if distance >= 100:
        train = distance * 0.06

if train < taxi and train < bus:
    smallest = train
elif bus < taxi and bus < train:
    smallest = bus
elif taxi < bus and taxi < train:
    smallest = taxi

print(f"{smallest:.2f}")



# Fifth Bonus Problem

from math import floor, ceil
gone = int(input())
food = int(input())
dog = float(input())
cat = float(input())
turtle = float(input())

dog1 = dog * gone
cat1 = cat * gone
turtle1 = turtle * gone / 1000
sum = dog1 + cat1 + turtle1

if food >= sum:
    left = abs(sum - food)
    print(f"{floor(left)} kilos of food left.")
elif food < sum:
    more = abs(food - sum)
    print(f"{ceil(more)} more kilos of food are needed.")



# Sixth Bonus Problem

from math import floor,ceil
flower1 = int(input())
flower2 = int(input())
flower3 = int(input())
flower4 = int(input())
present = float(input())

money1 = flower1 * 3.25
money2 = flower2 * 4.00
money3 = flower3 * 3.50
money4 = flower4 * 8.00
money = money4 + money3 + money2 + money1
total = money - (money * 0.05)

if total >= present:
    left = total - present
    print(f"She is left with {floor(left)} leva.")
elif total < present:
    more = present - total
    print(f"She will have to borrow {ceil(more)} leva.")



# Seventh Bonus Problem

type = str(input())
amount = float(input())
if type == "Diesel" or type == "Gasoline" or type == "Gas":
    if amount >= 25:
        print(f"You have enough {type.lower()}.")
    elif amount < 25:
        print(f"Fill your tank with {type.lower()}!")
else:
    print("Invalid fuel!")



# Eighth Bonus Problem

type = str(input())
amount = float(input())
card = str(input())

if type == "Gas":
    money = amount * 0.93
elif type == "Gasoline":
    money = amount * 2.22
elif type == "Diesel":
    money = amount * 2.33

if card == "Yes" and type == "Gas":
    money = money - amount * 0.08
elif card == "Yes" and type == "Gasoline":
    money = money - amount * 0.18
elif card == "Yes" and type == "Diesel":
    money = money - amount * 0.12

if 20 <= amount <= 25:
    total = money - (money * 0.08)
elif amount > 25:
    total = money - (money * 0.10)
else:
    total = money
print(f"{total:.2f} lv.")