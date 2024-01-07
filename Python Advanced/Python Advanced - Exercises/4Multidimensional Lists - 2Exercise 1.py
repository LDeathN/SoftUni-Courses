# First Problem

number = int(input())
matrix = []
primary_diagonal = []
secondary_diagonal = []
for i in range(number):
    line = list(map(int, input().split(", ")))
    matrix.append(line)
for i in range(len(matrix)):
    number1 = matrix[i][i]
    number2 = matrix[i][(len(matrix) - 1) - i]
    primary_diagonal.append(number1)
    secondary_diagonal.append(number2)
primary_diagonal_1 = [str(x) for x in primary_diagonal]
secondary_diagonal_1 = [str(x) for x in secondary_diagonal]
print(f"Primary diagonal: {', '.join(primary_diagonal_1)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(secondary_diagonal_1)}. Sum: {sum(secondary_diagonal)}")



# Second Problem

number = int(input())
matrix = []
primary_diagonal = []
secondary_diagonal = []
for i in range(number):
    line = list(map(int, input().split(" ")))
    matrix.append(line)
for i in range(len(matrix)):
    number1 = matrix[i][i]
    number2 = matrix[i][(len(matrix) - 1) - i]
    primary_diagonal.append(number1)
    secondary_diagonal.append(number2)
primary_sum = sum(primary_diagonal)
secondary_sum = sum(secondary_diagonal)
print(abs(primary_sum - secondary_sum))



# Third Problem

numbers = list(map(int, input().split(" ")))
rows, columns = numbers[0], numbers[1]
matrix = []
result = 0
for i in range(rows):
    line = input().split(" ")
    matrix.append(line)
for i in range(rows - 1):
    for j in range(columns - 1):
        sub_matrix = [matrix[i][j], matrix[i][j + 1], matrix[i + 1][j], matrix[i + 1][j + 1]]
        if all(element == sub_matrix[0] for element in sub_matrix):
            result += 1
print(result)



# Fourth Problem

rows, columns = map(int, input().split())
matrix = []
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)
max_sum = None
max_submatrix = None

for i in range(rows - 2):
    for j in range(columns - 2):
        submatrix = [
            matrix[i][j], matrix[i][j + 1], matrix[i][j + 2],
            matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2],
            matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]
        ]
        submatrix_sum = sum(submatrix)
        if max_sum is None or submatrix_sum > max_sum:
            max_sum = submatrix_sum
            max_submatrix = submatrix

print(f"Sum = {max_sum}")
for i in range(3):
    for j in range(3):
        print(max_submatrix[i * 3 + j], end=" ")
    print()



# Fifth Problem

rows, columns = list(map(int, input().split(" ")))
matrix = []
count = 0
value = 97
for i in range(rows):
    for j in range(columns):
        element = "".join([chr(value), chr(value + count), chr(value)])
        matrix.append(element)
        count += 1
    value += 1
    count = 0
    print(" ".join(matrix))
    matrix = []



# Sixth Problem

rows, columns = list(map(int, input().split(" ")))
matrix = []
for i in range(rows):
    line = input().split(" ")
    matrix.append(line)
while True:
    command = input().split(" ")
    if command[0] == "END":
        break
    elif command[0] == "swap":
        if len(command) == 5 and int(command[1]) in range(rows) and int(command[3]) in range(rows) and int(command[2]) in range(columns) and int(command[4]) in range(columns):
            row1, col1 = int(command[1]), int(command[2])
            row2, col2 = int(command[3]), int(command[4])
            changed = matrix[row1][col1]
            matrix[row1][col1] = matrix[row2][col2]
            matrix[row2][col2] = changed
            for i in range(rows):
                line = matrix[i]
                print(" ".join(line))

        else:
            print("Invalid input!")
    else:
        print("Invalid input!")



# Seventh Problem

rows, columns = list(map(int, input().split(" ")))
snake = input()
left = [x for x in snake]
for i in range(rows):
    if not left:
        left = [x for x in snake]
    current = ""
    for j in range(columns):
        if not left:
            left = [x for x in snake]
        current += left.pop(0)
    if i % 2 == 0:
        print(current)
    elif i % 2 != 0:
        print("".join(reversed(current)))



# Eighth Problem

number = int(input())
matrix = []
for i in range(number):
    line = list(map(int, input().split()))
    matrix.append(line)

bombs = input().split()
for bomb_coord in bombs:
    row, column = map(int, bomb_coord.split(","))
    if matrix[row][column] > 0:
        bomb_value = matrix[row][column]
        matrix[row][column] = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                new_row, new_column = row + i, column + j
                if 0 <= new_row < number and 0 <= new_column < number and matrix[new_row][new_column] > 0:
                    matrix[new_row][new_column] -= bomb_value

alive_cells = [cell for row in matrix for cell in row if cell > 0]

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")

for row in matrix:
    print(" ".join(map(str, row)))



# Ninth Problem

number = int(input())
commands = input().split()
matrix = [input().split() for _ in range(number)]
position = [(row, col) for row, line in enumerate(matrix) for col, cell in enumerate(line) if cell == 's'][0]
coal = sum(line.count("c") for line in matrix)
flag = False
condition = True

