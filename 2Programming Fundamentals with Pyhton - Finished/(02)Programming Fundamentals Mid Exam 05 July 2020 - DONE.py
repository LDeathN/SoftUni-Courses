# First Problem

efficiency1 = int(input())
efficiency2 = int(input())
efficiency3 = int(input())
students = int(input())
hours = 0
total_efficiency = efficiency1 + efficiency2 + efficiency3
while students > 0:
    hours += 1
    if hours % 4 != 0:
        students -= total_efficiency
print(f"Time needed: {hours}h.")



# Second Problem

elements = input().split(" ")
while True:
    command = input()
    if command == "end":
        break
    command = command.split(" ")
    if command[0] == "swap":
        temp = elements[int(command[1])]
        elements[int(command[1])] = elements[int(command[2])]
        elements[int(command[2])] = temp
    elif command[0] == "multiply":
        elements[int(command[1])] = int(elements[int(command[1])]) * int(elements[int(command[2])])
    elif command[0] == "decrease":
        for i in range(0, len(elements)):
            elements[i] = int(elements[i]) - 1

for i in range(0, len(elements)):
    if i != len(elements) - 1:
        print(elements[i], end=", ")
    else:
        print(elements[i])



# Third Problem

numbers = input().split(" ")
bigger = []

for i in range(0, len(numbers)):
    numbers[i] = int(numbers[i])
total = sum(numbers)
average = round(total / len(numbers))

for number in numbers:
    number = int(number)
    if number > average:
        bigger.append(number)
if bigger != []:
    bigger.sort(reverse=True)
    count = 0
    for i in range(0, len(bigger)):
        if count == 5 or bigger == []:
            break
        print(bigger[0], end=" ")
        bigger.remove(bigger[0])
        count += 1
else:
    print("No")


