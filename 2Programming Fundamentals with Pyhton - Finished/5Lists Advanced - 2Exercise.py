# First Problem

searched = str(input()).split(", ")
given = str(input()).split(", ")
checked = []
result = list(searched)
for i in range(0, len(given)):
    current = given[i]
    checked += set(filter(lambda x: x in current, searched))
for j in searched:
    if j not in checked:
        result.remove(j)
print(result)



# Second Problem

version = str(input()).split(".")
first = int(version[0])
second = int(version[1])
third = int(version[2]) + 1
if third <= 9:
    print(f"{first}.{second}.{third}")
else:
    third = 0
    second += 1
    if second <= 9:
        print(f"{first}.{second}.{third}")
    else:
        second = 0
        first += 1
        print(f"{first}.{second}.{third}")



# Third Problem

words = input().split(" ")
even = list(filter(lambda x: len(x) % 2 == 0, words))
for i in even:
    print(i)



# Fourth Problem

sequence = input().split(", ")
count = 0
positive = []
negative = []
even = []
odd = []

positive += list(filter(lambda x: int(x) >= 0, sequence))
negative += list(filter(lambda x: int(x) < 0, sequence))
even += list(filter(lambda x: int(x) % 2 == 0, sequence))
odd += list(filter(lambda x: int(x) % 2 != 0, sequence))

print("Positive:", end=" ")
for i in range(len(positive)):
    count += 1
    if count == len(positive):
        print(f"{positive[i]}", end="")
    else:
        print(f"{positive[i]},", end=" ")
count = 0
print()
print("Negative:", end=" ")
for i in range(len(negative)):
    count += 1
    if count == len(negative):
        print(f"{negative[i]}", end="")
    else:
        print(f"{negative[i]},", end=" ")
count = 0
print()
print("Even:", end=" ")
for i in range(len(even)):
    count += 1
    if count == len(even):
        print(f"{even[i]}", end="")
    else:
        print(f"{even[i]},", end=" ")
count = 0
print()
print("Odd:", end=" ")
for i in range(len(odd)):
    count += 1
    if count == len(odd):
        print(f"{odd[i]}", end="")
    else:
        print(f"{odd[i]},", end=" ")



# Fifth Problem

rooms = int(input())
free = 0
needed = 0
flag = True
for i in range(1, rooms + 1):
    chairs_visitors = input().split(" ")
    if len(chairs_visitors[0]) >= int(chairs_visitors[1]):
        free += len(chairs_visitors[0]) - int(chairs_visitors[1])
    elif len(chairs_visitors[0]) < int(chairs_visitors[1]):
        needed = int(chairs_visitors[1]) - len(chairs_visitors[0])
        flag = False
        print(f"{needed} more chairs needed in room {i}")
if flag:
    print(f"Game On, {free} free chairs left")



# Sixth Problem

electrons = int(input())
shells = []
shell = 0
while electrons != 0:
    shell += 1
    if electrons >= 2 * (shell ** 2):
        electrons -= 2 * (shell ** 2)
        shells.append(2 * (shell ** 2))
    elif electrons < 2 * (shell ** 2):
        shells.append((electrons))
        electrons = 0

print(shells)



# Seventh Problem

numbers = list(map(int, input().split(", ")))
group = []
biggest = max(numbers)
for i in range(10, 10001, 10):
    if biggest > i - 10:
        for j in numbers:
            if int(j) in range(i - 9, i + 1):
                group.append(int(j))
        print(f"Group of {i}'s: {group}")
        group = []



# Eighth Problem

import re
code = input().split(" ")
letters = []
decipher = ""
for i in code:
    first = re.findall(r'[0-9]+', i)
    other = re.findall(r'[a-zA-Z]+', i)
    other = other[0]
    for j in other:
        letters.append(j)
    letters[0], letters[len(letters) - 1] = letters[len(letters) - 1], letters[0]
    decipher += chr(int(first[0]))
    for h in letters:
        decipher += h
    print(f"{decipher} ", end="")
    letters = []
    decipher = ""



# Ninth Problem(The Hardest One So Far!)

