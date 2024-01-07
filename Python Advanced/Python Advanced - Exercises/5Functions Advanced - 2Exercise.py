# First Problem

numbers = [int(number) for number in input().split()]
positive = 0
negative = 0
for number in numbers:
    if number > 0:
        positive += number
    else:
        negative += number

print(negative)
print(positive)
if positive > abs(negative):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")



# Second Problem

def kwargs_length(**args):
    return len(args)



# Third Problem

def even_odd(*numbers):
    numbers = list(numbers)
    even_or_odd = numbers.pop()
    if even_or_odd == "even":
        even = []
        for number in numbers:
            if number % 2 == 0:
                even.append(number)
        return even
    elif even_or_odd == "odd":
        odd = []
        for number in numbers:
            if number % 2 != 0:
                odd.append(number)
        return odd



# Fourth Problem

def even_odd_filter(**args):
    dictionary = {}
    for odd_or_even, numbers in args.items():

        if odd_or_even == "odd":
            odd = []
            for number in numbers:
                if number % 2 != 0:
                    odd.append(number)
            dictionary["odd"] = odd

        if odd_or_even == "even":
            even = []
            for number in numbers:
                if number % 2 == 0:
                    even.append(number)
            dictionary["even"] = even
    dictionary = sorted(dictionary.items())
    dictionary = dict(dictionary)
    return dictionary



# Fifth Problem

def concatenate(*args, **kwargs):
    args = list(args)
    string = "".join(args)
    for old, new in kwargs.items():
        if old in string:
            string = string.replace(old, new)
    return string



# Sixth Problem

def func_executor(*args):
    result = ""
    for function in args:
        name, values = function
        value = name(*values)
        result += f"{name.__name__} - {value}" + "\n"
    lines = result.split('\n')
    result = [line for line in lines if line.strip() != '']
    return "\n".join(result)



# Seventh Problem

def grocery_store(**args):
    result = ""
    # Convert Into Dictionary
    values = [_ for _ in args.items()]
    values = dict(values)
    # First Sorting (Alphabetically)
    values = sorted(values.items(), key=lambda x: x)
    values = dict(values)
    # Second Sorting (By Length)
    values = sorted(values.items(), key=lambda x: len(x[0]), reverse=True)
    values = dict(values)
    # Third Sorting (By Value)
    values = sorted(values.items(), key=lambda x: x[1], reverse=True)
    values = dict(values)

    for key, value in values.items():
        result += f"{key}: {value}\n"
    lines = result.split('\n')
    result = [line for line in lines if line.strip() != '']
    return "\n".join(result)



# Eighth Problem

def age_assignment(*args, **kwargs):
    result = ""
    args = list(args)
    kwargs = sorted(kwargs.items(), key=lambda x: x[0])
    kwargs = dict(kwargs)

    for key, value in kwargs.items():
        for element in args:
            if key == element[0]:
                result += f"{element} is {value} years old.\n"

    lines = result.split('\n')
    result = [line for line in lines if line.strip() != '']

    return "\n".join(result)



# Ninth Problem (Me)

def palindrome(word, index):
    first = []
    last = []
    if word[index] == word[len(word) - 1]:
        if len(word) == 1:
            return f"{word} is a palindrome"
        first.append(word[index])
        last.append(word[len(word) - 1])
        if palindrome(word[1:len(word)-1], index) == f"{word[1:len(word)-1]} is a palindrome":
            return f"{word} is a palindrome"
        else:
            return f"{word} is not a palindrome"
    else:
        return f"{word} is not a palindrome"



# Ninth Problem (ChatGPT)

def palindrome1(word, index):
    if index >= len(word) // 2:
        return f"{word} is a palindrome"

    if word[index] == word[len(word) - 1 - index]:
        return palindrome(word, index + 1)
    else:
        return f"{word} is not a palindrome"



# Tenth Problem

def fill_the_box(*args):
    total = 0
    numbers = list(args)
    a, b, c = numbers.pop(0), numbers.pop(0), numbers.pop(0)
    volume = a * b * c
    for number in numbers:
        if number == "Finish":
            break
        total += number
    if volume > total:
        return f"There is free space in the box. You could put {volume - total} more cubes."
    else:
        return f"No more free space! You have {total - volume} more cubes."



# Eleventh Problem

def math_operations(*args, **kwargs):
    result = ""
    args = list(args)
    while args:
        for i in range(4):
            if args:
                number = args.pop(0)
            else:
                break
            if i == 0:
                kwargs["a"] += number
            elif i == 1:
                kwargs["s"] -= number
            elif i == 2 and number != 0.0:
                kwargs["d"] /= number
            elif i == 3:
                kwargs["m"] *= number

    results = sorted(kwargs.items(), key=lambda x: x[0])
    results = dict(results)
    results = sorted(results.items(), key=lambda x: x[1], reverse=True)
    results = dict(results)

    for key, value in results.items():
        result += f"{key}: {value:.1f}\n"
    lines = result.split('\n')
    result = [line for line in lines if line.strip() != '']

    return "\n".join(result)
