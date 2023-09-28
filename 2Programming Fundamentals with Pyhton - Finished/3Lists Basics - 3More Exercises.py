# First Problem

list = input().split(", ")
digits = []
for i in range(0, len(list)):
    digits.append(int(list[i]))
for i in digits:
    if i == 0:
        digits.remove(i)
        digits.append(i)
print(digits)



# Second Problem

numbers = input().split(" ")
string = input()
sentence = []
for i in string:
    sentence.append(i)
message = ""
for i in numbers:
    number = 0
    for j in i:
        number += int(j)
    if number >= len(sentence):
        number = number % len(sentence)
        message += sentence[number]
        sentence.remove(sentence[number])
    else:
        message += sentence[number]
        sentence.remove(sentence[number])
print(message)



# Third Problem

race = input().split(" ")
player1 = 0
player2 = 0
for i in range(0, len(race) // 2):
    lap = int(race[i])
    if lap != 0:
        player1 += lap
    elif lap == 0:
        player1 = player1 * 0.80

for j in range(len(race) - 1, (len(race) // 2), -1):
    lap2 = int(race[j])
    if lap2 != 0:
        player2 += lap2
    elif lap2 == 0:
        player2 = player2 * 0.80

if player1 < player2:
    print(f"The winner is left with total time: {player1:.1f}")
elif player2 < player1:
    print(f"The winner is right with total time: {player2:.1f}")



# Fourth Problem

people = input().split(" ")
space = int(input())
numbers = []
result = []
count = 0
for i in people:
    numbers.append(int(i))
list = [" "] * len(numbers)
while numbers != list:
    for element in range(0, len(numbers)):
        if numbers[element] != " ":
            count += 1
        if count == space:
            count = 0
            result.append(numbers[element])
            numbers.pop(element)
            numbers.insert(element, " ")
print("[" + ",".join(str(item) for item in result) + "]")



# Fifth Problem

line1 = input().split(" ")
line2 = input().split(" ")
line3 = input().split(" ")
digits1 = []
digits2 = []
digits3 = []
for element in line1:
    digits1.append(int(element))
for element in line2:
    digits2.append(int(element))
for element in line3:
    digits3.append(int(element))
winner1 = False
winner2 = False

for i in range(1, 3):
    count = 0
    for j in digits1:
        if j == i:
            count += 1
            if count == 3 and i == 1:
                winner1 = True
            elif count == 3 and i == 2:
                winner2 = True
    count = 0
    for j in digits2:
        if j == i:
            count += 1
            if count == 3 and i == 1:
                winner1 = True
            elif count == 3 and i == 2:
                winner2 = True
    count = 0
    for j in digits3:
        if j == i:
            count += 1
            if count == 3 and i == 1:
                winner1 = True
            elif count == 3 and i == 2:
                winner2 = True

if (digits1[0] == 1 and digits2[1] == 1 and digits3[2] == 1) or (digits1[2] == 1 and digits2[1] == 1 and digits3[0] == 1):
        winner1 = True
if (digits1[0] == 2 and digits2[1] == 2 and digits3[2] == 2) or (digits1[2] == 2 and digits2[1] == 2 and digits3[0] == 2):
        winner2 = True

for j in range(1, 3):
    for i in range(0, 3):
        if digits1[i] == j and digits2[i] == j and digits3[i] == j:
            if j == 1:
                winner1 = True
            elif j == 2:
                winner2 = True

if winner1:
    print(f"First player won")
elif winner2:
    print(f"Second player won")
else:
    print(f"Draw!")



# Sixth Problem

numbers = input().split(" ")
digits = []
for element in numbers:
    digits.append(int(element))

while True:
    command = input()
    if command == "end":
        break
    command = command.split(" ")

    if command[0] == "exchange":
        index = int(command[1])
        if index < len(digits) and index >= 0:
            for i in range(0, index + 1):
                temp = digits[0]
                digits.remove(digits[0])
                digits.append(temp)
        else:
            print("Invalid index")

    elif command[0] == "max":
        if command[1] == "odd":
            maximum = -1
            for i in range(len(digits) - 1, -1, -1):
                if digits[i] > maximum and digits[i] % 2 != 0:
                    maximum = digits[i]
                    odd = i
            if maximum != -1:
                print(odd)
            else:
                print("No matches")
        elif command[1] == "even":
            maximum = -1
            for i in range(len(digits) - 1, -1, -1):
                if digits[i] > maximum and digits[i] % 2 == 0:
                    maximum = digits[i]
                    even = i
            if maximum != -1:
                print(even)
            else:
                print("No matches")

    elif command[0] == "min":
        if command[1] == "odd":
            minimum = 1001
            for i in range(len(digits) - 1, -1, -1):
                if digits[i] < minimum and digits[i] % 2 != 0:
                    minimum = digits[i]
                    odd = i
            if minimum != 1001:
                print(odd)
            else:
                print("No matches")
        elif command[1] == "even":
            minimum = 1001
            for i in range(len(digits) - 1, -1, -1):
                if digits[i] < minimum and digits[i] % 2 == 0:
                    minimum = digits[i]
                    even = i
            if minimum != 1001:
                print(even)
            else:
                print("No matches")

    elif command[0] == "first":
        first = []
        amount = int(command[1])
        count = 0
        if amount <= len(digits):
            if command[2] == "even":
                for i in digits:
                    if i % 2 == 0 and count < amount:
                        first.append(i)
                        count += 1
                print(first)
            elif command[2] == "odd":
                for i in digits:
                    if i % 2 != 0 and count < amount:
                        first.append(i)
                        count += 1
                print(first)
        else:
            print("Invalid count")

    elif command[0] == "last":
        last = []
        amount = int(command[1])
        count = 0
        if amount <= len(digits):
            if command[2] == "even":
                for i in list(reversed(digits)):
                    if i % 2 == 0 and count < amount:
                        last.insert(0, i)
                        count += 1
                print(last)
            elif command[2] == "odd":
                for i in list(reversed(digits)):
                    if i % 2 != 0 and count < amount:
                        last.insert(0, i)
                        count += 1
                print(last)
        else:
            print("Invalid count")

print(digits)
