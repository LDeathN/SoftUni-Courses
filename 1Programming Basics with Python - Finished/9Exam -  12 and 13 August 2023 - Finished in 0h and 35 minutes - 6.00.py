# First Problem

from math import ceil
price_per_video_card = int(input())
price_per_transitional = int(input())
price_for_electricity_per_day = float(input())
profit_per_day = float(input())
total = 13 * price_per_video_card + 13 * price_per_transitional + 1000
days = ceil(total / ((profit_per_day - price_for_electricity_per_day) * 13))
print(total)
print(days)



# Second Problem

from math import ceil
name = input()
budget = float(input())
amount_beer = int(input())
amount_chips = int(input())
total_beer = 1.20 * amount_beer
total_chips = ceil((0.45 * total_beer) * amount_chips)
total = total_chips + total_beer
if total <= budget:
    print(f"{name} bought a snack and has {(budget - total):.2f} leva left.")
else:
    print(f"{name} needs {(total - budget):.2f} more leva!")



# Third Problem

month = input()
hours = int(input())
people = int(input())
day_night_time = input()
if month == "march" or month == "april" or month == "may":
    if day_night_time == "day":
        price_per_person = 10.50
    else:
        price_per_person = 8.40
elif month == "june" or month == "july" or month == "august":
    if day_night_time == "day":
        price_per_person = 12.60
    else:
        price_per_person = 10.20

if people >= 4:
    price_per_person = price_per_person * 0.90
if hours >= 5:
    price_per_person = price_per_person * 0.50

total = price_per_person * people * hours

print(f"Price per person for one hour: {price_per_person:.2f}")
print(f"Total cost of the visit: {total:.2f}")



# Fourth Problem

N = int(input())
M = int(input())
S = int(input())
for i in range(M, N - 1, -1):
    if i % 2 == 0 and i % 3 == 0:
        if i != S:
            print(i, end=" ")
        elif i == S:
            break



# Fifth Problem

kids = 0
adults = 0
kids_cost = 0
adults_cost = 0
while True:
    check = input()
    if check == "Christmas":
        break
    years = int(check)
    if years <= 16:
        kids += 1
        kids_cost += 5
    elif years > 16:
        adults += 1
        adults_cost += 15
print(f"Number of adults: {adults}")
print(f"Number of kids: {kids}")
print(f"Money for toys: {kids_cost}")
print(f"Money for sweaters: {adults_cost}")



# Sixth Problem

locations = int(input())
for i in range(locations):
    total_gold = 0
    expected_gold_per_day = float(input())
    days_at_location = int(input())
    for j in range(days_at_location):
        gold_per_day = float(input())
        total_gold += gold_per_day
    if total_gold / days_at_location >= expected_gold_per_day:
        print(f"Good job! Average gold per day: {(total_gold / days_at_location):.2f}.")
    elif total_gold / days_at_location < expected_gold_per_day:
        print(f"You need {(expected_gold_per_day - (total_gold / days_at_location)):.2f} gold.")


