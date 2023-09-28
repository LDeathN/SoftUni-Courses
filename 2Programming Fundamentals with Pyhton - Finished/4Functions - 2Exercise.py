# First Problem

n1 = int(input())
n2 = int(input())
n3 = int(input())
def smallest_number(n1, n2, n3):
    result = min(n1, n2, n3)
    return result
print(smallest_number(n1, n2, n3))



# Second Problem

n1 = int(input())
n2 = int(input())
n3 = int(input())
def add_and_subtract(n1, n2, n3):

    def sum_numbers():
        sums = n1 + n2
        return sums

    def subtract():
        total = sum_numbers()
        result = total - n3
        return result
    return subtract()

print(add_and_subtract(n1, n2, n3))



# Third Problem

char1 = str(input())
char2 = str(input())
def ASCII(first, second):
    for i in range(ord(first), ord(second) - 1):
        print(f"{chr(i + 1)} ", end="")
ASCII(char1, char2)



# Fourth Problem

num = int(input())
def even_odd_sum(n):
    even_sum = 0
    odd_sum = 0
    new = str(n)
    for i in range(0, len(new)):
        if int(new[i]) % 2 == 0:
            even_sum += int(new[i])
        elif int(new[i]) % 2 != 0:
            odd_sum += int(new[i])
    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")
even_odd_sum(num)



# Fifth Problem

number = str(input())
numbers = number.split(" ")
even = []
def only_even(number):
    return True if int(number) % 2 == 0 else False
result = filter(only_even, numbers)
final = list(result)
for i in range(0, len(final)):
    even.append(int(final[i]))
print(even)



# Sixth Problem

number = str(input())
numbers = number.split(" ")
order = []
for i in range(0, len(numbers)):
    order.append(int(numbers[i]))
def ascending_order(number):
    result = sorted(number, reverse=False)
    return result
print(ascending_order(order))



# Seventh Problem

number = str(input())
numbers = number.split(" ")
order = []
for i in range(0, len(numbers)):
    order.append(int(numbers[i]))
def max_min_sum(number):
    maximum = max(number)
    minimum = min(number)
    total = sum(number)
    print(f"The minimum number is {minimum}")
    print(f"The maximum number is {maximum}")
    print(f"The sum number is: {total}")
max_min_sum(order)



# Eighth Problem

number = str(input())
numbers = number.split(", ")
def palindrome(number):
    for i in range(0, len(number)):
        if list(number[i]) == list(reversed(number[i])):
            print(True)
        else:
            print(False)
palindrome(numbers)



# Ninth Problem

password = str(input())
def valid_or_not(password):
    count1 = 0
    count2 = 0
    if 6 <= len(password) <= 10:
        condition1= True
    else:
        condition1 = False
    for i in range(0, len(password)):
        if 48 <= ord(password[i]) <= 57 or 65 <= ord(password[i]) <= 90 or 97 <= ord(password[i]) <= 122:
           count1 += 1
        if 48 <= ord(password[i]) <= 57:
            count2 += 1
    if count1 == len(password):
        condition2 = True
    else:
        condition2 = False
    if count2 >= 2:
        condition3 = True
    else:
        condition3 = False

    if condition1 and condition2 and condition3:
        print("Password is valid")
    if not condition1:
        print("Password must be between 6 and 10 characters")
    if not condition2:
        print("Password must consist only of letters and digits")
    if not condition3:
        print("Password must have at least 2 digits")
valid_or_not(password)



# Tenth Problem

number = int(input())
def perfect_or_not(number):
    total = 0
    for i in range(2, number + 1):
        if number % i == 0:
            result = number / i
            total += result
    if total == number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")
perfect_or_not(number)



# Eleventh Problem

number = int(input())
def loading_bar(percentage):
    loading = ""
    progress = percentage // 10
    for i in range(1, progress + 1):
        loading += "%"
    for j in range(10 - progress, 0, -1):
        loading +="."
    if progress != 10:
        print(f"{percentage}% [{loading}]")
        print("Still loading...")
    if progress == 10:
        print("100% Complete!")
        print(f"[{loading}]")
loading_bar(number)



# Twelfth Problem

number1 = int(input())
number2 = int(input())
def factorial_division(num1, num2):
    factorial1 = 1
    factorial2 = 1
    for i in range(num1, 0, -1):
        factorial1 *= i
    for j in range(num2, 0, -1):
        factorial2 *= j
    division = factorial1 / factorial2
    print(f"{division:.2f}")
factorial_division(number1, number2)
