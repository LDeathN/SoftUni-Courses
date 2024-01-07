# First Problem

stack = [int(x) for x in input().split()]
queue = [int(x) for x in input().split()]
amount_of_fuel_needed = [int(x) for x in input().split()]
count = 0
failed = False
reached_altitudes = []

while amount_of_fuel_needed:
    count += 1
    fuel = stack.pop()
    consumption = queue.pop(0)
    needed_fuel = amount_of_fuel_needed.pop(0)
    result = fuel - consumption

    if result >= needed_fuel:
        print(f"John has reached: Altitude {count}")
        reached_altitudes.append(count)
    else:
        print(f"John did not reach: Altitude {count}")
        failed = True
        break

if not reached_altitudes:
    print("John failed to reach the top.")
    print("John didn't reach any altitude.")
elif failed:
    print("John failed to reach the top.")
    print("Reached altitudes:", end=" ")
    print(", ".join(f"Altitude {altitude}" for altitude in reached_altitudes))
else:
    print("John has reached all the altitudes and managed to reach the top!")



# Second Problem

rows = int(input())
matrix = [[x for x in input()] for _ in range(rows)]
whirlpools = []
numbers = []
collected_fish = 0
position = None
survived = True

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == "S":
            position = (i, j)
        elif matrix[i][j] == "W":
            whirlpools.append((i, j))
        elif matrix[i][j] != "-":
            numbers.append((i, j))

while True:
    x, y = position
    command = input()
    if command == "collect the nets":
        break

    elif command == "up":
        if x - 1 >= 0:
            position = (x - 1, y)
            matrix[x][y] = "-"
            if matrix[x - 1][y] == "W":
                survived = False
                print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{position[0]},{position[1]}]")
                break
            elif matrix[x - 1][y] != "-":
                collected_fish += int(matrix[x - 1][y])
                matrix[x - 1][y] = "S"
            elif matrix[x - 1][y] == "-":
                matrix[x - 1][y] = "S"
        else:
            position = (len(matrix) - 1, y)
            matrix[x][y] = "-"
            if matrix[len(matrix) - 1][y] == "W":
                survived = False
                print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{position[0]},{position[1]}]")
                break
            elif matrix[len(matrix) - 1][y] != "-":
                collected_fish += int(matrix[len(matrix) - 1][y])
                matrix[len(matrix) - 1][y] = "S"
            elif matrix[len(matrix) - 1][y] == "-":
                matrix[len(matrix) - 1][y] = "S"

    elif command == "down":
        if x + 1 < len(matrix):
            position = (x + 1, y)
            matrix[x][y] = "-"
            if matrix[x + 1][y] == "W":
                survived = False
                print(
                    f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{position[0]},{position[1]}]")
                break
            elif matrix[x + 1][y] != "-":
                collected_fish += int(matrix[x + 1][y])
                matrix[x + 1][y] = "S"
            elif matrix[x + 1][y] == "-":
                matrix[x + 1][y] = "S"
        else:
            position = (0, y)
            matrix[x][y] = "-"
            if matrix[0][y] == "W":
                survived = False
                print(
                    f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{position[0]},{position[1]}]")
                break
            elif matrix[0][y] != "-":
                collected_fish += int(matrix[0][y])
                matrix[0][y] = "S"
            elif matrix[0][y] == "-":
                matrix[0][y] = "S"

    elif command == "right":
        if y + 1 < len(matrix):
            position = (x, y + 1)
            matrix[x][y] = "-"
            if matrix[x][y + 1] == "W":
                survived = False
                print(
                    f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{position[0]},{position[1]}]")
                break
            elif matrix[x][y + 1] != "-":
                collected_fish += int(matrix[x][y + 1])
                matrix[x][y + 1] = "S"
            elif matrix[x][y + 1] == "-":
                matrix[x][y + 1] = "S"
        else:
            position = (x, 0)
            matrix[x][y] = "-"
            if matrix[x][0] == "W":
                survived = False
                print(
                    f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{position[0]},{position[1]}]")
                break
            elif matrix[x][0] != "-":
                collected_fish += int(matrix[x][0])
                matrix[x][0] = "S"
            elif matrix[x][0] == "-":
                matrix[x][0] = "S"

    elif command == "left":
        if y - 1 >= 0:
            position = (x, y - 1)
            matrix[x][y] = "-"
            if matrix[x][y - 1] == "W":
                survived = False
                print(
                    f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{position[0]},{position[1]}]")
                break
            elif matrix[x][y - 1] != "-":
                collected_fish += int(matrix[x][y - 1])
                matrix[x][y - 1] = "S"
            elif matrix[x][y - 1] == "-":
                matrix[x][y - 1] = "S"
        else:
            position = (x, len(matrix) - 1)
            matrix[x][y] = "-"
            if matrix[x][len(matrix) - 1] == "W":
                survived = False
                print(
                    f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{position[0]},{position[1]}]")
                break
            elif matrix[x][len(matrix) - 1] != "-":
                collected_fish += int(matrix[x][len(matrix) - 1])
                matrix[x][len(matrix) - 1] = "S"
            elif matrix[x][len(matrix) - 1] == "-":
                matrix[x][len(matrix) - 1] = "S"

if survived:
    if collected_fish >= 20:
        print("Success! You managed to reach the quota!")
    else:
        print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - collected_fish} tons of fish more.")
    if collected_fish > 0:
        print(f"Amount of fish caught: {collected_fish} tons.")
    for line in matrix:
        print("".join(line))



# Third Problem

def team_lineup(*args):
    dictionary = {}
    result = ""
    for pair in args:
        player, country = pair
        if country not in dictionary:
            dictionary[country] = [player]
        else:
            dictionary[country].append(player)
    dictionary = sorted(dictionary.items(), key=lambda x: x)
    dictionary = dict(dictionary)
    dictionary = sorted(dictionary.items(), key=lambda x: len(x[1]), reverse=True)
    dictionary = dict(dictionary)

    for country, players in dictionary.items():
        result += f"{country}:\n"
        for player in players:
            result += f"  -{player}\n"

    lines = result.split('\n')
    result = [line for line in lines if line.strip() != '']
    return "\n".join(result)


