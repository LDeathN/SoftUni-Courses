# First Problem

jobs = [int(x) for x in input().split(", ")]
wanted_index = int(input())
total = 0
while True:
    smallest = 1000
    for i in range(len(jobs)):
        if jobs[i] < smallest and jobs[i] != 0:
            smallest = jobs[i]
            index = i
    jobs[index] = 0
    total += smallest
    if index == wanted_index:
        print(total)
        break



# Second Problem

board = [[x for x in input().split()] for i in range(8)]
king = None
queens = []
checks = []

for i in range(8):
    for j in range(8):
        if board[i][j] == "K":
            king = (i, j)
        elif board[i][j] == "Q":
            queens.append((i, j))

for queen in queens:
    qx, qy = queen
    kx, ky = king

    if qx == kx or qy == ky or abs(qx - kx) == abs(qy - ky):
        flag = True
        for i in range(min(qx, kx) + 1, max(qx, kx)):
            if (i, qy) in queens:
                flag = False
                break
        for j in range(min(qy, ky) + 1, max(qy, ky)):
            if (qx, j) in queens:
                flag = False
                break
        for i, j in zip(range(qx + 1, kx), range(qy + 1, ky)):
            if (i, j) in queens:
                flag = False
                break
        for i, j in zip(range(qx + 1, kx), range(qy - 1, ky, -1)):
            if (i, j) in queens:
                flag = False
                break

        if flag:
            checks.append([qx, qy])

if checks:
    for check in checks:
        print(check)
else:
    print("The king is safe!")



# Third Problem

def best_list_pureness(numbers, rotations):
    best_sum = 0
    best_rotation = None

    for i in range(rotations + 1):
        current_sum = 0
        for j in range(len(numbers)):
            current_sum += j * numbers[j]
        if current_sum > best_sum:
            best_sum = current_sum
            best_rotation = i
        number = numbers.pop()
        numbers.insert(0, number)
    message = f"Best pureness {best_sum} after {best_rotation} rotations"
    return message
