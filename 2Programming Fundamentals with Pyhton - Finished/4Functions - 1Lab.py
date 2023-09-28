# First Problem

sequence = str(input())
def absolute(line):
    result = []
    split = line.split(" ")
    for i in range(0, len(split)):
        temp = float(split[i])
        result.append(abs(temp))
    return result
print(absolute(sequence))



# Second Problem

grade = float(input())
def solve(grade):
    if 2.00 <= grade <= 2.99:
        return "Fail"
    elif 3.00 <= grade <= 3.49:
        return "Poor"
    elif 3.50 <= grade <= 4.49:
        return "Good"
    elif 4.50 <= grade <= 5.49:
        return "Very Good"
    elif 5.50 <= grade <= 6.00:
        return "Excellent"
print(solve(grade))



# Third Problem

operator = str(input())
num1 = int(input())
num2 = int(input())
def calculate(operator, num1, num2):
    if operator == "multiply":
        return num1 * num2
    elif operator == "divide":
        return int(num1 / num2)
    elif operator == "add":
        return num1 + num2
    elif operator == "subtract":
        return num1 - num2
print(calculate(operator, num1, num2))



# Fourth Problem

string = input()
n = int(input())
def wtf(string, n):
    repeat_string = lambda a, b: a * b
    result = repeat_string(string, n)
    print(result)
wtf(string, n)



# Fifth Problem

order = str(input())
quantity = int(input())
def check(drink, amount):
    money = 0
    if drink == "coffee":
        money = amount * 1.50
    elif drink == "water":
        money = amount * 1.00
    elif drink == "coke":
        money = amount * 1.40
    elif drink == "snacks":
        money = amount * 2.00
    return f"{money:.2f}"
print(check(order, quantity))



# Sixth Problem

num1 = int(input())
num2 = int(input())
def rectangle_area(n1, n2):
    area = n1 * n2
    return area
print(rectangle_area(num1, num2))



# Seventh Problem

sequence = str(input())
def rounded(line):
    result = []
    split = line.split(" ")
    for i in range(0, len(split)):
        number = round(float(split[i]))
        result.append(number)
    return result
print(rounded(sequence))
