# First Problem

queue = [int(x) for x in input().split()]
stack = [int(x) for x in input().split()]
items = [30, 40, 100]
crafted = {}
while queue and stack:
    textiles = queue.pop(0)
    medicament = stack.pop()
    result = textiles + medicament
    if result in items:
        if result == 30:
            if "Patch" not in crafted:
                crafted["Patch"] = 0
            crafted["Patch"] += 1
        elif result == 40:
            if "Bandage" not in crafted:
                crafted["Bandage"] = 0
            crafted["Bandage"] += 1
        elif result == 100:
            if "MedKit" not in crafted:
                crafted["MedKit"] = 0
            crafted["MedKit"] += 1
    elif result > 100:
        if "MedKit" not in crafted:
            crafted["MedKit"] = 0
        crafted["MedKit"] += 1
        result -= 100
        result1 = stack.pop()
        result1 += result
        stack.append(result1)
    else:
        medicament += 10
        stack.append(medicament)

if not queue and not stack:
    print("Textiles and medicaments are both empty.")
elif not queue:
    print("Textiles are empty.")
elif not stack:
    print("Medicaments are empty.")

crafted = sorted(crafted.items(), key=lambda x: x[0])
crafted = dict(crafted)
crafted = sorted(crafted.items(), key=lambda x: x[1], reverse=True)
crafted = dict(crafted)
if len(crafted) >= 1:
    for key, value in crafted.items():
        print(f"{key} - {value}")

if stack:
    stack.reverse()
    print(f"Medicaments left: {', '.join(map(str, stack))}")
if queue:
    print(f"Textiles left: {', '.join(map(str, queue))}")



# Second Problem

rows, cols = [int(x) for x in input().split()]
matrix = [[x for x in input() if x != " "] for _ in range(rows)]
obstacles = []
enemies = []
position = None
touched = 0
moves = 0
flag = True

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == "B":
            position = (i, j)
        elif matrix[i][j] == "O":
            obstacles.append((i, j))
        elif matrix[i][j] == "P":
            enemies.append((i, j))

while True:
    x, y = position
    command = input()
    if command == "Finish":
        break

    elif command == "up":
        if x - 1 >= 0:
            if (x - 1, y) in obstacles:
                continue
            elif (x - 1, y) in enemies:
                touched += 1
                moves += 1
                enemies.remove((x - 1, y))
                matrix[x - 1][y] = "-"
                position = (x - 1, y)
                if not enemies:
                    print("Game over!")
                    print(f"Touched opponents: {touched} Moves made: {moves}")
                    flag = False
                    break

            else:
                moves += 1
                position = (x - 1, y)
        else:
            continue

    elif command == "down":
        if x + 1 < rows:
            if (x + 1, y) in obstacles:
                continue
            elif (x + 1, y) in enemies:
                touched += 1
                moves += 1
                enemies.remove((x + 1, y))
                matrix[x + 1][y] = "-"
                position = (x + 1, y)
                if not enemies:
                    print("Game over!")
                    print(f"Touched opponents: {touched} Moves made: {moves}")
                    flag = False
                    break
            else:
                moves += 1
                position = (x + 1, y)
        else:
            continue

    elif command == "right":
        if y + 1 < cols:
            if (x, y + 1) in obstacles:
                continue
            elif (x, y + 1) in enemies:
                touched += 1
                moves += 1
                enemies.remove((x, y + 1))
                matrix[x][y + 1] = "-"
                position = (x, y + 1)
                if not enemies:
                    print("Game over!")
                    print(f"Touched opponents: {touched} Moves made: {moves}")
                    flag = False
                    break
            else:
                moves += 1
                position = (x, y + 1)
        else:
            continue

    elif command == "left":
        if y - 1 >= 0:
            if (x, y - 1) in obstacles:
                continue
            elif (x, y - 1) in enemies:
                touched += 1
                moves += 1
                enemies.remove((x, y - 1))
                matrix[x][y - 1] = "-"
                position = (x, y - 1)
                if not enemies:
                    print("Game over!")
                    print(f"Touched opponents: {touched} Moves made: {moves}")
                    flag = False
                    break
            else:
                moves += 1
                position = (x, y - 1)
        else:
            continue

if flag:
    print("Game over!")
    print(f"Touched opponents: {touched} Moves made: {moves}")



# Third Problem

def shop_from_grocery_list(budget, grocery_list, *args):
    for pair in args:
        product, price = pair
        if budget - price >= 0 and product in grocery_list:
            grocery_list.remove(product)
            budget -= price
        elif budget - price < 0:
            break
        elif product not in grocery_list:
            continue
    if not grocery_list:
        result = f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        result = f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."
    return result


