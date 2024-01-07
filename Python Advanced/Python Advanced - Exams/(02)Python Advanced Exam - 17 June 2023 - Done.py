# First Problem

queue = [int(x) for x in input().split()]
stack = [int(x) for x in input().split()]
challenges = [int(x) for x in input().split()]
while stack and queue:
    tool = queue.pop(0)
    substance = stack.pop()
    result = tool * substance
    if result in challenges:
        challenges.remove(result)
    else:
        tool += 1
        queue.append(tool)
        substance -= 1
        if substance == 0:
            continue
        stack.append(substance)
    if not challenges:
        print("Harry found an ostracon, which is dated to the 6th century BCE.")
        break

if challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")

if queue:
    print("Tools: ", end="")
    print(", ".join([str(x) for x in queue]))

if stack:
    print("Substances: ", end="")
    print(", ".join([str(x) for x in stack]))

if challenges:
    print("Challenges: ", end="")
    print(", ".join([str(x) for x in challenges]))



# Second Problem

rows, cols = [int(x) for x in input().split(",")]
matrix = [[x for x in input()] for _ in range(rows)]
cheese = []
obstacles = []
traps = []
position = None

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == "M":
            position = (i, j)
        elif matrix[i][j] == "C":
            cheese.append((i, j))
        elif matrix[i][j] == "@":
            obstacles.append((i, j))
        elif matrix[i][j] == "T":
            traps.append((i, j))

while True:
    x, y = position
    command = input()
    if command == "danger":
        break
    elif command == "up":
        if x - 1 >= 0:
            if (x - 1, y) in cheese:
                matrix[x][y] = "*"
                cheese.remove((x - 1, y))
                matrix[x - 1][y] = "M"
                if not cheese:
                    print("Happy mouse! All the cheese is eaten, good night!")
                    break
                position = (x - 1, y)
            elif (x - 1, y) in obstacles:
                continue
            elif (x - 1, y) in traps:
                matrix[x][y] = "*"
                matrix[x - 1][y] = "M"
                print("Mouse is trapped!")
                break
            else:
                matrix[x][y] = "*"
                matrix[x - 1][y] = "M"
                position = (x - 1, y)
        else:
            print("No more cheese for tonight!")
            break

    elif command == "down":
        if x + 1 < rows:
            if (x + 1, y) in cheese:
                matrix[x][y] = "*"
                cheese.remove((x + 1, y))
                matrix[x + 1][y] = "M"
                if not cheese:
                    print("Happy mouse! All the cheese is eaten, good night!")
                    break
                position = (x + 1, y)
            elif (x + 1, y) in obstacles:
                continue
            elif (x + 1, y) in traps:
                matrix[x][y] = "*"
                matrix[x + 1][y] = "M"
                print("Mouse is trapped!")
                break
            else:
                matrix[x][y] = "*"
                matrix[x + 1][y] = "M"
                position = (x + 1, y)
        else:
            print("No more cheese for tonight!")
            break

    elif command == "right":
        if y + 1 < cols:
            if (x, y + 1) in cheese:
                matrix[x][y] = "*"
                cheese.remove((x, y + 1))
                matrix[x][y + 1] = "M"
                if not cheese:
                    print("Happy mouse! All the cheese is eaten, good night!")
                    break
                position = (x, y + 1)
            elif (x, y + 1) in obstacles:
                continue
            elif (x, y + 1) in traps:
                matrix[x][y] = "*"
                matrix[x][y + 1] = "M"
                print("Mouse is trapped!")
                break
            else:
                matrix[x][y] = "*"
                matrix[x][y + 1] = "M"
                position = (x, y + 1)
        else:
            print("No more cheese for tonight!")
            break

    elif command == "left":
        if y - 1 >= 0:
            if (x, y - 1) in cheese:
                matrix[x][y] = "*"
                cheese.remove((x, y - 1))
                matrix[x][y - 1] = "M"
                if not cheese:
                    print("Happy mouse! All the cheese is eaten, good night!")
                    break
                position = (x, y - 1)
            elif (x, y - 1) in obstacles:
                continue
            elif (x, y - 1) in traps:
                matrix[x][y] = "*"
                matrix[x][y - 1] = "M"
                print("Mouse is trapped!")
                break
            else:
                matrix[x][y] = "*"
                matrix[x][y - 1] = "M"
                position = (x, y - 1)
        else:
            print("No more cheese for tonight!")
            break

if command == "danger":
    print("Mouse will come back later!")

for line in matrix:
    print("".join(line))



# Third Problem

def gather_credits(needed, *args):
    credits_needed = needed
    enrolled = []
    gathered = 0
    for pair in args:
        course, credit = pair
        if credits_needed > gathered:
            if course not in enrolled:
                enrolled.append(course)
                gathered += credit
            else:
                continue
        elif credits_needed <= gathered:
            break

    if gathered >= credits_needed:
        result = []
        result.append(f"Enrollment finished! Maximum credits: {gathered}.")
        result.append("Courses: ")
        result.append(", ".join(enrolled))
        result = result[0] + "\n" + result[1] + ", ".join(sorted(result[2].split(", ")))
    else:
        result = f"You need to enroll in more courses! You have to gather {credits_needed - gathered} credits more."

    return result
