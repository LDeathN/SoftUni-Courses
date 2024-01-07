# First Problem

sequence = input().split("|")
values = []
for element in reversed(sequence):
    current = element.split()
    current = [value for value in current if value]
    values.extend(current)
print(" ".join(values), end=" ")



# Second Problem

rows = int(input())
matrix = []
for i in range(rows):
    matrix.append([int(x) for x in input().split(" ")])

while True:
    command = input().split(" ")
    if command[0] == "END":
        break

    elif command[0] == "Add":
        row, col, value = int(command[1]), int(command[2]), int(command[3])
        if row in range(0, len(matrix)) and col in range(0, len(matrix)):
            matrix[row][col] += value
        else:
            print("Invalid coordinates")

    elif command[0] == "Subtract":
        row, col, value = int(command[1]), int(command[2]), int(command[3])
        if row in range(0, len(matrix)) and col in range(0, len(matrix)):
            matrix[row][col] -= value
        else:
            print("Invalid coordinates")
for line in matrix:
    line = [str(x) for x in line]
    print(" ".join(line))



# Third Problem

def count_attacks(board, x, y, n):
    attacks = 0
    possible_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                      (1, -2), (1, 2), (2, -1), (2, 1)]

    for dx, dy in possible_moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == "K":
            attacks += 1

    return attacks


def remove_knights(board, n):
    total_removed = 0

    while True:
        max_attacks = 0
        knight_to_remove = None

        for i in range(n):
            for j in range(n):
                if board[i][j] == "K":
                    attacks = count_attacks(board, i, j, n)
                    if attacks > max_attacks:
                        max_attacks = attacks
                        knight_to_remove = (i, j)

        if knight_to_remove is not None:
            x, y = knight_to_remove
            board[x][y] = "0"
            total_removed += 1
        else:
            break

    return total_removed


# Input
n = int(input())
board = [list(input()) for _ in range(n)]

# Calculate and print the number of knights that need to be removed
removed = remove_knights(board, n)
print(removed)



# Fourth Problem

