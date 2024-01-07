# First Problem

fireworks = [int(x) for x in input().split(", ")]
powers = [int(x) for x in input().split(", ")]
palm = 0
willow = 0
crossette = 0

while fireworks and powers:
    firework = fireworks.pop(0)
    if firework <= 0:
        continue
    power = powers.pop()
    if power <= 0:
        fireworks.insert(0, firework)
        continue
    result = power + firework
    if result % 3 == 0 and result % 5 == 0:
        crossette += 1
    elif result % 3 == 0 and result % 5 != 0:
        palm += 1
    elif result % 5 == 0 and result % 3 != 0:
        willow += 1
    else:
        firework -= 1
        fireworks.append(firework)
        powers.append(power)
    if palm >= 3 and willow >= 3 and crossette >= 3:
        break

if palm >= 3 and willow >= 3 and crossette >= 3:
    print(f"Congrats! You made the perfect firework show!")
else:
    print(f"Sorry. You can't make the perfect firework show.")

if fireworks:
    print(f"Firework Effects left: {', '.join([str(x) for x in fireworks])}")
if powers:
    print(f"Explosive Power left: {', '.join([str(x) for x in powers])}")

print(f"Palm Fireworks: {palm}")
print(f"Willow Fireworks: {willow}")
print(f"Crossette Fireworks: {crossette}")



# Second Problem

rows = int(input())
matrix = [[x for x in input().split()] for i in range(rows)]
walls = []
numbers = []
coins = 0
position = None
path = []

for i in range(rows):
    for j in range(rows):
        if matrix[i][j] == "P":
            position = (i, j)
            path.append([i, j])
        elif matrix[i][j] == "X":
            walls.append((i, j))
        else:
            numbers.append((i, j))

while True:
    command = input()
    x, y = position
    if command == "up":
        if x - 1 >= 0:
            path.append([x - 1, y])
            if (x - 1, y) in walls:
                coins = coins // 2
                print(f"Game over! You've collected {coins} coins.")
                break
            elif (x - 1, y) in numbers:
                numbers.remove((x - 1, y))
                coins += int(matrix[x - 1][y])
            position = (x - 1, y)
        else:
            position = (rows - 1, y)
            x, y = position
            path.append([x, y])
            if (x, y) in walls:
                coins = coins // 2
                print(f"Game over! You've collected {coins} coins.")
                break
            elif (x, y) in numbers:
                numbers.remove((x, y))
                coins += int(matrix[x][y])
    elif command == "down":
        if x + 1 < rows:
            path.append([x + 1, y])
            if (x + 1, y) in walls:
                coins = coins // 2
                print(f"Game over! You've collected {coins} coins.")
                break
            elif (x + 1, y) in numbers:
                numbers.remove((x + 1, y))
                coins += int(matrix[x + 1][y])
            position = (x + 1, y)
        else:
            position = (0, y)
            x, y = position
            path.append([x, y])
            if (x, y) in walls:
                coins = coins // 2
                print(f"Game over! You've collected {coins} coins.")
                break
            elif (x, y) in numbers:
                numbers.remove((x, y))
                coins += int(matrix[x][y])
    elif command == "right":
        if y + 1 < rows:
            path.append([x, y + 1])
            if (x, y + 1) in walls:
                coins = coins // 2
                print(f"Game over! You've collected {coins} coins.")
                break
            elif (x, y + 1) in numbers:
                numbers.remove((x, y + 1))
                coins += int(matrix[x][y + 1])
            position = (x, y + 1)
        else:
            position = (x, 0)
            x, y = position
            path.append([x, y])
            if (x, y) in walls:
                coins = coins // 2
                print(f"Game over! You've collected {coins} coins.")
                break
            elif (x, y) in numbers:
                numbers.remove((x, y))
                coins += int(matrix[x][y])
    elif command == "left":
        if y - 1 >= 0:
            path.append([x, y - 1])
            if (x, y - 1) in walls:
                coins = coins // 2
                print(f"Game over! You've collected {coins} coins.")
                break
            elif (x, y - 1) in numbers:
                numbers.remove((x, y - 1))
                coins += int(matrix[x][y - 1])
            position = (x, y - 1)
        else:
            position = (x, rows - 1)
            x, y = position
            path.append([x, y])
            if (x, y) in walls:
                coins = coins // 2
                print(f"Game over! You've collected {coins} coins.")
                break
            elif (x, y) in numbers:
                numbers.remove((x, y))
                coins += int(matrix[x][y])
    if coins >= 100:
        print(f"You won! You've collected {coins} coins.")
        break

print("Your path:")
for element in path:
    print(element)



# Third Problem

def stock_availability(flavours, option, *args):
    if option == "delivery":
        for element in args:
            flavours.append(element)
    elif option == "sell":
        if args:
            for element in args:
                if type(element) == int:
                    element = int(args[0])
                    for i in range(element):
                        flavours.remove(flavours[0])
                else:
                    for flavour in flavours:
                        if flavour == element:
                            number = flavours.count(flavour)
                            for j in range(number):
                                flavours.remove(flavour)

        else:
            flavours.remove(flavours[0])

    return flavours



