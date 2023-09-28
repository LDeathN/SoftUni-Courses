# First Problem

energy = int(input())
won = 0
count = 0
while True:
    distance = input()
    if distance == "End of battle":
        break
    distance = int(distance)
    if energy >= distance:
        won += 1
        energy -= distance
        count += 1
    else:
        print(f"Not enough energy! Game ends with {won} won battles and {energy} energy")
        break
    if count % 3 == 0:
        energy += won
if distance == "End of battle":
    print(f"Won battles: {won}. Energy left: {energy}")



# Second Problem

targets = input().split(" ")
hits = 0
while True:
    shot = input()
    if shot == "End":
        break
    shot = int(shot)
    current = 0
    if 0 <= shot <= len(targets) - 1:
        if int(targets[shot]) == -1:
            continue
        current = int(targets[shot])
        targets[shot] = -1
        hits += 1
        for i in range(0, len(targets)):
            if int(targets[i]) > current and int(targets[i]) != -1:
                targets[i] = int(targets[i]) - current
            elif int(targets[i]) <= current and int(targets[i]) != -1:
                targets[i] = int(targets[i]) + current
print(f"Shot targets: {hits} -> ", end="")
for target in targets:
    print(target, end=" ")



# Third Problem

targets = input().split(" ")
targets = [int(target) for target in targets]
while True:
    command = input()
    if command == "End":
        break
    name, digit1, digit2 = command.split(" ")
    if name == "Shoot":
        index = int(digit1)
        power = int(digit2)
        if 0 <= index <= len(targets) - 1:
            targets[index] = int(targets[index]) - power
            if int(targets[index]) <= 0:
                targets.remove(targets[index])
    elif name == "Strike":
        index = int(digit1)
        radius = int(digit2)
        if 0 <= index <= len(targets) - 1 and 0 <= index + radius <= len(targets) - 1 and 0 <= index - radius <= len(targets) - 1:
            start = index - radius
            end = index + radius
            for i in range(start, end + 1):
                removed = targets[start]
                targets.remove(removed)
        else:
            print(f"Strike missed!")
    elif name == "Add":
        index = int(digit1)
        value = int(digit2)
        if 0 <= index <= len(targets) - 1:
            targets.insert(index, value)
        else:
            print(f"Invalid placement!")
for i in range(0, len(targets)):
    if i != len(targets) - 1:
        print(targets[i], end="|")
    else:
        print(targets[i])