for command in commands:
    if flag:
        break

    row, col = position
    matrix[row][col] = "*"

    if command == "up" and row > 0:
        row -= 1
    elif command == "down" and row < number - 1:
        row += 1
    elif command == "left" and col > 0:
        col -= 1
    elif command == "right" and col < len(matrix[row]) - 1:
        col += 1

    if matrix[row][col] == "c":
        coal -= 1
        matrix[row][col] = "s"
        position = (row, col)
        if coal == 0:
            flag = True
    elif matrix[row][col] == "e":
        position = (row, col)
        print("Game over!", end=" ")
        condition = False
        break
    else:
        matrix[row][col] = "s"
        position = (row, col)

if flag:
    print("You collected all coal!", end=" ")
elif not flag and not any("c" in line for line in matrix):
    print("You collected all coal!", end=" ")
elif not flag and condition:
    print(f"{coal} pieces of coal left.", end=" ")
print(position)



# Tenth Problem

rows, cols = [int(item) for item in input().split()]
matrix = []

for _ in range(rows):
    matrix.append(list(input()))

commands = input()

# End of inputs


def find_player(matrix):
    stop = False
    postion = ()
    for r in range(rows):
        if stop:
            break
        for c in range(cols):
            if matrix[r][c] == 'P':
                postion = (r, c)
                stop = True
    return postion


def multiply_bunny(matrix, dead):
    bunnies_location = []
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 'B':
                bunnies_location.append((r, c))

    for bun in bunnies_location:
        up = (bun[0] - 1, bun[1])
        down = (bun[0] + 1, bun[1])
        left = (bun[0], bun[1] - 1)
        right = (bun[0], bun[1] + 1)

        if 0 <= up[0] < rows and 0 <= up[1] < cols:
            if matrix[up[0]][up[1]] == 'P':
                dead = True
            matrix[up[0]][up[1]] = 'B'
        if 0 <= down[0] < rows and 0 <= down[1] < cols:
            if matrix[down[0]][down[1]] == 'P':
                dead = True
            matrix[down[0]][down[1]] = 'B'
        if 0 <= left[0] < rows and 0 <= left[1] < cols:
            if matrix[left[0]][left[1]] == 'P':
                dead = True
            matrix[left[0]][left[1]] = 'B'
        if 0 <= right[0] < rows and 0 <= right[1] < cols:
            if matrix[right[0]][right[1]] == 'P':
                dead = True
            matrix[right[0]][right[1]] = 'B'

    return dead, matrix


def move_player(loc, go, matrix, dead):
    out = False
    last = loc
    if go == 'U':
        new = (loc[0] - 1, loc[1])
        if 0 <= new[0] < rows and 0 <= new[1] < cols:
            last = new
            if matrix[new[0]][new[1]] == 'B':
                dead = True
                return last, dead, out, matrix
            else:
                matrix[new[0]][new[1]] = 'P'
                matrix[loc[0]][loc[1]] = '.'
                return last, dead, out, matrix
        else:
            out = True
            matrix[last[0]][last[1]] = '.'
            return last, dead, out, matrix

    elif go == 'D':
        new = (loc[0] + 1, loc[1])
        if 0 <= new[0] < rows and 0 <= new[1] < cols:
            last = new
            if matrix[new[0]][new[1]] == 'B':
                dead = True
                return last, dead, out, matrix
            else:
                matrix[new[0]][new[1]] = 'P'
                matrix[loc[0]][loc[1]] = '.'
                return last, dead, out, matrix
        else:
            out = True
            matrix[last[0]][last[1]] = '.'
            return last, dead, out, matrix

    elif go == 'L':
        new = (loc[0], loc[1] - 1)
        if 0 <= new[0] < rows and 0 <= new[1] < cols:
            last = new
            if matrix[new[0]][new[1]] == 'B':
                dead = True
                return last, dead, out, matrix
            else:
                matrix[new[0]][new[1]] = 'P'
                matrix[loc[0]][loc[1]] = '.'
                return last, dead, out, matrix
        else:
            out = True
            matrix[last[0]][last[1]] = '.'
            return last, dead, out, matrix

    elif go == 'R':
        new = (loc[0], loc[1] + 1)
        if 0 <= new[0] < rows and 0 <= new[1] < cols:
            last = new
            if matrix[new[0]][new[1]] == 'B':
                dead = True
                return last, dead, out, matrix
            else:
                matrix[new[0]][new[1]] = 'P'
                matrix[loc[0]][loc[1]] = '.'
                return last, dead, out, matrix
        else:
            out = True
            matrix[last[0]][last[1]] = '.'
            return last, dead, out, matrix

    return last, dead, out, matrix

# Main
dead = False
where = find_player(matrix)
for ch in commands:
    where, dead, out, matrix = move_player(where, ch, matrix, dead)
    dead, matrix = multiply_bunny(matrix, dead)
    if dead or out:
        break

if dead:
    for row in matrix:
        print(*row, sep="")

    print("dead: ", end='')
    print(*where, sep=' ')
else:
    for row in matrix:
        print(*row, sep="")
    print("won: ", end='')
    print(*where, sep=' ')