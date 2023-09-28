print("Lab Work!")


print("1 DONE")
while True:
    word = str(input())
    if word == "Stop":
        break
    print(word)



print("2 DONE")
nickname = str(input())
set_password = str(input())
sign_in_password = str(input())

while sign_in_password != set_password:
    sign_in_password = str(input())

if set_password == sign_in_password:
    print(f"Welcome {nickname}!")



print("3 DONE")
goal = int(input())
sum = 0

while sum < goal:
    num = int(input())
    sum += num

print(sum)



print("4 DONE")
goal = int(input())
num = 0
while goal >= num:
    num = (num * 2) + 1
    if num > goal:
        break
    print(num)



print("5 DONE")
money = input()
balance = 0.0

while money != "NoMoreMoney":
    if float(money) >= 0:
        balance += float(money)
        print(f"Increase: {float(money):.2f}")
        money = input()
    elif float(money) < 0:
        print("Invalid operation!")
        break
print(f"Total: {balance:.2f}")

print("Uni Method")
money = input()
while money != "NoMoreMoney":
    amount = float(money)
    if amount < 0:
        print("Invalid operation!")
        break
    balance += amount
    print(f"Increase: {amount:.2f}")
    money = input()
print(f"Total: {balance:.2f}")



print("6,7 DONE")
import sys

num = input()
max_num = -sys.maxsize
min_num = sys.maxsize
while num != "Stop":
    if num > str(max_num):
        max_num = num
    if num < str(min_num):
        min_num = num
    num = input()

print("Max: " + max_num)
print("Min: " + min_num)

print("Uni method")
num = input()
max = -sys.maxsize
min = sys.maxsize
while num != "Stop":
    num1 = int(num)

    if num1 > max:
        max = num1
    if num1 < min:
        min = num1
    num = input()

print(f"{max}")
print(f"{min}")



print("8 DONE")
name = str(input())
sum_grades = 0
failed = 0
grades = 1
flag = True
while grades <= 12 and flag:
    grade = float(input())
    sum_grades += grade
    if grade < 4.00:
        failed += 1
        if failed > 1:
            print(f"{name} has been excluded at {int(grades - 1)} grade")
            flag = False
            continue
    grades += 1

if failed <= 1:
    average_grade = sum_grades / 12
    print(f"{name} graduated. Average grade: {average_grade:.2f}")





print("Exercise Work! ")


print("1 DONE")
name = str(input())
amount = int(input())
book = str(input())
number = 0
while name != book:
    number += 1
    if number == amount:
        print("No More Books")
        break
    book = str(input())

if name == book:
    print(f"You checked {number} books and found it.")
else:
    print("The book you searched is not here!")
    print(f"You checked {number} books.")

print("How softuni wants it: ")
name = str(input())
book = str(input())
number = 0
while book != "No More Books":
    if name == book:
        print(f"You checked {number} books and found it.")
        break

    number += 1
    book = str(input())

if book == "No More Books":
    print("The book you searched is not here!")
    print(f"You checked {number} books.")



print("2 DONE")
poor_grades = int(input())
condition = True
problems = 0
poor = 0
sum = 0
while condition:
    name = str(input())
    if name == "Enough":
        condition = False
        continue
    else:
        last_name = name
    grade = int(input())
    if grade > 4:
        problems += 1
        sum += grade
    elif grade <= 4:
        poor += 1
        problems += 1
        sum += grade
    if poor_grades == poor:
        print(f"You need a break, {poor} poor grades. ")
        break

if condition == False:
    average = sum / problems
    print(f"Average score: {average:.2f}")
    print(f"Number of problems: {problems}")
    print(f"Last problem: {last_name}")



print("3 DONE")
need = float(input())
money = float(input())
days = 0
count = 0
while money < need:
    decision = str(input())
    sum = float(input())
    if decision == "spend":
        money -= sum
        if money < 0:
            money = 0
        days += 1
        count += 1
    elif decision == "save":
        money += sum
        days += 1
        count = 0
    if count == 5:
        print("You can't save the money.")
        print(days)
        break
if not count == 5:
    print(f"You saved the money for {days} days.")



print("4 DONE")
steps = 0
step_to_home = 0
goal = False
while steps < 10000:
    current = input()
    if current == "Going home":
        step_to_home = int(input())
        if steps + step_to_home >= 10000:
            goal = True
        break
    steps += int(current)
    if steps >= 10000:
        goal = True
if goal:
    diff = steps + step_to_home - 10000
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    diff = abs(steps + step_to_home - 10000)
    print(f"{diff} more steps to reach goal.")



print("5 DONE")
change = float(input())
coins = 0
rest = 0
# Coins: 2 BGB, 1 BGN, 0.5 BGN, 0.2 BGN, 0.1 BGN, 0.05 BGN, 0.02 BGN, 0.01 BGN
rest = change // 2
if rest > 0:
    coins += rest
    change -= rest * 2
    change = round(change, 2)
rest = change // 1
if rest > 0:
    coins += rest
    change -= rest
    change = round(change, 2)
rest = change // 0.5
if rest > 0:
    coins += rest
    change -= rest * 0.5
    change = round(change, 2)
rest = change // 0.2
if rest > 0:
    coins += rest
    change -= rest * 0.2
    change = round(change, 2)
rest = change // 0.1
if rest > 0:
    coins += rest
    change -= rest * 0.1
    change = round(change, 2)
rest = change // 0.05
if rest > 0:
    coins += rest
    change -= rest * 0.05
    change = round(change, 2)
rest = change // 0.02
if rest > 0:
    coins += rest
    change -= rest * 0.02
    change = round(change, 2)
rest = change // 0.01
if rest > 0:
    coins += rest
    change -= rest * 0.01
    change = round(change, 2)

print(int(coins))



print("6 DONE")
width = int(input())
lenght = int(input())
pieces = width * lenght
pieces_left = pieces
total = 0
while pieces_left >= 0:
    number = input()
    if number == "STOP":
        print(f"{pieces_left} pieces are left.")
        break
    pieces_taken = int(number)
    pieces_left -= pieces_taken
    total += pieces_taken
if pieces_left < 0:
    pieces_needed = total - pieces
    print(f"No more cake left! You need {pieces_needed} pieces more.")



print("7 DONE... FINISHED THIS ONE AS WELL")
width = int(input())
length = int(input())
height = int(input())
space = width * length * height
space_left = space
total = 0

while space_left >= 0:
    box = input()
    if box == "Done":
        print(f"{space_left} Cubic meters left.")
        break
    boxes = int(box)
    space_left -= boxes
    total += boxes

if space_left < 0:
    space_needed = total - space
    print(f"No more free space! You need {space_needed} Cubic meters more.")