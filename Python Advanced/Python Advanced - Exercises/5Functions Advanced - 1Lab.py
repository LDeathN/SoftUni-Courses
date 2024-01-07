# First Problem

def multiply(*sequence):
    result = 1
    sequence = list(sequence)
    while sequence:
        result = result * sequence.pop()
    return result



# Second Problem

def get_info(name, town, age):
    return f"This is {name} from {town} and he is {age} years old"



# Third Problem

def sorting_cheeses(**cheeses):
    result = ""
    cheese = {}
    cheese_values = sorted([value for value in cheeses.items()])
    for name, value in cheese_values:
        cheese[name] = len(value)
    cheese = sorted(cheese.items(), key=lambda x: x[1], reverse=True)
    cheese = dict(cheese)

    for name in cheese:
        result += f"{name}\n"
        for name1, values in cheese_values:
            if name == name1:
                for value in sorted(values, reverse=True):
                    result += f"{value}\n"
    lines = result.split('\n')
    result = [line for line in lines if line.strip() != '']
    return "\n".join(result)



# Fourth Problem

def rectangle(length, width):
    length = length
    width = width
    if length == int(length) and width == int(width):

        def area(a, b):
            rectangle_area = a * b
            return f"Rectangle area: {rectangle_area}"

        def perimeter(a, b):
            rectangle_perimeter = 2 * (a + b)
            return f"Rectangle perimeter: {rectangle_perimeter}"

        r1 = area(length, width)
        r2 = perimeter(length, width)
        return r1 + "\n" + r2

    else:
        return 'Enter valid values!'



# Fifth Problem

def operate(symbol, *args):
    symbol = symbol
    numbers = list(args)
    if symbol == "+":
        result = 0
        for number in numbers:
            result += number
    elif symbol == "-":
        result = numbers[0]
        for i in range(1, len(numbers)):
            result -= numbers[i]
    elif symbol == "*":
        result = 1
        for number in numbers:
            result *= number
    elif symbol == "/":
        result = numbers[0]
        for i in range(1, len(numbers)):
            if numbers[i] != 0:
                result /= numbers[i]
    return result



# Sixth Problem

def recursive_power(number, power):
    return number ** power