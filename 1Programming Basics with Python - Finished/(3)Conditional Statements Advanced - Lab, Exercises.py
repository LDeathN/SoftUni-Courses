print("Lab Work!")


print("Prices in different places!")

sofia = str("Sofia")
varna = str("Varna")
plovdiv = str("Plovdiv")

coffee = str("coffee")
water = str("water")
beer = str("beer")
sweets = str("sweets")
peanuts = str("peanuts")

name_product = str(input(""))
name_city = str(input(""))
volume = float(input(""))

if name_product == coffee and name_city == sofia:
    money = 0.50 * volume
    print(money)
elif name_product == coffee and name_city == varna:
    money = 0.45 * volume
    print(money)
elif name_product == coffee and name_city == plovdiv:
    money = 0.40 * volume
    print(money)
elif name_product == water and name_city == sofia:
    money = 0.80 * volume
    print(money)
elif name_product == water and name_city == varna:
    money = 0.70 * volume
    print(money)
elif name_product == water and name_city == plovdiv:
    money = 0.70 * volume
    print(money)
elif name_product == beer and name_city == sofia:
    money = 1.20 * volume
    print(money)
elif name_product == beer and name_city == varna:
    money = 1.10 * volume
    print(money)
elif name_product == beer and name_city == plovdiv:
    money = 1.15 * volume
    print(money)
elif name_product == sweets and name_city == sofia:
    money = 1.45 * volume
    print(money)
elif name_product == sweets and name_city == varna:
    money = 1.35 * volume
    print(money)
elif name_product == sweets and name_city == plovdiv:
    money = 1.30 * volume
    print(money)
elif name_product == peanuts and name_city == sofia:
    money = 1.60 * volume
    print(money)
elif name_product == peanuts and name_city == varna:
    money = 1.55 * volume
    print(money)
elif name_product == peanuts and name_city == plovdiv:
    money = 1.50 * volume
    print(money)
else:
    print("Something went wrong!")






print("Day of the week! ... Working or nor as well!")


number = int(input(""))

if 1 <= number <= 7:
    if number == 1:
        print("Monday")
    elif number == 2:
        print("Tuesday")
    elif number == 3:
        print("Wednesday")
    elif number == 4:
        print("Thursday")
    elif number == 5:
        print("Friday")
    elif number == 6:
        print("Saturday")
    elif number == 7:
        print("Sunday")
else:
    print("Error")


day = str(input(""))

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    print("Working day")
elif day == "Saturday" or day == "Sunday":
    print("Weekend")
else:
    print("Error")





print("Type of animal!")

name = str(input(""))

if name == "dog":
    print("mammal")
elif name == "snake" or name == "tortoise" or name == "crocodile":
    print("reptile")
else:
    print("unknown")





print("Gender and age!")

age = float(input(""))
gender = str(input(""))

if gender == "f" and age < 16:
    print("Miss")
elif gender == "f" and age >= 16:
    print("Ms.")
elif gender == "m" and age < 16:
    print("Master")
elif gender == "m" and age >= 16:
    print("Mr.")






print("Tell if number is in")

number = int(input(""))
if -100 <= number <= 100 and number != 0:
     print("Yes")
else:
    print("No")






print("Open or Closed")

time = float(input(""))
day = str(input(""))

if 10 <= time <= 18 and day != "Sunday":
    print("open")
else:
    print("closed")






print("Tickets on day")

day_of_week = str(input(""))

if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Friday":
    print(12)
elif day_of_week == "Wednesday" or day_of_week == "Thursday":
    print(14)
elif day_of_week == "Saturday" or day_of_week == "Sunday":
    print(16)







print("Veg or Fruit")

veg_or_fruit = str(input(""))

if veg_or_fruit == "banana" or veg_or_fruit == "apple" or veg_or_fruit == "kiwi" or veg_or_fruit == "cherry" or veg_or_fruit == "lemon" or veg_or_fruit == "grapes":
    print("fruit")
elif veg_or_fruit == "tomato" or veg_or_fruit == "cucumber" or veg_or_fruit == "pepper" or veg_or_fruit == "carrot":
    print("vegetable")
else:
    print("unknown")







print("Valid or Invalid")

number = float(input(""))

if 100 <= number <= 200 or number == 0:
    print("")
else:
    print("invalid")






print("Something with shop")

