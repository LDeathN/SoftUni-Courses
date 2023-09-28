# First Problem

price = float(input())
bananas = float(input())
oranges = float(input())
berries = float(input())
strawberries = float(input())
money4 = price * strawberries
price1 = price / 2
money1 = price1 * berries
price2 = price1 * 0.60
money2 = price2 * oranges
price3 = price1 * 0.20
money3 = price3 * bananas
money = money3 + money2 + money1 + money4
print(f"{money:.2f}")



# Second Problem

budget = float(input())
gas = float(input())
day = str(input())

money = gas * 2.10 + 100
if day == "Saturday":
    money = money * 0.90
elif day == "Sunday":
    money = money * 0.80

if budget >= money:
    print(f"Safari time! Money left: {budget - money:.2f} lv.")
elif budget < money:
    print(f"Not enough money! Money needed: {money - budget:.2f} lv.")



# Third Problem

contract = str(input())
types = str(input())
option = str(input())
months = int(input())

if contract == "one":
    if types == "Small":
        price = 9.98
    elif types == "Middle":
        price = 18.99
    elif types == "Large":
        price = 25.98
    elif types == "ExtraLarge":
        price = 35.99
elif contract == "two":
    if types == "Small":
        price = 8.58
    elif types == "Middle":
        price = 17.09
    elif types == "Large":
        price = 23.59
    elif types == "ExtraLarge":
        price = 31.79

if option == "yes":
    if price <= 10:
        price += 5.50
    elif price <= 30:
        price += 4.35
    elif price > 30:
        price += 3.85
elif option == "no":
    price = price
money = months * price
if contract == "two":
    money = money * 96.25 / 100

print(f"{money:.2f} lv.")



# Fourth Problem

budget = float(input())
name = ""
count = 0
total = 0

while name != "Stop":
    name = str(input())
    if name == "Stop":
        continue
    price = float(input())
    count += 1
    if count % 3 == 0:
        price = price / 2
    budget -= price
    total += price
    if budget < 0:
        break

if name == "Stop":
    print(f"You bought {count} products for {total:.2f} leva.")
elif budget < 0:
    print(f"You don't have enough money!")
    print(f"You need {abs(budget):.2f} leva!")



# Fifth Problem

n = int(input())
div2 = 0
div3 = 0
div4 = 0
count = 0
for i in range(1, n + 1):
    number = int(input())
    count += 1
    if number % 2 == 0:
        div2 += 1
    if number % 3 == 0:
        div3 += 1
    if number % 4 == 0:
        div4 += 1

print(f"{div2 / count * 100:.2f}%")
print(f"{div3 / count * 100:.2f}%")
print(f"{div4 / count * 100:.2f}%")



# Sixth Problem

days = int(input())
hours = int(input())
total = 0
for i in range(1, days + 1):
    price = 0
    for j in range(1, hours + 1):
        if i % 2 == 0 and j % 2 != 0:
            price += 2.50
        elif i % 2 != 0 and j % 2 == 0:
            price += 1.25
        else:
            price += 1
    print(f"Day: {i} - {price:.2f} leva")
    total += price
print(f"Total: {total:.2f} leva")