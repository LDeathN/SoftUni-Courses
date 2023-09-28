print("Lab Work!")


print("1 DONE")
for h in range(24):
    for m in range(60):
        if m >= 10:
            print(f"{h}:{m}")
        elif m < 10:
            print(f"{h}:{m}")



print("2 DONE")
for num1 in range(1, 11):
    for num2 in range(1, 11):
        print(f"{num1} * {num2} = {num1 * num2}")



print("3 DONE")
n = int(input())
sum = 0
for i in range(n + 1):
    for j in range(n + 1):
        for k in range(n + 1):
            result = i + j + k
            if result == n:
                sum += 1
print(sum)



print("4 DONE")
found = False
count = 0
num1 = int(input())
num2 = int(input())
magic_number = int(input())
for i in range(num1, num2 + 1):
    for j in range(num1, num2 + 1):
        result = i + j
        count += 1
        if result == magic_number:
            print(f"Combination N:{count} ({i} + {j} = {magic_number})")
            found = True
            break
    if found:
        break
if not found:
    print(f"{count} combinations - neither equals {magic_number}")



print("5 DONE")
destination = str(input())
minimum = float(input())
saving = 0
condition = True
while condition:
    money = float(input())
    saving += money
    if saving >= minimum:
        print(f"Going to {destination}!")
        saving = 0
        destination = str(input())
        if destination == "End":
            condition = False
            continue
        minimum = float(input())



print("6 DONE")
floors = int(input())
rooms = int(input())

for i in range(floors, 0, -1):
    for j in range(0, rooms):
        if i == floors:
            print(f"L{i}{j}", end=" ")
        if i != floors and i % 2 == 0:
            print(f"O{i}{j}", end=" ")
        if i != floors and i % 2 != 0:
            print(f"A{i}{j}", end=" ")
    print("")





print("Exercise Work!")


print("1 DONE")
n = int(input())
current = 1
condition = False
for row in range(1, n + 1):
    for column in range(1, row + 1):

        if current > n:
            condition = True
            break
        print(str(current) + " ", end="")
        current += 1
    if condition:
        break
    print()



print("2 DONE")
num1 = int(input())
num2 = int(input())
for i in range(num1, num2 + 1):
    num = str(i)
    sum_even = 0
    sum_odd = 0

    for j, digit in enumerate(num):
        if j % 2 == 0:
            sum_even += int(digit)
        else:
            sum_odd += int(digit)

    if sum_even == sum_odd:
        print((i), end=" ")



print("3 DONE")
import sys
condition = True
prime_sum = 0
non_prime_sum = 0

while condition:
    start = input()
    if start == "stop":
        condition = False
        continue
    number = int(start)
    if number < 0:
        print("Number is negative.")
        continue
    for j in range(2, sys.maxsize, 1):
        if number % j == 0:
            number = number / j
            if number == 1 or number == 0:
                prime_sum += number * j
                break
            else:
                non_prime_sum += number * j
                break

if not condition:
    print(f"Sum of all prime numbers is: {prime_sum}")
    print(f"Sum of all non prime numbers is: {non_prime_sum}")



print("4 DONE")
people = int(input())
name = str(input())
count = 0
current = 0
total = 0
while name != "Finish":
    for i in range(1, people + 1):
        grade = float(input())
        current += grade
    print(f"{name} - {current / people:.2f}. ")
    total += current / people
    count += 1
    current = 0
    name = str(input())

average = total / count
print(f"Student's final assessment is {average:.2f}.")



print("5 DONE")
N = int(input())
count = 0
special = False
for i in range(1111, 10000):
    number = str(i)
    for index, digit in enumerate(number):
        digit = int(digit)
        if digit == 0:
            continue
        if N % digit == 0:
            count += 1
            if count == 4:
                special = True
    if special:
        print(i)
    count = 0
    special = False



print("6 DONE")
film = str(input())
total = 0
student = 0
standard = 0
kid = 0
type = ""
while film != "Finish":
    spaces = int(input())
    free = 0
    while free <= spaces and type != "End":
        type = str(input())
        if type == "student":
            student += 1
        elif type == "standard":
            standard += 1
        elif type == "kid":
            kid += 1
        else:
            continue
        free += 1
        total += 1
        if free == spaces:
            type = "End"
            continue
    type = "Nothing"
    full = free / spaces * 100
    print(f"{film} - {full:.2f}% full.")
    film = str(input())

print(f"Total tickets: {total}")
print(f"{student / total * 100:.2f}% student tickets.")
print(f"{standard / total * 100:.2f}% standard tickets.")
print(f"{kid / total * 100:.2f}% kids tickets.")