fruit = str(input(""))
day = str(input(""))
volume = float(input(""))

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    if fruit == "banana":
        money = volume * 2.50
        print(f"{money:.2f}")
    elif fruit == "apple":
        money = volume * 1.20
        print(f"{money:.2f}")
    elif fruit == "orange":
        money = volume * 0.85
        print(f"{money:.2f}")
    elif fruit == "grapefruit":
        money = volume * 1.45
        print(f"{money:.2f}")
    elif fruit == "kiwi":
        money = volume * 2.70
        print(f"{money:.2f}")
    elif fruit == "pineapple":
        money = volume * 5.50
        print(f"{money:.2f}")
    elif fruit == "grapes":
        money = volume * 3.85
        print(f"{money:.2f}")
    else:
        print("error")
elif day == "Saturday" or day == "Sunday":
    if fruit == "banana":
        money = volume * 2.70
        print(f"{money:.2f}")
    elif fruit == "apple":
        money = volume * 1.25
        print(f"{money:.2f}")
    elif fruit == "orange":
        money = volume * 0.90
        print(f"{money:.2f}")
    elif fruit == "grapefruit":
        money = volume * 1.60
        print(f"{money:.2f}")
    elif fruit == "kiwi":
        money = volume * 3.00
        print(f"{money:.2f}")
    elif fruit == "pineapple":
        money = volume * 5.60
        print(f"{money:.2f}")
    elif fruit == "grapes":
        money = volume * 4.20
        print(f"{money:.2f}")
    else:
        print("error")
else:
    print("error")






print("Comission in different places ")

city = str(input(""))
volume = float(input(""))

if city == "Sofia":
    if 0 <= volume <= 500:
        commission = volume * 5 / 100
        print(f"{commission:.2f}")
    elif 500 < volume <= 1000:
        commission = volume * 7 / 100
        print(f"{commission:.2f}")
    elif 1000 < volume <= 10000:
        commission = volume * 8 / 100
        print(f"{commission:.2f}")
    elif volume > 10000:
        commission = volume * 12 / 100
        print(f"{commission:.2f}")
    else:
        print("error")
elif city == "Varna":
    if 0 <= volume <= 500:
        commission = volume * 4.5 / 100
        print(f"{commission:.2f}")
    elif 500 < volume <= 1000:
        commission = volume * 7.5 / 100
        print(f"{commission:.2f}")
    elif 1000 < volume <= 10000:
        commission = volume * 10 / 100
        print(f"{commission:.2f}")
    elif volume > 10000:
        commission = volume * 13 / 100
        print(f"{commission:.2f}")
    else:
        print("error")
elif city == "Plovdiv":
    if 0 <= volume <= 500:
        commission = volume * 5.5 / 100
        print(f"{commission:.2f}")
    elif 500 < volume <= 1000:
        commission = volume * 8 / 100
        print(f"{commission:.2f}")
    elif 1000 < volume <= 10000:
        commission = volume * 12 / 100
        print(f"{commission:.2f}")
    elif volume > 10000:
        commission = volume * 14.5 / 100
        print(f"{commission:.2f}")
    else:
        print("error")
else:
    print("error")





print("Exercise Work!")
print("1 Cinema let's go")

type = str(input(""))
rows = int(input(""))
columns = int(input(""))

if type == "Premiere":
    money = rows * columns * 12
    print(f"{money:.2f} leva")
elif type == "Normal":
    money = rows * columns * 7.50
    print(f"{money:.2f} leva")
elif type == "Discount":
    money = rows * columns * 5
    print(f"{money:.2f} leva")
else:
    print("Error")






print("2 What should I wear")

degrees = int(input())
time = str(input(""))
outfit = ""
shoes = ""

if time == "Morning" and 10 <= degrees <= 18:
    outfit = "Sweatshirt"
    shoes = "Sneakers"
elif time == "Morning" and 18 < degrees <= 24:
    outfit = "Shirt"
    shoes = "Moccasins"
elif time == "Morning" and degrees >= 25:
    outfit = "T-Shirt"
    shoes = "Sandals"
elif time == "Afternoon" and 10 <= degrees <= 18:
    outfit = "Shirt"
    shoes = "Moccasins"
elif time == "Afternoon" and 18 < degrees <= 24:
    outfit = "T-Shirt"
    shoes = "Sandals"
elif time == "Afternoon" and degrees >= 25:
    outfit = "Swim Suit"
    shoes = "Barefoot"
elif time == "Evening" and 10 <= degrees <= 18:
    outfit = "Shirt"
    shoes = "Moccasins"
