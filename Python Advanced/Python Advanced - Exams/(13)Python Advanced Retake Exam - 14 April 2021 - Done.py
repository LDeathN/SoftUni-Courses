# First Problem

orders = [int(x) for x in input().split(", ")]
employees = [int(x) for x in input().split(", ")]
total_pizza = 0

while orders and employees:
    order = orders.pop(0)
    if order > 10 or order <= 0:
        continue
    employee = employees.pop()
    if employee >= order:
        total_pizza += order
        continue
    else:
        order -= employee
        total_pizza += employee
        orders.insert(0, order)

if not orders:
    print(f"All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizza}")
    print(f"Employees: {', '.join([str(x) for x in employees])}")
else:
    print(f"Not all orders are completed.")
    print(f"Orders left: {', '.join([str(x) for x in orders])}")



# Second Problem

player1, player2 = input().split(", ")
matrix = [[x for x in input().split(" ")] for _ in range(7)]
scores = {player1: 501, player2: 501}
count = 0
turn1 = 0
turn2 = 0
points = None

while True:
    player = None
    turn = None
    point = 0
    count += 1
    command = input()
    command = command[1: len(command) - 1].split(", ")
    x, y = int(command[0]), int(command[1])
    if count % 2 != 0:
        points = scores[player1]
        player = player1
        turn1 += 1
        turn = turn1
    elif count % 2 == 0:
        points = scores[player2]
        player = player2
        turn2 += 1
        turn = turn2

    if 0 <= x < 7 and 0 <= y < 7:
        if matrix[x][y] == "D":
            point = (int(matrix[0][y]) + int(matrix[6][y]) + int(matrix[x][0]) + int(matrix[x][6])) * 2

        elif matrix[x][y] == "T":
            point = (int(matrix[0][y]) + int(matrix[6][y]) + int(matrix[x][0]) + int(matrix[x][6])) * 3

        elif matrix[x][y] == "B":
            print(f"{player} won the game with {turn} throws!")
            break
        else:
            point = int(matrix[x][y])
        points -= point
        scores[player] = points
        if points <= 0:
            print(f"{player} won the game with {turn} throws!")
            break



# Third Problem

def flights(*args):
    flight_list = {}
    count = 0
    while True:
        destination = args[count]
        if destination == "Finish":
            break
        passengers = args[count + 1]
        if destination not in flight_list:
            flight_list[destination] = 0
        flight_list[destination] += passengers
        count += 2

    return flight_list
