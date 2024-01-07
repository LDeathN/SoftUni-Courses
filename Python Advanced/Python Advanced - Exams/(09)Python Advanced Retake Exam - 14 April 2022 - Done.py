# First Problem

bowls = [int(x) for x in input().split(", ")]
customers = [int(x) for x in input().split(", ")]

while bowls and customers:
    bowl = bowls.pop()
    customer = customers.pop(0)
    if bowl == customer:
        continue
    elif bowl > customer:
        bowl -= customer
        bowls.append(bowl)
    elif customer > bowl:
        customer -= bowl
        customers.insert(0, customer)

if not customers:
    print(f"Great job! You served all the customers.")
    if bowls:
        print(f"Bowls of ramen left: {', '.join([str(x) for x in bowls])}")
else:
    print(f"Out of ramen! You didn't manage to serve all customers.")
    if customers:
        print(f"Customers left: {', '.join([str(x) for x in customers])}")



# Second Problem

matrix = [[x for x in input().split(" ")] for _ in range(6)]
water = []
metal = []
concrete = []
rock = []
water_count = 0
metal_count = 0
concrete_count = 0
rover = None

for i in range(6):
    for j in range(6):
        if matrix[i][j] == "E":
            rover = (i, j)
        elif matrix[i][j] == "W":
            water.append((i, j))
        elif matrix[i][j] == "M":
            metal.append((i, j))
        elif matrix[i][j] == "C":
            concrete.append((i, j))
        elif matrix[i][j] == "R":
            rock.append((i, j))

commands = input().split(", ")
for command in commands:
    x, y = rover

    if command == "up":
        if x - 1 >= 0:
            rover = (x - 1, y)
        else:
            rover = (5, y)

        if rover in water:
            water_count += 1
            print(f"Water deposit found at {rover}")
        elif rover in metal:
            metal_count += 1
            print(f"Metal deposit found at {rover}")
        elif rover in concrete:
            concrete_count += 1
            print(f"Concrete deposit found at {rover}")
        elif rover in rock:
            print(f"Rover got broken at {rover}")
            break

    elif command == "down":
        if x + 1 < len(matrix):
            rover = (x + 1, y)
        else:
            rover = (0, y)

        if rover in water:
            water_count += 1
            print(f"Water deposit found at {rover}")
        elif rover in metal:
            metal_count += 1
            print(f"Metal deposit found at {rover}")
        elif rover in concrete:
            concrete_count += 1
            print(f"Concrete deposit found at {rover}")
        elif rover in rock:
            print(f"Rover got broken at {rover}")
            break

    elif command == "right":
        if y + 1 < len(matrix):
            rover = (x, y + 1)
        else:
            rover = (x, 0)

        if rover in water:
            water_count += 1
            print(f"Water deposit found at {rover}")
        elif rover in metal:
            metal_count += 1
            print(f"Metal deposit found at {rover}")
        elif rover in concrete:
            concrete_count += 1
            print(f"Concrete deposit found at {rover}")
        elif rover in rock:
            print(f"Rover got broken at {rover}")
            break

    elif command == "left":
        if y - 1 >= 0:
            rover = (x, y - 1)
        else:
            rover = (x, 5)

        if rover in water:
            water_count += 1
            print(f"Water deposit found at {rover}")
        elif rover in metal:
            metal_count += 1
            print(f"Metal deposit found at {rover}")
        elif rover in concrete:
            concrete_count += 1
            print(f"Concrete deposit found at {rover}")
        elif rover in rock:
            print(f"Rover got broken at {rover}")
            break

if water_count >= 1 and concrete_count >= 1 and metal_count >= 1:
    print(f"Area suitable to start the colony.")
else:
    print(f"Area not suitable to start the colony.")



# Third Problem

def words_sorting(*args):
    words = {}
    result = []
    total = 0

    for word in args:
        ascii_value = 0
        for letter in word:
            ascii_value += ord(letter)
        total += ascii_value
        words[word] = ascii_value

    if total % 2 == 0:
        words = sorted(words.items(), key=lambda x: x)
        words = dict(words)
    else:
        words = sorted(words.items(), key=lambda x: x[1], reverse=True)
        words = dict(words)

    for word, value in words.items():
        result.append(f"{word} - {value}")

    return "\n".join(result)