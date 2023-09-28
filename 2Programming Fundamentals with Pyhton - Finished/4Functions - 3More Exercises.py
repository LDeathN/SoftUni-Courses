# First Problem

input1 = str(input())
input2 = input()
def function(type, number):
    if type == "int":
        result = int(number) * 2
        return result
    elif type == "real":
        result = float(number) * 1.50
        return f"{result:.2f}"
    elif type == "string":
        return f"${number}$"

print(function(input1, input2))



# Second Problem

from math import floor
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

def closest(x1, y1, x2, y2):
    distance1 = (abs(x1) ** 2 + abs(y1) ** 2)
    distance2 = (abs(x2) ** 2 + abs(y2) ** 2)
    if distance1 <= distance2:
        return f"({floor(x1)}, {floor(y1)})"
    else:
        return f"({floor(x2)}, {floor(y2)})"

print(closest(x1, y1, x2, y2))



# Third Problem

from math import floor
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())
def closest(x1, y1, x2, y2, x3, y3, x4, y4):
    line1 = (x2 - x1) ** 2 + (y2 - y1) ** 2
    line2 = (x4 - x3) ** 2 + (y4 - y3) ** 2
    if line1 >= line2:
        distance1 = (abs(x1) ** 2 + abs(y1) ** 2)
        distance2 = (abs(x2) ** 2 + abs(y2) ** 2)
        if distance1 <= distance2:
            return f"({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})"
        else:
            return f"({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})"
    else:
        distance3 = (abs(x3) ** 2 + abs(y3) ** 2)
        distance4 = (abs(x4) ** 2 + abs(y4) ** 2)
        if distance3 <= distance4:
            return f"({floor(x3)}, {floor(y3)})({floor(x4)}, {floor(y4)})"
        else:
            return f"({floor(x4)}, {floor(y4)})({floor(x3)}, {floor(y3)})"

print(closest(x1, y1, x2, y2, x3, y3, x4, y4))



# Fourth Problem

integer = int(input())

def tribonacci_sequence(number):
    result = [1]
    current = 0
    sum = [1]
    for i in range(1, number):
        if len(sum) == 4:
            sum.pop(0)
        for j in range(0, len(sum)):
            current += sum[j]
        sum.append(current)
        result.append(current)
        current = 0
    for i in result:
        print(int(i), end=" ")

tribonacci_sequence(integer)



# Fifth Problem

n1 = float(input())
n2 = float(input())
n3 = float(input())

def multiplication_sign(n1, n2, n3):
    negative = 0
    if n1 == 0 or n2 == 0 or n3 == 0:
        print("zero")
    else:
        if n1 < 0:
            negative += 1
        if n2 < 0:
            negative += 1
        if n3 < 0:
            negative += 1
        if negative % 2 == 0:
            print("positive")
        else:
            print("negative")

multiplication_sign(n1, n2, n3)


