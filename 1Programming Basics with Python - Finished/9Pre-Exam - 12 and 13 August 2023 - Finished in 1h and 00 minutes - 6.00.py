# First Problem

people = int(input())
nights = int(input())
cards = int(input())
tickets = int(input())
money = people * (nights * 20 + cards * 1.60 + tickets * 6)
total = money * 1.25
print(f"{total:.2f}")



# Second Problem

money_per_day = float(input())
profit_per_day = float(input())
total_wasted_money = float(input())
price_for_present = float(input())
total = 5 * (money_per_day + profit_per_day) - total_wasted_money
if total >= price_for_present:
    print(f"Profit: {total:.2f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {(price_for_present - total):.2f} BGN.")



# Third Problem

weight = float(input())
delivery = input()
length = int(input())
if delivery == "standard":
    if weight < 1:
        money = length * 0.03
    elif 1 <= weight < 10:
        money = length * 0.05
    elif 10 <= weight < 40:
        money = length * 0.10
    elif 40 <= weight < 90:
        money = length * 0.15
    elif 90 <= weight <= 150:
        money = length * 0.20
elif delivery == "express":
    if weight < 1:
        money = length * 0.03
        money += length * (weight * 0.03 * 0.80)
    elif 1 <= weight < 10:
        money = length * 0.05
        money += length * (weight * 0.05 * 0.40)
    elif 10 <= weight < 40:
        money = length * 0.10
        money += length * (weight * 0.10 * 0.05)
    elif 40 <= weight < 90:
        money = length * 0.15
        money += length * (weight * 0.15 * 0.02)
    elif 90 <= weight <= 150:
        money = length * 0.20
        money += length * (weight * 0.20 * 0.01)
print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {money:.2f} lv.")



# Fourth Problem

total = 0
count = 0
failed = 0
average = 0
good = 0
top = 0
students = int(input())
for i in range(students):
    grade = float(input())
    if 2.00 <= grade <= 2.99:
        failed += 1
        total += grade
        count += 1
    elif 3.00 <= grade <= 3.99:
        average += 1
        total += grade
        count += 1
    elif 4.00 <= grade <= 4.99:
        good += 1
        total += grade
        count += 1
    elif 5.00 <= grade:
        top += 1
        total += grade
        count += 1
print(f"Top students: {(top / count) * 100:.2f}%")
print(f"Between 4.00 and 4.99: {(good / count) * 100:.2f}%")
print(f"Between 3.00 and 3.99: {(average / count) * 100:.2f}%")
print(f"Fail: {(failed / count) * 100:.2f}%")
average_grade = total / count
print(f"Average: {average_grade:.2f}")



# Fifth Problem

flag = True
best = 0
best_player = ""
while True and flag:
    name = input()
    if name == "END":
        break
    goals = int(input())
    if goals > best:
        best = goals
        best_player = name
        if goals >= 10:
            flag = False
            continue
print(f"{best_player} is the best player!")
if best >= 3:
    print(f"He has scored {best} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best} goals.")



# Sixth Problem

valid = 0
flag = False
K = int(input())
L = int(input())
M = int(input())
N = int(input())
for k in range(K, 9):
    if flag:
        break
    for l in range(9, L - 1, -1):
        if flag:
            break
        for m in range(M, 9):
            if flag:
                break
            for n in range(9, N - 1, -1):
                if flag:
                    break
                if k % 2 == 0 and m % 2 == 0 and l % 2 != 0 and n % 2 != 0:
                    if k != m or l != n:
                        valid += 1
                        print(f"{k}{l} - {m}{n}")
                        if valid == 6:
                            flag = True
                            break
                    elif k == m and l == n:
                        print(f"Cannot change the same player.")