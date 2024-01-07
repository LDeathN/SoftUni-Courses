# First Problem

queue = [int(x) for x in input().split()]
stack = [int(x) for x in input().split()]
ducks = {}
while queue and stack:
    time = queue.pop(0)
    task = stack.pop()
    result = time * task
    if 0 <= result <= 60:
        if "Darth Vader Ducky" not in ducks:
            ducks["Darth Vader Ducky"] = 0
        ducks["Darth Vader Ducky"] += 1
    elif 61 <= result <= 120:
        if "Thor Ducky" not in ducks:
            ducks["Thor Ducky"] = 0
        ducks["Thor Ducky"] += 1
    elif 121 <= result <= 180:
        if "Big Blue Rubber Ducky" not in ducks:
            ducks["Big Blue Rubber Ducky"] = 0
        ducks["Big Blue Rubber Ducky"] += 1
    elif 181 <= result <= 240:
        if "Small Yellow Rubber Ducky" not in ducks:
            ducks["Small Yellow Rubber Ducky"] = 0
        ducks["Small Yellow Rubber Ducky"] += 1
    else:
        task -= 2
        queue.append(time)
        stack.append(task)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
print(f"Darth Vader Ducky: {ducks['Darth Vader Ducky'] if 'Darth Vader Ducky' in ducks else 0}")
print(f"Thor Ducky: {ducks['Thor Ducky'] if 'Thor Ducky' in ducks else 0}")
print(f"Big Blue Rubber Ducky: {ducks['Big Blue Rubber Ducky'] if 'Big Blue Rubber Ducky' in ducks else 0}")
print(f"Small Yellow Rubber Ducky: {ducks['Small Yellow Rubber Ducky'] if 'Small Yellow Rubber Ducky' in ducks else 0}")



# Second Problem

rows = int(input())
commands = [x for x in input().split(", ")]
matrix = [[x for x in input()] for _ in range(rows)]
traps = []
hazelnuts = []
position = None
flag = True
collected = 0

for i in range(rows):
    for j in range(rows):
        if matrix[i][j] == "s":
            position = (i, j)
        elif matrix[i][j] == "h":
            hazelnuts.append((i, j))
        elif matrix[i][j] == "t":
            traps.append((i, j))

for command in commands:
    x, y = position
    if command == "up":
        if x - 1 >= 0:
            if (x - 1, y) in hazelnuts:
                collected += 1
                hazelnuts.remove((x - 1, y))
                matrix[x - 1][y] = "*"
                position = (x - 1, y)
                if collected == 3:
                    print(f"Good job! You have collected all hazelnuts!")
                    flag = False
                    break
            elif (x - 1, y) in traps:
                print("Unfortunately, the squirrel stepped on a trap...")
                flag = False
                break
            else:
                position = (x - 1, y)
        else:
            print("The squirrel is out of the field.")
            flag = False
            break

    elif command == "down":
        if x + 1 < rows:
            if (x + 1, y) in hazelnuts:
                collected += 1
                hazelnuts.remove((x + 1, y))
                matrix[x + 1][y] = "*"
                position = (x + 1, y)
                if collected == 3:
                    print(f"Good job! You have collected all hazelnuts!")
                    flag = False
                    break
            elif (x + 1, y) in traps:
                print("Unfortunately, the squirrel stepped on a trap...")
                flag = False
                break
            else:
                position = (x + 1, y)
        else:
            print("The squirrel is out of the field.")
            flag = False
            break

    elif command == "right":
        if y + 1 < rows:
            if (x, y + 1) in hazelnuts:
                collected += 1
                hazelnuts.remove((x, y + 1))
                matrix[x][y + 1] = "*"
                position = (x, y + 1)
                if collected == 3:
                    print(f"Good job! You have collected all hazelnuts!")
                    flag = False
                    break
            elif (x, y + 1) in traps:
                print("Unfortunately, the squirrel stepped on a trap...")
                flag = False
                break
            else:
                position = (x, y + 1)
        else:
            print("The squirrel is out of the field.")
            flag = False
            break
    elif command == "left":
        if y - 1 >= 0:
            if (x, y - 1) in hazelnuts:
                collected += 1
                hazelnuts.remove((x, y - 1))
                matrix[x][y - 1] = "*"
                position = (x, y - 1)
                if collected == 3:
                    print(f"Good job! You have collected all hazelnuts!")
                    flag = False
                    break
            elif (x, y - 1) in traps:
                print("Unfortunately, the squirrel stepped on a trap...")
                flag = False
                break
            else:
                position = (x, y - 1)
        else:
            print("The squirrel is out of the field.")
            flag = False
            break

if flag:
    print("There are more hazelnuts to collect.")
print(f"Hazelnuts collected: {collected}")



# Third Problem

def movie_organizer(*args):
    movies = {}
    result = []
    for pair in args:
        name, genre = pair
        if genre not in movies:
            movies[genre] = []
        movies[genre].append(name)
    movies = sorted(movies.items(), key=lambda x: x[0])
    movies = dict(movies)
    movies = sorted(movies.items(), key=lambda x: len(x[1]), reverse=True)
    movies = dict(movies)
    for key, values in movies.items():
        result.append(f"{key} - {len(values)}")
        for value in sorted(values):
            result.append(f"* {value}")
    return "\n".join(result)


