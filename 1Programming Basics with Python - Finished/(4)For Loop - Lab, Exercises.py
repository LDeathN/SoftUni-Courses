print("Presentation Examples!")


print("First Example")
import sys
i = 1
max_num = -sys.maxsize
min_num = sys.maxsize
num = int(input("Enter a number: "))

for i in range(1, num + 1):
    num1 = int(input("Enter the sequence: "))
    if num1 > max_num:
        max_num = num1
    if num1 < min_num:
        min_num = num1

print(f"Max number: {max_num}")
print(f"Min number: {min_num}")



print("Second Examlpe")

num = int(input("Enter a number: "))
i = 1
left_sum = 0
right_sum = 0
for i in range(1, num + 1):
    num1 = int(input("Enter the sequence: "))
    left_sum += num1
for i in range(1, num + 1):
    num2 = int(input("Enter the second sequence: "))
    right_sum += num2

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    difference = abs(left_sum - right_sum)
    print(f"No, difference = {difference}")



print("Third Example")
num = int(input("Enter a number: "))
i = 1
even_sum = 0
odd_sum = 0
for i in range(1, num + 1):
    number = int(input("Enter a number: "))
    if i % 2 == 0:
        even_sum += number
    else:
        odd_sum += number

if odd_sum == even_sum:
    print(f"Yes, sum - {odd_sum}")
else:
    difference = abs(odd_sum - even_sum)
    print(f"No, difference = {difference}")





print("Lab Work!")


print("1 Done")
for i in range (1 , 101):
    print(i)


print("2 Done")
num = int(input())
for i in range(1, num + 1, 3):
    print(i)


print("3 Done")
num = int(input())
for i in range(0, num + 1, 2):
    result = pow(2, i,)
    print(result)


print("4 Done")
num = int(input())
for i in range(num, 0, -1):
    print(i)


print("5 Done")
word = str(input())
for letter in word:
    print(letter)
for letter in range(0, len(word)):
    print(word[letter])


print("6 Done")
word = str(input())
sum = 0
for letter in word:
    if letter == "A" or letter == "a":
        sum += 1
    elif letter == "E" or letter == "e":
        sum += 2
    elif letter == "I" or letter == "i":
        sum += 3
    elif letter == "O" or letter == "o":
        sum += 4
    elif letter == "U" or letter == "u":
        sum += 5
print(sum)


print("7 Done")
num = int(input())
total = 0
for i in range(1, num + 1):
    element = int(input())
    total += element
print(total)


print("8 Done")
import sys
i = 1
max_num = -sys.maxsize
min_num = sys.maxsize
num = int(input())

for i in range(1, num+1):
    num1 = int(input())
    if num1 > max_num:
        max_num = num1
    if num1 < min_num:
        min_num = num1

print(f"Max number: {max_num}")
print(f"Min number: {min_num}")


print("9 Done")
num = int(input())
i = 1
left_sum = 0
right_sum = 0
for i in range(1, num + 1):
    num1 = int(input())
    left_sum += num1
for i in range(1, num + 1):
    num2 = int(input())
    right_sum += num2

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    difference = abs(left_sum - right_sum)
    print(f"No, diff = {difference}")


print("10 Done... END LAB!")
num = int(input())
i = 1
even_sum = 0
odd_sum = 0
for i in range(1, num + 1):
    number = int(input())
    if i % 2 == 0:
        even_sum += number
    else:
        odd_sum += number

if odd_sum == even_sum:
    print(f"Yes")
else:
    difference = abs(odd_sum - even_sum)
    print(f"No")







print("Exercise Work!")


print("1 Done")
for i in range(1, 1001):
    if i % 10 == 7:
        print(i)




print("2 Done")
import sys
import math
max_num = -sys.maxsize
sum = 0
n = int(input())
for i in range(0, n):
    num = int(input())
    if num > max_num:
        max_num = num
    sum += num

if max_num == sum / 2:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    print("No")
    print(f"Diff = {math.ceil(abs(max_num - (sum - max_num)))}")