elif time == "Evening" and 18 < degrees <= 24:
    outfit = "Shirt"
    shoes = "Moccasins"
elif time == "Evening" and degrees >= 25:
    outfit = "Shirt"
    shoes = "Moccasins"
print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")








print("3 Making a garden")

type_flower = str(input(""))
number_of_flower = int(input())
budget = float(input())
money_spend = 0
if type_flower == "Roses" and number_of_flower > 80:
    money_spend = number_of_flower * 5
    money_spend = money_spend - (money_spend * 10 / 100)
elif type_flower == "Roses" and number_of_flower <= 80:
    money_spend = number_of_flower * 5
elif type_flower == "Dahlias" and number_of_flower > 90:
    money_spend = number_of_flower * 3.80
    money_spend = money_spend - (money_spend * 15 / 100)
elif type_flower == "Dahlias" and number_of_flower <= 90:
    money_spend = number_of_flower * 3.80
elif type_flower == "Tulips" and number_of_flower > 80:
    money_spend = number_of_flower * 2.80
    money_spend = money_spend - (money_spend * 15 / 100)
elif type_flower == "Tulips" and number_of_flower <= 80:
    money_spend = number_of_flower * 2.80
elif type_flower == "Narcissus" and number_of_flower < 120:
    money_spend = number_of_flower * 3
    money_spend = money_spend - (money_spend * 15 / 100)
elif type_flower == "Narcissus" and number_of_flower >= 120:
    money_spend = number_of_flower * 3
elif type_flower == "Gladiolus" and number_of_flower < 80:
    money_spend = number_of_flower * 2.50
    money_spend = money_spend - (money_spend * 20 / 100)
elif type_flower == "Gladiolus" and number_of_flower >= 80:
    money_spend = number_of_flower * 2.50

if money_spend <= budget:
    money_left = budget - money_spend
    print(f"Hey, you have a great garden with {number_of_flower} {type_flower} and {money_left:.2f} leva left.")
elif money_spend > budget:
    money_needed = money_spend - budget
    print(f"Not enough money, you need {money_needed:.2f} leva more.")







print("4 Fishermen boat")

budget = int(input())
season = str(input())
number_of_fishermen = int(input())

if season == "Spring":
    cost = 3000
elif season == "Summer" or season == "Autumn":
    cost = 4200
elif season == "Winter":
    cost = 2600

if number_of_fishermen <= 6:
    cost = cost - (cost * 10 / 100)
elif 7 <= number_of_fishermen <= 11:
    cost = cost - (cost * 15 / 100)
elif number_of_fishermen >= 12:
    cost = cost - (cost * 25 / 100)

if number_of_fishermen % 2 == 0 and season != "Autumn":
    cost = cost - (cost * 5 / 100)

if cost <= budget:
    money_left = budget - cost
    print(f"Yes! You have {money_left:.2f} leva left.")
elif cost > budget:
    money_needed = cost - budget
    print(f"Not enough money! You need {money_needed:.2f} leva.")







print("5 Hotel or Camp is the question")

budget = float(input())
season = str(input())

if budget <= 100 and season == "summer":
    camp = budget * 30 / 100
    print("Somewhere in Bulgaria")
    print(f"Camp - {camp:.2f}")
elif budget <= 100 and season == "winter":
    hotel = budget * 70 / 100
    print("Somewhere in Bulgaria")
    print(f"Hotel - {hotel:.2f}")
elif budget <= 1000 and season == "summer":
    camp = budget * 40 / 100
    print("Somewhere in Balkans")
    print(f"Camp - {camp:.2f}")
elif budget <= 1000 and season == "winter":
    hotel = budget * 80 / 100
    print("Somewhere in Balkans")
    print(f"Hotel - {hotel:.2f}")
elif budget > 1000:
    if season == "summer":
        camp = budget * 90 / 100
        print("Somewhere in Europe")
        print(f"Hotel - {camp:.2f}")
    elif season == "winter":
        hotel = budget * 90 / 100
        print("Somewhere in Europe")
        print(f"Hotel - {hotel:.2f}")








print("6 Simple calculator boy!")

num1 = int(input())
num2 = int(input())
operator = str(input())

if operator == "+":
    result = num1 + num2
    if result % 2 == 0:
        print(f"{num1} + {num2} = {result} - even")
    else:
        print(f"{num1} + {num2} = {result} - odd")
