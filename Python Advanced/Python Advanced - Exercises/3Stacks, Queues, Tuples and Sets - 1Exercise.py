# First Problem

line1 = input().split(" ")
line2 = input().split(" ")
sequence1 = set(map(int, line1))
sequence2 = set(map(int, line2))

number = int(input())
for i in range(number):
    command = input().split(" ")
    key1, key2 = command[0], command[1]

    if key1 == "Add" and key2 == "First":
        for j in range(2, len(command)):
            num = int(command[j])
            sequence1.add(num)

    elif key1 == "Add" and key2 == "Second":
        for j in range(2, len(command)):
            num = int(command[j])
            sequence2.add(num)

    elif key1 == "Remove" and key2 == "First":
        for j in range(2, len(command)):
            num = int(command[j])
            sequence1.discard(num)

    elif key1 == "Remove" and key2 == "Second":
        for j in range(2, len(command)):
            num = int(command[j])
            sequence2.discard(num)

    elif key1 == "Check" and key2 == "Subset":
        if sequence1.issubset(sequence2) or sequence2.issubset(sequence1):
            print("True")
        else:
            print("False")

print(", ".join(map(str, sorted(sequence1))))
print(", ".join(map(str, sorted(sequence2))))



# Second Problem

equation = input().split(" ")
queue = []
while equation:
    num_or_op = equation.pop(0)
    if not num_or_op.lstrip("-").isdigit():
        while len(queue) != 1:
            num1 = int(queue.pop(0))
            num2 = int(queue.pop(0))
            if num_or_op == "-":
                num3 = num1 - num2
            elif num_or_op == "+":
                num3 = num1 + num2
            elif num_or_op == "*":
                num3 = num1 * num2
            elif num_or_op == "/":
                num3 = num1 // num2
            queue.insert(0, num3)
    else:
        queue.append(num_or_op)
print(queue[0])



# Third Problem

stack = list(map(int, input().split(", ")))
queue = list(map(int, input().split(", ")))
milkshakes = 0
while stack and queue and milkshakes != 5:
    chocolate = stack.pop()
    cup = queue.pop(0)

    if cup <= 0 and chocolate <= 0:
        continue
    elif cup <= 0:
        stack.append(chocolate)
        continue
    elif chocolate <= 0:
        queue.insert(0, cup)
        continue

    if cup == chocolate:
        milkshakes += 1
    else:
        queue.append(cup)
        chocolate -= 5
        if chocolate > 0:
            stack.append(chocolate)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

stack = [str(x) for x in stack]
if stack:
    print("Chocolate: ", end="")
    print(", ".join(stack))
else:
    print("Chocolate: empty")

queue = [str(x) for x in queue]
if queue:
    print("Milk: ", end="")
    print(", ".join(queue))
else:
    print("Milk: empty")



# Fourth Problem

queue = list(map(int, input().split(" ")))
stack = list(map(int, input().split(" ")))
symbols = input().split(" ")
total = 0
while queue and stack:
    bee = queue.pop(0)
    nectar = stack.pop()
    if nectar >= bee:
        honey = 0
        symbol = symbols.pop(0)
        if symbol == "+":
            honey = bee + nectar
        elif symbol == "-":
            honey = bee - nectar
        elif symbol == "*":
            honey = bee * nectar
        elif symbol == "/":
            if nectar == 0:
                continue
            honey = bee / nectar
        total += abs(honey)
    elif nectar < bee:
        queue.insert(0, bee)
        continue

print(f"Total honey made: {total}")

if queue:
    print("Bees left: ", end="")
    queue = [str(x) for x in queue]
    print(", ".join(queue))
if stack:
    print("Nectar left: ", end="")
    stack = [str(x) for x in stack]
    print(", ". join(stack))



# Fifth Problem

stack = list(map(int, input().split(" ")))
queue = list(map(int, input().split(" ")))
task = False
presents = {}
while stack and queue:
    box = stack.pop()
    magic_level = queue.pop(0)

    if box == 0 and magic_level == 0:
        continue
    elif box == 0:
        queue.insert(0, magic_level)
        continue
    elif magic_level == 0:
        stack.append(box)
        continue

    product = box * magic_level

    if product == 150:
        if "Doll" not in presents:
            presents["Doll"] = 1
        else:
            presents["Doll"] += 1
        continue
    elif product == 250:
        if "Wooden train" not in presents:
            presents["Wooden train"] = 1
        else:
            presents["Wooden train"] += 1
        continue
    elif product == 300:
        if "Teddy bear" not in presents:
            presents["Teddy bear"] = 1
        else:
            presents["Teddy bear"] += 1
        continue
    elif product == 400:
        if "Bicycle" not in presents:
            presents["Bicycle"] = 1
        else:
            presents["Bicycle"] += 1
        continue

    if product < 0:
        value = box + magic_level
        stack.append(value)
    elif product > 0:
        box += 15
        stack.append(box)

if "Doll" in presents and "Wooden train" in presents:
    task = True

if "Teddy bear" in presents and "Bicycle" in presents:
    task = True

if task:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if stack:
    stack = [str(x) for x in stack]
    print("Materials left: ", end="")
    print(", ".join(reversed(stack)))

if queue:
    queue = [str(x) for x in queue]
    print("Magic left: ", end="")
    print(", ".join(queue))

sorted_toys = sorted(presents.keys())
for toy in sorted_toys:
    print(f"{toy}: {presents[toy]}")



# Sixth Problem

input_string = input()
colors = ["red", "yellow", "blue", "orange", "purple", "green"]
found_colors = []

substrings = input_string.split()

while substrings:
    if len(substrings) == 1:
        last = substrings.pop(0)
        if last in colors:
            found_colors.append(last)
    else:
        first = substrings.pop(0)
        last = substrings.pop()
        combination1 = first + last
        combination2 = last + first
        if combination1 in colors:
            found_colors.append(combination1)
        elif combination2 in colors:
            found_colors.append(combination2)
        else:
            first = first[:-1]
            last = last[:-1]

            if first:
                substrings.insert(len(substrings) // 2, first)
            if last:
                substrings.insert(len(substrings) // 2, last)

if "orange" in found_colors and ("red" not in found_colors or "yellow" not in found_colors):
    found_colors.remove("orange")
if "purple" in found_colors and ("red" not in found_colors or "blue" not in found_colors):
    found_colors.remove("purple")
if "green" in found_colors and ("yellow" not in found_colors or "blue" not in found_colors):
    found_colors.remove("green")

print(found_colors)
