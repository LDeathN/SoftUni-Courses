# First Problem

sequence = input().split(" ")
dictionary = {}
for number in sequence:
    if number not in dictionary:
        dictionary[number] = 1
    else:
        dictionary[number] += 1
for element in dictionary:
    print(f"{float(element):.1f} - {dictionary[element]} times")



# Second Problem

student_records = {}
n = int(input())
for _ in range(n):
    student_name, grade = input().split()
    grade = float(grade)
    if student_name in student_records:
        student_records[student_name].append(grade)
    else:
        student_records[student_name] = [grade]

for student_name, grades in student_records.items():
    rounded_grades = [f"{grade:.2f}" for grade in grades]
    average_grade = sum(grades) / len(grades)
    print(f"{student_name} -> {' '.join(rounded_grades)} (avg: {average_grade:.2f})")



# Third Problem

number = int(input())
names = []
for i in range(number):
    name = input()
    if name not in names:
        names.append(name)
for name in names:
    print(name)



# Fourth Problem

number = int(input())
cars = []
for i in range(number):
    car = input().split(", ")
    direction, id = car[0], car[1]
    if direction == "IN" and id not in cars:
        cars.append(id)
    if direction == "OUT" and id in cars:
        cars.remove(id)
if cars:
    for car in cars:
        print(car)
else:
    print("Parking Lot is Empty")



# Fifth Problem

Regular = []
VIP = []
number = int(input())
for i in range(number):
    code = input()
    if code[0].isdigit() and code not in VIP:
        VIP.append(code)
    elif not code[0].isdigit() and code not in Regular:
        Regular.append(code)
while True:
    guest = input()
    if guest == "END":
        break
    if guest in VIP:
        VIP.remove(guest)
    elif guest in Regular:
        Regular.remove(guest)
VIP = sorted(VIP)
Regular = sorted(Regular)
missing = len(VIP) + len(Regular)
print(missing)
while VIP:
    print(VIP.pop(0))
while Regular:
    print(Regular.pop(0))



# Sixth Problem (a) (Bonus)

numbers = list(map(int, input().split(" ")))
target = int(input())
for i in range(len(numbers)):
    if numbers[i] == "":
        continue
    for j in range(i + 1, len(numbers)):
        if numbers[j] == "":
            continue
        if numbers[i] + numbers[j] == target:
            print(f"{numbers[i]} + {numbers[j]} = {target}")
            numbers[i] = ""
            numbers[j] = ""
            break

# Sixth Problem (b) (Bonus)

numbers = list(map(int, input().split(" ")))
target = int(input())
targets = set()
values_map = {}
for value in numbers:
    if value in targets:
        targets.remove(value)
        pair = values_map[value]
        del values_map[value]
        print(f"{pair} + {value} = {target}")
        continue
    resulting_number = target - value
    targets.add(resulting_number)
    values_map[resulting_number] = value