elif operator == "-":
    result = num1 - num2
    if result % 2 == 0:
        print(f"{num1} - {num2} = {result} - even")
    else:
        print(f"{num1} - {num2} = {result} - odd")
elif operator == "*":
    result = num1 * num2
    if result % 2 == 0:
        print(f"{num1} * {num2} = {result} - even")
    else:
        print(f"{num1} * {num2} = {result} - odd")
elif operator == "/" and num2 == 0:
    print(f"Cannot divide {num1} by zero")
elif operator == "/" and num2 != 0:
    result = num1 / num2
    print(f"{num1} / {num2} = {result:.2F}")
elif operator == "%" and num2 == 0:
    print(f"Cannot divide {num1} by zero")
elif operator == "%" and num2 != 0:
    result = num1 % num2
    print(f"{num1} % {num2} = {result}")
else:
    print("Error")







print("7 Hotel rooms and money")

month = str(input())
nights = int(input())

if month == "May" or month == "October":
    studio = nights * 50
    apartment = nights * 65
elif month == "June" or month == "September":
    studio = nights * 75.20
    apartment = nights * 68.70
elif month == "July" or month == "August":
    studio = nights * 76
    apartment = nights * 77
else:
    print("Error")

if (month == "May" or month == "October") and 7 < nights <= 14:
    studio = studio - (studio * 5 / 100)
elif (month == "May" or month == "October") and nights > 14:
    studio = studio - (studio * 30 / 100)
elif (month == "June" or month == "September") and nights > 14:
    studio = studio - (studio * 20 / 100)


if nights > 14:
    apartment = apartment - (apartment * 10 / 100)

print(f"Apartment: {apartment:.2f} lv.")
print(f"Studio: {studio:.2f} lv.")







print("8 I admit this is the hardest so far")

import math
exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

if 0 <= exam_hour <= 23 and 0 <= exam_minutes <= 59 and 0 <= arrival_hour <= 23 and 0 <= arrival_minutes <= 59:
    exam_time = exam_hour * 60 + exam_minutes
    arrival_time = arrival_hour * 60 + arrival_minutes
    if arrival_time > exam_time:
        difference = arrival_time - exam_time
        print("Late")
        if difference < 60:
            print(f"{difference} minutes after the start")
        elif difference > 60:
            difference_hour = math.floor(difference / 60)
            difference_minutes = difference % 60
            if difference_minutes < 10:
                print(f"{difference_hour}:0{difference_minutes} hours after the start.")
            else:
                print(f"{difference_hour}:{difference_minutes} hours after the start.")
    elif arrival_time == exam_time:
        print("On time")
    elif arrival_time < exam_time:
        difference = exam_time - arrival_time
        if difference <= 30:
            print("On time")
            print(f"{difference} minutes before the start")
        elif difference > 30:
            print("Early")
            if difference < 60:
                print(f"{difference} minutes before the start")
            elif difference >= 60:
                difference_hour = math.floor(difference / 60)
                difference_minutes = difference % 60
                if difference_minutes < 10:
                    print(f"{difference_hour}:0{difference_minutes} hours before the start")
                else:
                    print(f"{difference_hour}:{difference_minutes} hours before the start")
else:
    print("Error")







print("9 This one was chill though")

days_staying = int(input())
room_type = str(input())
feedback = str(input())

night_staying = days_staying - 1

if room_type == "room for one person":
    money_spend = night_staying * 18
    final_cost = money_spend
elif room_type == "apartment":
    money_spend = night_staying * 25
    if days_staying < 10:
        final_cost = money_spend - (money_spend * 30 / 100)
    elif 10 <= days_staying <= 15:
        final_cost = money_spend - (money_spend * 35 / 100)
    elif days_staying > 15:
        final_cost = money_spend - (money_spend * 50 / 100)
elif room_type == "president apartment":
    money_spend = night_staying * 35
    if days_staying < 10:
        final_cost = money_spend - (money_spend * 10 / 100)
    elif 10 <= days_staying <= 15:
        final_cost = money_spend - (money_spend * 15 / 100)
    elif days_staying > 15:
        final_cost = money_spend - (money_spend * 20 / 100)
else:
    print("Error")

if feedback == "positive":
    final_cost = final_cost + (final_cost * 25 / 100)
elif feedback == "negative":
    final_cost = final_cost - (final_cost * 10 / 100)
else:
    print("Error")

print(f"{final_cost:.2f}")