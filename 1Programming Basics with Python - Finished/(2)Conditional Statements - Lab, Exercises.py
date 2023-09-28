print("Exercise Work!")


print("1 Time + 15 Minutes Calculator")

hours = int(input())
minutes = int(input())

if 0 <= hours <= 23:
    if 0 <= minutes <= 59:
        minutes = minutes + 15
        if minutes >= 60:
            hours = hours + 1
            minutes = minutes - 60
            if hours > 23:
                hours = 0
    else:
        print("Wrong minute input!")
else:
    print("Wrong hour input!")

if minutes < 10:
    print(f"{hours}:0{minutes}")
else:
    print(f"{hours}:{minutes}")






print("2 Shop order!")

money_needed = float(input())
puzzles = int(input())
dolls = int(input())
teddy_bear = int(input())
minions = int(input())
trucks = int(input())

total_money = puzzles * 2.60 + dolls * 3 + teddy_bear * 4.10 + minions * 8.20 + trucks * 2
total_number = puzzles + dolls + teddy_bear + minions + trucks

if total_number >= 50:
   total_money = total_money - (total_money / 4)
else:
    total_money = total_money

final_money = total_money - (total_money * 0.1)

if final_money >= money_needed:
    money_left = round(final_money - money_needed, 2)
    print(f"Yes! {money_left:.2f} lv left.")
else:
    money_low = round(abs(money_needed - final_money), 2)
    print(f"Not enough money! {money_low:.2f} lv needed.")




print("3 King Kong Film!")

money_available = float(input())
number_of_people = int(input())
price_for_costume = float(input())
decoration = money_available * 0.1
total_for_costume = number_of_people * price_for_costume

if number_of_people > 150:
    total_for_costume = total_for_costume - (total_for_costume * 0.1)

money_needed = total_for_costume + decoration

if money_available >= money_needed:
    print("Action!")
    money_left = round(money_available - money_needed, 2)
    print(f"Wingard starts filming with {money_left:.2f} leva left.")
else:
    print("Not enough money!")
    money_low = round(abs(money_needed - money_available), 2)
    print(f"Wingard needs {money_low:.2f} leva more.")





print("4 New World Record!")

current_record = float(input())
distance = float(input())
time_speed = float(input())

resistance_time = (distance // 15) * 12.5
total_time = ((distance * time_speed) + resistance_time)

if current_record <= total_time:
    time_slower = (total_time - current_record)
    print(f"No, he failed! He was {time_slower:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")



print("5 No Chance Petar has so much money!")

money_available = float(input())
video_cards = int(input())
processors = int(input())
ram = int(input())

money_for_video_cards = (video_cards * 250)
money_for_processors = (((money_for_video_cards * 35) / 100) * processors)
money_for_ram = (((money_for_video_cards * 10) / 100) * ram)
total_money = money_for_video_cards + money_for_processors + money_for_ram

if video_cards > processors:
    total_money = total_money - (total_money * 15 / 100)

if total_money <= money_available:
    money_left = money_available - total_money
    print(f"You have {money_left:.2f} leva left!")
else:
    money_low = total_money - money_available
    print(f"Not enough money! You need {money_low:.2f} leva more!")





print("6 Lunch Break Time Boyy!")

from math import ceil
name = str(input())
length = int(input())
lunch_break = int(input())

time_for_lunch = lunch_break / 8
time_for_chill = lunch_break / 4

time_needed = length + time_for_lunch + time_for_chill

if time_needed <= lunch_break:
    time_left = lunch_break - time_needed
    print(f"You have enough time to watch {name} and left with {round(time_left)} minutes free time.")
else:
    time_short = time_needed - lunch_break
    print(f"You don't have enough time to watch {name}, you need {ceil(time_short)} more minutes.")