data = input().split()
while True:
    command = str(input())
    if command == "3:1":
        break
    command = command.split(" ")
    operation = command[0]
    index = int(command[1])
    range_divisor = int(command[2])
    if operation == "merge":
        if range_divisor >= len(data):
            if index >= 0:
                data[index: len(data)] = [''.join(data[index: len(data)])]
            else:
                data[0: len(data)] = [''.join(data[0: len(data)])]
        else:
            if index >= 0:
                data[index: range_divisor + 1] = [''.join(data[index: range_divisor + 1])]
            else:
                data[0: range_divisor + 1] = [''.join(data[0: range_divisor + 1])]
    if operation == "divide":
        if len(data[index]) % int(range_divisor) == 0:
            result = len(data[index]) // range_divisor
            text = data[index]
            text = [text[i:i + result] for i in range(0, len(text), result)]
            data.pop(index)
            for j in reversed(text):
                data.insert(index, j)

        elif len(data[index]) % range_divisor != 0:
            result = len(data[index]) // range_divisor
            remainder = len(data[index]) % range_divisor
            text = data[index]
            text1 = [text[i:i + result] for i in range(0, len(text) - remainder - result, result)]
            text2 = text[::-1]
            text2 = [text2[i:i + result + remainder] for i in range(1)]
            text2 = text2[0]
            text3 = text2[::-1]
            data.remove(data[index])
            data.insert(index, text3)
            for j in reversed(text1):
                data.insert(index, j)
for element in data:
    print(f"{element} ", end="")



# Tenth Problem

numbers = input().split()
sum = []
final = 0
while numbers != []:
    position = int(input())
    if position < 0:
        current = int(numbers[0])
        sum.append(current)
        numbers.pop(0)
        numbers.insert(0, numbers[len(numbers) - 1])
        for i in range(0, len(numbers)):
            if current >= int(numbers[i]):
                numbers[i] = int(numbers[i]) + current
            else:
                numbers[i] = int(numbers[i]) - current

    elif 0 <= position < len(numbers):
        current = int(numbers[position])
        sum.append(current)
        numbers.pop(position)
        for i in range(0, len(numbers)):
            if current >= int(numbers[i]):
                numbers[i] = int(numbers[i]) + current
            else:
                numbers[i] = int(numbers[i]) - current

    elif position >= len(numbers):
        current = int(numbers[len(numbers) - 1])
        sum.append(current)
        numbers.pop(len(numbers) - 1)
        numbers.insert(len(numbers), numbers[0])
        for i in range(0, len(numbers)):
            if current >= int(numbers[i]):
                numbers[i] = int(numbers[i]) + current
            else:
                numbers[i] = int(numbers[i]) - current
for i in sum:
    final += i
print(final)



# Eleventh Problem

schedule = input().split(", ")
exercise = []
while True:
    command = input()
    if command == "course start":
        break
    command = command.split(":")
    operation = command[0]

    if operation == "Add":
        lesson = command[1]
        if lesson not in schedule:
            schedule.append(lesson)

    elif operation == "Insert":
        lesson = command[1]
        index = int(command[2])
        if lesson not in schedule:
            schedule.insert(index, lesson)

    elif operation == "Remove":
        lesson = command[1]
        if lesson in schedule:
            if lesson + "-Exercise" in schedule:
                schedule.remove(schedule[schedule.index(lesson + "-Exercise")])
            schedule.remove(lesson)

    elif operation == "Swap":
        lesson1 = command[1]
        lesson2 = command[2]
        if lesson1 in schedule and lesson2 in schedule:
            index1 = schedule.index(lesson1)
            index2 = schedule.index(lesson2)
            schedule.pop(index1)
            schedule.insert(index1, lesson2)
            schedule.pop(index2)
            schedule.insert(index2, lesson1)
            if lesson1 + "-Exercise" in schedule:
                schedule.remove(schedule[schedule.index(lesson1 + "-Exercise")])
                schedule.insert(index2 + 1, lesson1 + "-Exercise")
            if lesson2 + "-Exercise" in schedule:
                schedule.remove(schedule[schedule.index(lesson2 + "-Exercise")])
                schedule.insert(index1 + 1, lesson2 + "-Exercise")

    elif operation == "Exercise":
        lesson = command[1]
        if lesson in schedule:
            if lesson + "-Exercise" not in schedule:
                schedule.insert(schedule.index(lesson) + 1, lesson + "-Exercise")
        elif lesson not in schedule:
            schedule.append(lesson)
            schedule.append((lesson + "-Exercise"))

for i in range(0, len(schedule)):
    print(f"{i + 1}.{schedule[i]}")