def find_bunny(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "B":
                return i, j

def move(matrix, direction, bunny_i, bunny_j):
    moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
    current_row, current_col = bunny_i, bunny_j
    path = []
    score = 0

    while True:
        current_row, current_col = current_row + moves[direction][0], current_col + moves[direction][1]

        if (
            current_row < 0
            or current_col < 0
            or current_row >= len(matrix)
            or current_col >= len(matrix[current_row])
            or matrix[current_row][current_col] == "X"
        ):
            break
        else:
            path.append([current_row, current_col])
            score += int(matrix[current_row][current_col])

    return path, score

def collect_eggs(matrix):
    bunny_i, bunny_j = find_bunny(matrix)
    best_direction = ""
    best_path = []
    best_score = float("-inf")

    possible_routes = ["up", "down", "left", "right"]

    for direction in possible_routes:
        path, score = move(matrix, direction, bunny_i, bunny_j)

        if score > best_score and path:
            best_score = score
            best_direction = direction
            best_path = path

    return best_direction, best_path, best_score

n = int(input())
matrix = [input().split() for _ in range(n)]
result = collect_eggs(matrix)

print(result[0])
for position in result[1]:
    print(position)
print(result[2])



# Fifth Problem

tea_bags = 0
party = False
rows = int(input())
matrix = [input().split() for _ in range(rows)]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == "A":
            alice = (i, j)
            matrix[i][j] = "*"
        elif matrix[i][j] == "R":
            rabit_hole = (i, j)

while True:
    command = input()
    if command == "down":
        x, y = alice
        if x + 1 < len(matrix):
            if matrix[x + 1][y].isdigit():
                tea_bags += int(matrix[x + 1][y])
                matrix[x + 1][y] = "*"
                if tea_bags >= 10:
                    party = True
                    break
            elif matrix[x + 1][y] == "R":
                matrix[x + 1][y] = "*"
                break
            else:
                matrix[x + 1][y] = "*"
            alice = (x + 1, y)
        else:
            break

    elif command == "up":
        x, y = alice
        if x - 1 >= 0:
            if matrix[x - 1][y].isdigit():
                tea_bags += int(matrix[x - 1][y])
                matrix[x - 1][y] = "*"
                if tea_bags >= 10:
                    party = True
                    break
            elif matrix[x - 1][y] == "R":
                matrix[x - 1][y] = "*"
                break
            else:
                matrix[x - 1][y] = "*"
            alice = (x - 1, y)
        else:
            break

    elif command == "left":
        x, y = alice
        if y - 1 >= 0:
            if matrix[x][y - 1].isdigit():
                tea_bags += int(matrix[x][y - 1])
                matrix[x][y - 1] = "*"
                if tea_bags >= 10:
                    party = True
                    break
            elif matrix[x][y - 1] == "R":
                matrix[x][y - 1] = "*"
                break
            else:
                matrix[x][y - 1] = "*"
            alice = (x, y - 1)
        else:
            break

    elif command == "right":
        x, y = alice
        if y + 1 < len(matrix):
            if matrix[x][y + 1].isdigit():
                tea_bags += int(matrix[x][y + 1])
                matrix[x][y + 1] = "*"
                if tea_bags >= 10:
                    party = True
                    break
            elif matrix[x][y + 1] == "R":
                matrix[x][y + 1] = "*"
                break
            else:
                matrix[x][y + 1] = "*"
            alice = (x, y + 1)
        else:
            break

if party:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")
for line in matrix:
    print(" ".join(line))



# Sixth Problem

def move(position, direction, count):
    x, y = position
    if direction == "left":
        if y - count >= 0:
            if matrix[x][y - count] == ".":
                matrix[x][y] = "."
                matrix[x][y - count] = "A"
                position = (x, y - count)
    elif direction == "right":
        if y + count < len(matrix):
            if matrix[x][y + count] == ".":
                matrix[x][y] = "."
                matrix[x][y + count] = "A"
                position = (x, y + count)
    elif direction == "up":
        if x - count >= 0:
            if matrix[x - count][y] == ".":
                matrix[x][y] = "."
                matrix[x - count][y] = "A"
                position = (x - count, y)
    elif direction == "down":
        if x + count < len(matrix):
            if matrix[x + count][y] == ".":
                matrix[x][y] = "."
                matrix[x + count][y] = "A"
                position = (x + count, y)
    return position


def shoot(position, direction, targets, removed):
    x, y = position
    count = 0
    if direction == "left":
        while y - count > 0:
            count += 1
            if (x, y - count) in targets:
                matrix[x][y - count] = "."
                removed.append([x, y - count])
                targets.remove((x, y - count))
                break
    elif direction == "right":
        while y + count < len(matrix):
            count += 1
            if (x, y + count) in targets:
                matrix[x][y + count] = "."
                removed.append([x, y + count])
                targets.remove((x, y + count))
                break
    elif direction == "down":
        while x + count < len(matrix):
            count += 1
            if (x + count, y) in targets:
                matrix[x + count][y] = "."
                removed.append([x + count, y])
                targets.remove((x + count, y))
                break
    elif direction == "up":
        while x - count > 0:
            count += 1
            if (x - count, y) in targets:
                matrix[x - count][y] = "."
                removed.append([x - count, y])
                targets.remove((x - count, y))
                break
    return targets, removed


matrix = [input().split() for _ in range(5)]
position = None
targets = []
removed = []
commands = int(input())

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == "A":
            position = (i, j)
        elif matrix[i][j] == "x":
            targets.append((i, j))

for i in range(commands):
    if not targets:
        break
    command = input().split()
    action, direction = command[0], command[1]
    if action == "move":
        steps = int(command[2])
        position = move(position, direction, steps)
    elif action == "shoot":
        targets, removed = shoot(position, direction, targets, removed)

if targets:
    print(f"Training not completed! {len(targets)} targets left.")
    for element in removed:
        print(element)
else:
    print(f"Training completed! All {len(removed)} targets hit.")
    for element in removed:
        print(element)



# Seventh Problem

number_of_presents = int(input())
rows = int(input())
neighbourhood = [input().split() for _ in range(rows)]
nice_kids = 0
naughty_kids = 0
santa = None
happy_kids = 0
possible_places = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(len(neighbourhood)):
    for j in range(len(neighbourhood[i])):
        if neighbourhood[i][j] == "S":
            santa = (i, j)
        elif neighbourhood[i][j] == "X":
            naughty_kids += 1
        elif neighbourhood[i][j] == "V":
            nice_kids += 1

while number_of_presents > 0:
    x, y = santa
    command = input()
    if command == "Christmas morning":
        break
    elif command == "up" and x - 1 >= 0:
        neighbourhood[x][y] = "-"
        santa = (x - 1, y)
        if neighbourhood[x - 1][y] == "X":
            pass
        elif neighbourhood[x - 1][y] == "V":
            number_of_presents -= 1
            nice_kids -= 1
            happy_kids += 1
        elif neighbourhood[x - 1][y] == "C":
            dx, dy = (x - 1, y)
            for place in possible_places:
                nx, ny = place
                if 0 <= dx + nx < len(neighbourhood) and 0 <= dy + ny < len(neighbourhood):
                    if neighbourhood[dx + nx][dy + ny] == "V":
                        neighbourhood[dx + nx][dy + ny] = "-"
                        number_of_presents -= 1
                        nice_kids -= 1
                        happy_kids += 1
                    elif neighbourhood[dx + nx][dy + ny] == "X":
                        neighbourhood[dx + nx][dy + ny] = "-"
                        number_of_presents -= 1
                        naughty_kids -= 1


                    if number_of_presents == 0 and nice_kids > 0:
                        break
        neighbourhood[x - 1][y] = "S"

    elif command == "down" and x + 1 < len(neighbourhood):
        neighbourhood[x][y] = "-"
        santa = (x + 1, y)
        if neighbourhood[x + 1][y] == "X":
            pass
        elif neighbourhood[x + 1][y] == "V":
            number_of_presents -= 1
            nice_kids -= 1
            happy_kids += 1
        elif neighbourhood[x + 1][y] == "C":
            dx, dy = (x + 1, y)
            for place in possible_places:
                nx, ny = place
                if 0 <= dx + nx < len(neighbourhood) and 0 <= dy + ny < len(neighbourhood):
                    if neighbourhood[dx + nx][dy + ny] == "V":
                        neighbourhood[dx + nx][dy + ny] = "-"
                        number_of_presents -= 1
                        nice_kids -= 1
                        happy_kids += 1
                    elif neighbourhood[dx + nx][dy + ny] == "X":
                        neighbourhood[dx + nx][dy + ny] = "-"
                        number_of_presents -= 1
                        naughty_kids -= 1


                    if number_of_presents == 0 and nice_kids > 0:
                        break
        neighbourhood[x + 1][y] = "S"

    elif command == "left" and y - 1 >= 0:
        neighbourhood[x][y] = "-"
        santa = (x, y - 1)
        if neighbourhood[x][y - 1] == "X":
            pass
        elif neighbourhood[x][y - 1] == "V":
            number_of_presents -= 1
            nice_kids -= 1
            happy_kids += 1
        elif neighbourhood[x][y - 1] == "C":
            dx, dy = (x, y - 1)
            for place in possible_places:
                nx, ny = place
                if 0 <= dx + nx < len(neighbourhood) and 0 <= dy + ny < len(neighbourhood):
                    if neighbourhood[dx + nx][dy + ny] == "V":
                        neighbourhood[dx + nx][dy + ny] = "-"
                        number_of_presents -= 1
                        nice_kids -= 1
                        happy_kids += 1
                    elif neighbourhood[dx + nx][dy + ny] == "X":
                        neighbourhood[dx + nx][dy + ny] = "-"
                        number_of_presents -= 1
                        naughty_kids -= 1


                    if number_of_presents == 0 and nice_kids > 0:
                        break
        neighbourhood[x][y - 1] = "S"

    elif command == "right" and y + 1 < len(neighbourhood):
        neighbourhood[x][y] = "-"
        santa = (x, y + 1)
        if neighbourhood[x][y + 1] == "X":
            pass
        elif neighbourhood[x][y + 1] == "V":
            number_of_presents -= 1
            nice_kids -= 1
            happy_kids += 1
        elif neighbourhood[x][y + 1] == "C":
            dx, dy = (x, y + 1)
            for place in possible_places:
                nx, ny = place
                if 0 <= dx + nx < len(neighbourhood) and 0 <= dy + ny < len(neighbourhood):
                    if neighbourhood[dx + nx][dy + ny] == "V":
                        neighbourhood[dx + nx][dy + ny] = "-"
                        number_of_presents -= 1
                        nice_kids -= 1
                        happy_kids += 1
                    elif neighbourhood[dx + nx][dy + ny] == "X":
                        neighbourhood[dx + nx][dy + ny] = "-"
                        number_of_presents -= 1
                        naughty_kids -= 1


                    if number_of_presents == 0 and nice_kids > 0:
                        break
        neighbourhood[x][y + 1] = "S"

if number_of_presents <= 0 and nice_kids > 0:
    print("Santa ran out of presents!")

for line in neighbourhood:
    print(" ".join(line))

if nice_kids == 0:
    print(f"Good job, Santa! {happy_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids} nice kid/s.")