print("3 Done")
n = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(0, n):
    num = int(input())
    if num < 200:
        p1 += 1
    elif 200 <= num <= 399:
        p2 += 1
    elif 400 <= num <= 599:
        p3 += 1
    elif 600 <= num <= 799:
        p4 += 1
    elif 800 <= num <= 1000:
        p5 += 1
    else:
        print(f"{num} is invalid!")
        n = n -1

print(f"{p1 / n * 100:.2f}%")
print(f"{p2 / n * 100:.2f}%")
print(f"{p3 / n * 100:.2f}%")
print(f"{p4 / n * 100:.2f}%")
print(f"{p5 / n * 100:.2f}%")




print("4 Done")
age = int(input())
washing_machine = float(input())
money_per_toy = float(input())
money = 0
toys = 0
if age <= 77:
    for i in range(1, age + 1):
        if i % 2 == 0:
            money += (5 * i) - 1
        else:
            toys += 1
else:
    print(f"{age} is too high")

money_of_toys = toys * money_per_toy
total_money = money + money_of_toys

if total_money >= washing_machine:
    print(f"Yes! {total_money - washing_machine:.2f}")
else:
    print(f"No! {washing_machine - total_money:.2f}")




print("5 Done")
import math
tabs = int(input())
salary = float(input())
if 1 <= tabs <= 10 and 500 <= salary <= 1500:
    for i in range(1, tabs + 1):
        name = str(input())
        if name == "Facebook":
            salary = salary - 150
        elif name == "Instagram":
            salary = salary - 100
        elif name == "Reddit":
            salary = salary - 50
        else:
            salary = salary
        if salary <= 0:
            print("You have lost your salary.")
            break
else:
    print("Error")

if salary > 0:
    print(math.floor(salary))




print("6 Done")
name_of_actor = str(input())
academy_points = float(input())
number_of_judges = int(input())
total_points = academy_points

if 2 <= academy_points <= 450.5 and 1 <= number_of_judges <= 20:
    for i in range(1, number_of_judges + 1):
        name_of_judge = str(input())
        judge_points = float(input())
        points = int(len(name_of_judge)) * (judge_points / 2)
        total_points += points
        if total_points > 1250.5:
            print(f"Congratulations, {name_of_actor} got a nominee for leading role with {total_points:.1f}!")
            break
if total_points <= 1250.5:
    print(f"Sorry, {name_of_actor} you need {1250.5 - total_points:.1f} more!")




print("7 Done")
groups = int(input())
total_people = 0
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

if 1 <= groups <= 1000:
    for i in range(1, groups + 1):
        people = int(input())
        total_people += people
        if people <= 5:
            p1 += people
        elif 6 <= people <= 12:
            p2 += people
        elif 13 <= people <= 25:
            p3 += people
        elif 26 <= people <= 40:
            p4 += people
        elif people >= 41:
            p5 += people

print(f"{p1 / total_people * 100:.2f}%")
print(f"{p2 / total_people * 100:.2f}%")
print(f"{p3 / total_people * 100:.2f}%")
print(f"{p4 / total_people * 100:.2f}%")
print(f"{p5 / total_people * 100:.2f}%")




print("8 Done... FINISHED THIS ONE TOO!")
import math
tournaments = int(input())
starting_points = int(input())
final_points = starting_points
tournaments_won = 0

if 1 <= tournaments <= 20 and 1 <= starting_points <= 4000:
    for i in range(1, tournaments + 1):
        position = str(input())
        if position == "W":
            tournaments_won += 1
            final_points += 2000
        elif position == "F":
            final_points += 1200
        elif position == "SF":
            final_points += 720
        else:
            final_points = final_points
else:
    print("Error")

average_points = (final_points - starting_points) / tournaments
winning_percentage = tournaments_won / tournaments * 100

print(f"Final points: {final_points}")
print(f"Average points: {math.floor(average_points)}")
print(f"{winning_percentage:.2f}%")