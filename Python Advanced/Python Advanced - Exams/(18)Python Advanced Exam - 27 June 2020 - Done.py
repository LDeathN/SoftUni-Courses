# First Problem

effects = [int(x) for x in input().split(", ")]
casings = [int(x) for x in input().split(", ")]
materials = {"Cherry Bombs": 0, "Datura Bombs": 0, "Smoke Decoy Bombs": 0}
flag = True

while effects and casings and flag:
    effect = effects.pop(0)
    casing = casings.pop()
    if effect + casing == 40:
        materials["Datura Bombs"] += 1
    elif effect + casing == 60:
        materials["Cherry Bombs"] += 1
    elif effect + casing == 120:
        materials["Smoke Decoy Bombs"] += 1
    else:
        casing -= 5
        effects.insert(0, effect)
        casings.append(casing)
    if materials["Smoke Decoy Bombs"] >= 3 and materials["Datura Bombs"] >= 3 and materials["Cherry Bombs"] >= 3:
        flag = False

if not flag:
    print(f"Bene! You have successfully filled the bomb pouch!")
else:
    print(f"You don't have enough materials to fill the bomb pouch.")

if effects:
    print(f"Bomb Effects: {', '.join([str(x) for x in effects])}")
else:
    print(f"Bomb Effects: empty")

if casings:
    print(f"Bomb Casings: {', '.join([str(x) for x in casings])}")
else:
    print(f"Bomb Casings: empty")

for bomb, count in materials.items():
    print(f"{bomb}: {count}")



# Second Problem

rows = int(input())
matrix = [[x for x in input()] for i in range(rows)]
tunnel = []
food = []
eaten = 0
position = None

for i in range(rows):
    for j in range(rows):
        if matrix[i][j] == "S":
            position = (i, j)
        elif matrix[i][j] == "B":
            tunnel.append((i, j))
        elif matrix[i][j] == "*":
            food.append((i, j))

while True:
    x, y = position
    command = input()
    if command == "up":
        if x - 1 >= 0:
            if (x - 1, y) in food:
                matrix[x][y] = "."
                matrix[x - 1][y] = "S"
                food.remove((x - 1, y))
                eaten += 1
                position = (x - 1, y)
            elif (x - 1, y) in tunnel:
                matrix[x][y] = "."
                matrix[x - 1][y] = "."
                tunnel.remove((x - 1, y))
                end = tunnel[0]
                tunnel.remove(tunnel[0])
                i, j = end
                matrix[i][j] = "S"
                position = (i, j)
            else:
                matrix[x][y] = "."
                matrix[x - 1][y] = "S"
                position = (x - 1, y)
        else:
            matrix[x][y] = "."
            break

    elif command == "down":
        if x + 1 < rows:
            if (x + 1, y) in food:
                matrix[x][y] = "."
                matrix[x + 1][y] = "S"
                food.remove((x + 1, y))
                eaten += 1
                position = (x + 1, y)
            elif (x + 1, y) in tunnel:
                matrix[x][y] = "."
                matrix[x + 1][y] = "."
                tunnel.remove((x + 1, y))
                end = tunnel[0]
                tunnel.remove(tunnel[0])
                i, j = end
                matrix[i][j] = "S"
                position = (i, j)
            else:
                matrix[x][y] = "."
                matrix[x + 1][y] = "S"
                position = (x + 1, y)
        else:
            matrix[x][y] = "."
            break

    elif command == "left":
        if y - 1 >= 0:
            if (x, y - 1) in food:
                matrix[x][y] = "."
                matrix[x][y - 1] = "S"
                food.remove((x, y - 1))
                eaten += 1
                position = (x, y - 1)
            elif (x, y - 1) in tunnel:
                matrix[x][y] = "."
                matrix[x][y - 1] = "."
                tunnel.remove((x, y - 1))
                end = tunnel[0]
                tunnel.remove(tunnel[0])
                i, j = end
                matrix[i][j] = "S"
                position = (i, j)
            else:
                matrix[x][y] = "."
                matrix[x][y - 1] = "S"
                position = (x, y - 1)
        else:
            matrix[x][y] = "."
            break

    elif command == "right":
        if y + 1 < rows:
            if (x, y + 1) in food:
                matrix[x][y] = "."
                matrix[x][y + 1] = "S"
                food.remove((x, y + 1))
                eaten += 1
                position = (x, y + 1)
            elif (x, y + 1) in tunnel:
                matrix[x][y] = "."
                matrix[x][y + 1] = "."
                tunnel.remove((x, y + 1))
                end = tunnel[0]
                tunnel.remove(tunnel[0])
                i, j = end
                matrix[i][j] = "S"
                position = (i, j)
            else:
                matrix[x][y] = "."
                matrix[x][y + 1] = "S"
                position = (x, y + 1)
        else:
            matrix[x][y] = "."
            break
    if eaten >= 10:
        break

if eaten >= 10:
    print(f"You won! You fed the snake.")
else:
    print(f"Game over!")

print(f"Food eaten: {eaten}")
for line in matrix:
    print("".join(line))



# Third Problem

def list_manipulator(numbers, command, position, *new):
    if command == "remove":
        if position == "end":
            if new:
                for i in range(new[0]):
                    numbers.pop()
            else:
                numbers.pop()
        elif position == "beginning":
            if new:
                for i in range(new[0]):
                    numbers.pop(0)
            else:
                numbers.pop(0)
    elif command == "add":
        if position == "end":
            for number in new:
                numbers.append(number)
        elif position == "beginning":
            for number in reversed(new):
                numbers.insert(0, number)

    return numbers


