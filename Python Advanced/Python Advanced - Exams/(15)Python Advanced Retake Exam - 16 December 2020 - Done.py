# First Problem

males = list(map(int, input().split()))
females = list(map(int, input().split()))

matches_count = 0
male_index = len(males) - 1
female_index = 0

while male_index >= 0 and female_index < len(females):
    current_male = males[male_index]
    current_female = females[female_index]

    if current_male <= 0:
        males.pop(male_index)
    elif current_female <= 0:
        females.pop(female_index)
    elif current_male % 25 == 0:
        males.pop(male_index)
        if male_index < len(males) and males[male_index] % 25 == 0:
            males.pop(male_index)
    elif current_female % 25 == 0:
        females.pop(female_index)
        if female_index < len(females) and females[female_index] % 25 == 0:
            females.pop(female_index)
    elif current_male == current_female:
        males.pop(male_index)
        females.pop(female_index)
        matches_count += 1
    else:
        females.pop(female_index)
        males[male_index] -= 2
        male_index += 1
    male_index -= 1

print(f"Matches: {matches_count}")
print(f"Males left: {'none' if not males else ', '.join(map(str, reversed(males)))}")
print(f"Females left: {'none' if not females else ', '.join(map(str, females))}")



# Second Problem

word = input()
size = int(input())
matrix = [[x for x in input()] for i in range(size)]
commands = int(input())
position = None
letters = []

for i in range(size):
    for j in range(size):
        if matrix[i][j] == "P":
            position = (i, j)
        elif matrix[i][j] != "-":
            letters.append((i, j))

for i in range(commands):
    x, y = position
    command = input()
    if command == "up":
        if x - 1 >= 0:
            matrix[x][y] = "-"
            if (x - 1, y) in letters:
                word += matrix[x - 1][y]
                letters.remove((x - 1, y))
            matrix[x - 1][y] = "P"
            position = (x - 1, y)
        else:
            if word:
                word = word[:len(word) - 1]

    elif command == "down":
        if x + 1 < size:
            matrix[x][y] = "-"
            if (x + 1, y) in letters:
                word += matrix[x + 1][y]
                letters.remove((x + 1, y))
            matrix[x + 1][y] = "P"
            position = (x + 1, y)

        else:
            if word:
                word = word[:len(word) - 1]

    elif command == "right":
        if y + 1 < size:
            matrix[x][y] = "-"
            if (x, y + 1) in letters:
                word += matrix[x][y + 1]
                letters.remove((x, y + 1))
            matrix[x][y + 1] = "P"
            position = (x, y + 1)
        else:
            if word:
                word = word[:len(word) - 1]

    elif command == "left":
        if y - 1 >= 0:
            matrix[x][y] = "-"
            if (x, y - 1) in letters:
                word += matrix[x][y - 1]
                letters.remove((x, y - 1))
            matrix[x][y - 1] = "P"
            position = (x, y - 1)
        else:
            if word:
                word = word[:len(word) - 1]

print(word)
for line in matrix:
    print("".join(line))



# Third Problem

def get_magic_triangle(n):
    magic_triangle = [[1], [1, 1]]

    for i in range(2, n):
        row = [1]  # First element in each row is always 1
        for j in range(1, i):
            # Each number in the row is the sum of the two numbers above it
            current_number = magic_triangle[i - 1][j - 1] + magic_triangle[i - 1][j]
            row.append(current_number)
        row.append(1)  # Last element in each row is always 1
        magic_triangle.append(row)

    return magic_triangle