# First Problem

customers = [int(x) for x in input().split(", ")]
taxis = [int(x) for x in input().split(", ")]
total_time = 0

while customers and taxis:
    customer = customers.pop(0)
    taxi = taxis.pop()
    if taxi >= customer:
        total_time += customer
    else:
        customers.insert(0, customer)

if customers:
    print(f"Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join([str(x) for x in customers])}")
else:
    print(f"All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")



# Second Problem

rows = int(input())
matrix = []
for i in range(rows):
    matrix.append([0] * rows)

number = int(input())
mines = []
for i in range(number):
    mine = input()
    mine = tuple(int(x) for x in mine[1:len(mine) - 1].split(", "))
    mines.append(mine)

for mine in mines:
    x = mine[0]
    y = mine[1]
    matrix[x][y] = "*"

for i in range(rows):
    row = i
    for j in range(rows):
        col = j
        if matrix[i][j] != "*":
            if row - 1 >= 0:
                if matrix[row - 1][col] == "*":
                    matrix[row][col] += 1
            if row + 1 < rows:
                if matrix[row + 1][col] == "*":
                    matrix[row][col] += 1
            if col - 1 >= 0:
                if matrix[row][col - 1] == "*":
                    matrix[row][col] += 1
            if col + 1 < rows:
                if matrix[row][col + 1] == "*":
                    matrix[row][col] += 1
            if row - 1 >= 0 and col - 1 >= 0:
                if matrix[row - 1][col - 1] == "*":
                    matrix[row][col] += 1
            if row - 1 >= 0 and col + 1 < rows:
                if matrix[row - 1][col + 1] == "*":
                    matrix[row][col] += 1
            if row + 1 < rows and col - 1 >= 0:
                if matrix[row + 1][col - 1] == "*":
                    matrix[row][col] += 1
            if row + 1 < rows and col + 1 < rows:
                if matrix[row + 1][col + 1] == "*":
                    matrix[row][col] += 1
        else:
            continue

for line in matrix:
    print(" ".join([str(x) for x in line]))



# Third Problem

def numbers_searching(*numbers):
    duplicates = []
    unique = []
    missing = None
    biggest_number = max(numbers)
    smallest_number = min(numbers)
    for i in range(smallest_number, biggest_number):
        if i not in numbers:
            missing = i
    for number in numbers:
        if number not in unique:
            unique.append(number)
        else:
            if number not in duplicates:
                duplicates.append(number)
    result = [missing, sorted(duplicates)]
    return result

