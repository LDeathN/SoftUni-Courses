# First Bonus Problem

i = 1
k = 1
for i in range(1, 11):
    for k in range(1, 11):
        star = "*"
        print(star, end="")
    print()



# Second Bonus Problem

num = int(input())
i = 1
k = 1
for i in range(1, num + 1):
    for k in range(1, num + 1):
        star = "*"
        print(star, end="")
    print()



# Third Bonus Problem

num = int(input())
i = 1
k = 1
for i in range(1, num + 1):
    for k in range(1, num + 1):
        star = "*"
        print(star + " ", end="")
    print()



# Fourth Bonus Problem

num = int(input())
i = 1
k = 1
for i in range(1, num + 1):
    for k in range(1, i + 1):
        dollar = "$"
        print(dollar + " ", end="")
    print()



# Fifth Bonus Problem

num = int(input())
i = 1
k = 1
minus = ""
for j in range(0, num - 2):
    minus += "- "
for i in range(1, num + 1):
    if i == 1 or i == num:
        print("+ " + minus + "+")
    else:
        print("| " + minus + "|")



# Sixth Bonus Problem

n = int(input())
for uprow in range(1, n):
    space = n - uprow
    for i in range(0, space):
        print(" ", end="")
    print("*", end="")
    more = uprow - 1
    for j in range(0, more):
        print(" *", end="")
    print()

print("*", end="")
for middle in range(1, n):
    print(" *", end="")
print()

for lowrow in range(1, n):
    spaces = lowrow
    for k in range(0, lowrow):
        print(" ", end="")
    print("*", end="")
    mores = (n - 1) - lowrow
    for h in range(0, mores):
        print(" *", end="")
    print()



# Seventh Bonus Problem

n = int(input())
for uprow in range(1, n):
    space = n - uprow
    for i in range(0, space):
        print(" ", end="")
    print("*", end="")
    more = uprow - 1
    for j in range(0, more):
        print(" *", end="")
    print()

print("*", end="")
for middle in range(1, n):
    print(" *", end="")
print()

for lowrow in range(1, n):
    spaces = lowrow
    for k in range(0, lowrow):
        print(" ", end="")
    print("*", end="")
    mores = (n - 1) - lowrow
    for h in range(0, mores):
        print(" *", end="")
    print()



# Eighth Bonus Problem

n = int(input())
for i in range(0, n * 2):
    print("*", end="")
for i in range(0, n):
    print(" ", end="")
for i in range(0, n * 2):
    print("*", end="")
print()

for i in range(0, n - 2):
    print("*", end="")
    for j in range(0, n * 2 - 2):
        print("/", end="")
    print("*", end="")

    if i == (n - 1) // 2 - 1:
        for j in range(0, n):
            print("|", end="")
    else:
        for j in range(0, n):
            print(" ", end="")

    print("*", end="")
    for j in range(0, n * 2 - 2):
        print("/", end="")
    print("*", end="")
    print()

for i in range(0, n * 2):
    print("*", end="")
for i in range(0, n):
    print(" ", end="")
for i in range(0, n * 2):
    print("*", end="")



# Ninth Bonus Problem

n = int(input())

for i in range(0, (n + 1) // 2):

    if n % 2 == 0:
        for j in range(i, n // 2 - 1):
            print("-", end="")
        for j in range(0, i + 1):
            print("**", end="")
        for j in range(i, n // 2 - 1):
            print("-", end="")
        print()

    if n % 2 != 0:
        for j in range(i, n // 2):
            print("-", end="")
        for j in range(0, (i + 1) * 2 - 1):
            print("*", end="")
        for j in range(i, n // 2):
            print("-", end="")
        print()

for i in range(0, n // 2):
    print("|", end="")
    for j in range(0, n - 2):
        print("*", end="")
    print("|", end="")
    print()



# Tenth Bonus Problem

n = int(input())
if n == 1:
    print("*")

for i in range(0, (n - 1) // 2):

    if n % 2 == 0:

        for j in range(i, (n - 1) // 2):
            print("-", end="")

        if i == 0:
            print("**", end="")
        else:
            print("*", end="")
            for j in range(0, i):
                print("--", end="")
            print("*", end="")

        for j in range(i, (n - 1) // 2):
            print("-", end="")
        print()

    if n % 2 != 0:

        for j in range(i, (n - 1) // 2):
            print("-", end="")

        if i == 0:
            print("*", end="")
        else:
            print("*", end="")
            for j in range(0, i * 2 - 1):
                print("-", end="")
            print("*", end="")

        for j in range(i, (n - 1) // 2):
            print("-", end="")
        print()


if n != 1:
    print("*", end="")
    for i in range(0, n - 2):
        print("-", end="")
    print("*", end="")
print()


for i in range(0, (n - 1) // 2):

    if n % 2 == 0:

        for j in range(0, i + 1):
            print("-", end="")

        if i == ((n - 1) // 2) - 1:
            print("**", end="")
        else:
            print("*", end="")
            for j in range(i, n // 2 - 2):
                print("--", end="")
            print("*", end="")

        for j in range(0, i + 1):
            print("-", end="")
        print()

    if n % 2 != 0:

        for j in range(0, i + 1):
            print("-", end="")

        if i == ((n - 1) // 2) - 1:
            print("*", end="")
        else:
            print("*", end="")
            for j in range((i + 1) * 2 - 1, n - 3):
                print("-", end="")
            print("*", end="")

        for j in range(0, i + 1):
            print("-", end="")
        print()