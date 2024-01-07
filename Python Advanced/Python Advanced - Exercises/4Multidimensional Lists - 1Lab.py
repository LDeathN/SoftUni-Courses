# First Problem

numbers = list(map(int, input().split(", ")))
matrix = []
total = 0
row, column = numbers[0], numbers[1]
for i in range(row):
    line = list(map(int, input().split(", ")))
    total += sum(line)
    matrix.append(line)
print(total)
print(matrix)



# Second Problem

rows = int(input())
matrix = []
for i in range(rows):
    line = list(map(int, input().split(", ")))
    result = [num for num in line if num % 2 == 0]
    matrix.append(result)
print(matrix)



# Third Problem

rows = int(input())
matrix = []
for i in range(rows):
    line = list(map(int, input().split(", ")))
    matrix.append(line)
flattened_matrix = [element for row in matrix for element in row]
print(flattened_matrix)



# Fourth Problem

numbers = list(map(int, input().split(", ")))
rows, columns = numbers[0], numbers[1]
matrix = []
column_sums = []
for i in range(rows):
    line = list(map(int, input().split(" ")))
    matrix.append(line)
for i in range(columns):
    column_sum = sum([row[i] for row in matrix])
    column_sums.append(column_sum)
for element in column_sums:
    print(element)



# Fifth Problem

number = int(input())
matrix = []
primary_diagonal = []
for i in range(number):
    line = list(map(int, input().split(" ")))
    matrix.append(line)
for i in range(len(matrix)):
    number = matrix[i][i]
    primary_diagonal.append(number)
print(sum(primary_diagonal))



# Sixth Problem

number = int(input())
flag = False
matrix = []
result = []
for i in range(number):
    line = input()
    matrix.append(line)
symbol = input()
for i in range(len(matrix)):
    if flag:
        break
    if symbol in matrix[i]:
        result.append(i)
        for j in range(len(matrix)):
            if symbol == matrix[i][j]:
                result.append(j)
                flag = True
                break
if result:
    print(tuple(result))
else:
    print(f"{symbol} does not occur in the matrix")



# Seventh Problem

numbers = list(map(int, input().split(", ")))
rows, columns = numbers[0], numbers[1]
matrix = []
biggest = 0
for i in range(rows):
    line = list(map(int, input().split(", ")))
    matrix.append(line)
for i in range(rows - 1):
    for j in range(columns - 1):
        sub_matrix = [matrix[i][j], matrix[i][j + 1], matrix[i + 1][j], matrix[i + 1][j + 1]]
        if sum(sub_matrix) > biggest:
            result = sub_matrix
            biggest = sum(sub_matrix)
print(f"{result[0]} {result[1]}")
print(f"{result[2]} {result[3]}")
print(biggest)



