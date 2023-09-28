# First Bonus Problem

treasure = float(input())
years = int(input())
age = 17
spend = 0
for i in range(1800, years + 1):
    age += 1
    if i % 2 == 0:
        spend += 12000
    elif i % 2 != 0:
        spend += 12000 + 50 * age
if spend <= treasure:
    left = treasure - spend
    print(f"Yes! He will live a carefree life and will have {left:.2f} dollars left.")
elif spend > treasure:
    more = spend - treasure
    print(f"He will need {more:.2f} dollars to survive.")



# Second Bonus Problem

count = 0
untreated = 0
treated = 0
untreated1 = 0
treated1 = 0
period = int(input())
doctors = 7
for i in range(1, period + 1):
    count += 1
    if count % 3 == 0:
        if untreated1 > treated1:
            doctors += 1
    patients = int(input())
    untreated = patients - doctors
    if untreated < 0:
        treated = patients
        treated1 += treated
        continue
    treated = patients - untreated
    untreated1 += untreated
    treated1 += treated

print(f"Treated patients: {treated1}.")
print(f"Untreated patients: {untreated1}.")



# Third Bonus Problem

money1 = 0
money2 = 0
money3 = 0
weight1 = 0
weight2 = 0
weight3 = 0
total_weight = 0
number = int(input())
for i in range(1, number + 1):
    weight = int(input())
    if weight <= 3:
        type = "Bus"
        money1 += 200 * weight
        weight1 += weight
    elif 4 <= weight <= 11:
        type = "Truck"
        money2 += 175 * weight
        weight2 += weight
    elif weight >= 12:
        type = "Train"
        money3 += 120 * weight
        weight3 += weight
total_weight += weight1 + weight2 + weight3
money = money1 + money2 + money3
average_money = money / total_weight
average1 = weight1 / total_weight * 100
average2 = weight2 / total_weight * 100
average3 = weight3 / total_weight * 100
print(f"{average_money:.2f}")
print(f"{average1:.2f}%")
print(f"{average2:.2f}%")
print(f"{average3:.2f}%")



# Fourth Bonus Problem

poor = 0
average = 0
good = 0
excellent = 0
total_grade = 0
students = int(input())

for i in range(1, students + 1):
    grade = float(input())
    if 2.00 <= grade <= 2.99:
        poor += 1
        total_grade += grade
    elif 3.00 <= grade <= 3.99:
        average += 1
        total_grade += grade
    elif 4.00 <= grade <= 4.99:
        good += 1
        total_grade += grade
    elif 5.00 <= grade:
        excellent += 1
        total_grade += grade

percentage_excellent = excellent / students * 100
percentage_good = good / students * 100
percentage_average = average / students * 100
percentage_poor = poor / students * 100
average = total_grade / students

print(f"Top students: {percentage_excellent:.2f}%")
print(f"Between 4.00 and 4.99: {percentage_good:.2f}%")
print(f"Between 3.00 and 3.99: {percentage_average:.2f}%")
print(f"Fail: {percentage_poor:.2f}%")
print(f"Average: {average:.2f}")



# FifthBonus Problem

sum = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
number = int(input())

for i in range(1 , number + 1):
    new = int(input())
    if 0 <= new <= 9:
        sum += new * 0.20
        count1 += 1
    elif 10 <= new <= 19:
        sum += new * 0.30
        count2 += 1
    elif 20 <= new <= 29:
        sum += new * 0.40
        count3 += 1
    elif 30 <= new <= 39:
        sum += 50
        count4 += 1
    elif 40 <= new <= 50:
        sum += 100
        count5 += 1
    elif new < 0 or new > 50:
        sum = sum / 2
        count6 += 1

percentage1 = count1 / number * 100
percentage2 = count2 / number * 100
percentage3 = count3 / number * 100
percentage4 = count4 / number * 100
percentage5 = count5 / number * 100
percentage6 = count6 / number * 100

print(f"{sum:.2f}")
print(f"From 0 to 9: {percentage1:.2f}% ")
print(f"From 10 to 19: {percentage2:.2f}% ")
print(f"From 20 to 29: {percentage3:.2f}% ")
print(f"From 30 to 39: {percentage4:.2f}% ")
print(f"From 40 to 50: {percentage5:.2f}% ")
print(f"Invalid numbers: {percentage6:.2f}% ")



# Sixth Bonus Problem

electricity = 0
water = 0
internet = 0
other = 0
month = int(input())

for i in range(1, month + 1):
    bill = float(input())
    electricity += bill
    water += 20
    internet += 15
    other += (bill + 20 + 15) + ((bill + 20 + 15) * 0.20)

average = (other + internet + water + electricity) / month
print(f"Electricity: {electricity:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {other:.2f} lv")
print(f"Average: {average:.2f} lv")



# Seventh Bonus Problem

sector1 = 0
sector2 = 0
sector3 = 0
sector4 = 0

capacity = int(input())
fans = int(input())
for i in range(1 , fans + 1):
    sector = str(input())
    if sector == "A":
        sector1 += 1
    elif sector == "B":
        sector2 += 1
    elif sector == "V":
        sector3 += 1
    elif sector == "G":
        sector4 += 1

percentage1 = sector1 / fans * 100
percentage2 = sector2 / fans * 100
percentage3 = sector3 / fans * 100
percentage4 = sector4 / fans * 100
percentage5 = fans / capacity * 100

print(f"{percentage1:.2f}%")
print(f"{percentage2:.2f}%")
print(f"{percentage3:.2f}%")
print(f"{percentage4:.2f}%")
print(f"{percentage5:.2f}%")



# Eighth Bonus Problem

count = 0
sum1 = 0
sum2 = 0
biggest = 0
number = int(input())

for i in range(1, number + 1):
    count += 1
    num1 = int(input())
    num2 = int(input())

    if count % 2 != 0:
        sum1 = num1 + num2
    elif count % 2 == 0:
        sum2 = num1 + num2

    if count >= 2:
        difference = abs(sum1 - sum2)
        if biggest < difference:
            biggest = difference


if biggest == 0:
    print(f"Yes, value={sum1}")
else:
    print(f"No, maxdiff={biggest}")



# Ninth Bonus Problem

for h in range (0, 24):
    for m in range(0, 60):
        print(f"{h} : {m}")



# Tenth Bonus Problem

for h in range (0, 24):
    for m in range(0, 60):
        for s in range(0, 60):
            print(f"{h} : {m} : {s}")



# Eleventh Bonus Problem

oddmax = -1000
oddmin = 1000
evenmax = -1000
evenmin = 1000
count = 0
oddsum = 0
evensum = 0
number = int(input())

for i in range(1, number + 1):
    count += 1
    num = float(input())
    if count % 2 != 0:
        oddsum += num
        if oddmax < num:
            oddmax = num
        if oddmin > num:
            oddmin = num
    elif count % 2 == 0:
        evensum += num
        if evenmax < num:
            evenmax = num
        if evenmin > num:
            evenmin = num

print(f"OddSum={oddsum:.2f},")
if oddmin == 1000:
    print(f"OddMin=No,")
else:
    print(f"OddMin={oddmin:.2f},")
if oddmax == -1000:
    print(f"OddMax=No,")
else:
    print(f"OddMax={oddmax:.2f},")

print(f"EvenSum={evensum:.2f},")
if evenmin == 1000:
    print(f"EvenMin=No,")
else:
    print(f"EvenMin={evenmin:.2f},")
if evenmax == -1000:
    print(f"EvenMax=No")
else:
    print(f"EvenMax={evenmax:.2f}")