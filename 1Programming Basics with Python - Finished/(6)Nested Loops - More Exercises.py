# First Bonus Problem

n1 = int(input())
n2 = int(input())
n3 = int(input())

for i in range(1, n1 + 1):
    if i % 2 == 0:
        first = i
        for j in range(2, n2 + 1):
            if j == 2 or j == 3 or j == 5 or j == 7:
                second = j
                for h in range(1, n3 + 1):
                    if h % 2 == 0:
                        third = h
                        print(f"{first} {second} {third}")
                    else:
                        continue
            else:
                continue
    else:
        continue



# Second Bonus Problem

n1 = 0
n2 = 0
n3 = 0
letters = 3

for i in range(0, 3):
    letter = str(input())
    letter = ord(letter)

    if letters == 3:
        n1 = letter
        letters -= 1
    elif letters == 2:
        n2 = letter
        letters -= 1
    elif letters == 1:
        n3 = letter

count = 0
for i in range(n1, n2 + 1):
    if i != n3:
        i = chr(i)
        first = i
    else:
        continue

    for j in range(n1, n2 + 1):
        if j != n3:
            j = chr(j)
            second = j
        else:
            continue

        for h in range(n1, n2 + 1):
            if h != n3:
                h = chr(h)
                third = h
                print(f"{first}{second}{third} ", end="")
                count += 1
            else:
                continue
print(count)



# Third Bonus Problem

number = int(input())
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for h in range(1, 10):
                if i + j == k + h and number % (i + j) == 0:
                    print(f"{i}{j}{k}{h} ", end="")



# Fourth Bonus Problem

start = int(input())
end = int(input())
for i in range(start, end + 1):
    for j in range(start, end + 1):
        for k in range(start, end + 1):
            for h in range(start, end + 1):
                if i > h and ((i % 2 == 0 and h % 2 != 0) or (i % 2 != 0 and h % 2 == 0)) and (j + k) % 2 == 0:
                    print(f"{i}{j}{k}{h} ", end="")



# Fifth Bonus Problem

men = int(input())
women = int(input())
maximum = int(input())
count = 0
for i in range(1, men + 1):
    for j in range(1, women + 1):
        count += 1
        if count <= maximum:
            print(f"({i} <-> {j}) ", end="")
        else:
            break



# Sixth Bonus Problem

last = str(input())
places = int(input())
odd = int(input())
special = 0
number = 0
for i in range(65, ord(last) + 1):
    count = 0
    special += 1
    i = chr(i)
    for j in range(1, places + special):
        count += 1
        if count % 2 != 0:
            for h in range(97, odd + 97):
                number += 1
                h = chr(h)
                print(f"{i}{j}{h}")
        elif count % 2 == 0:
            for h in range(97, odd + 99):
                number += 1
                h = chr(h)
                print(f"{i}{j}{h}")

print(number)



# Seventh Bonus Problem

end1 = int(input())
end2 = int(input())
maximum = int(input())
count = 0
A = 35
B = 64
for i in range(1, end1 + 1):
    for j in range(1, end2 + 1):
        count += 1
        if count <= maximum:
            if A > 55:
                A = 35
            if B > 96:
                B = 64
            symbol1 = chr(A)
            symbol2 = chr(B)
            A += 1
            B += 1
            print(f"{symbol1}{symbol2}{i}{j}{symbol2}{symbol1}|", end="")



# Eighth Bonus Problem

n1 = int(input())
n2 = int(input())
n3 = int(input())
for i in range(1, n1 + 1):
    for j in range(1, n2 + 1):
        for h in range(1, n3 + 1):
            if h % 2 == 0 and i % 2 == 0 and (j == 2 or j == 3 or j == 5 or j == 7):
                print(f"{i} {j} {h}")



# Ninth Bonus Problem

start = int(input())
end = int(input())
magic = int(input())
count = 0
condition = True
for i in range(start, end + 1):
    for j in range(start, end + 1):
        count += 1
        if i + j == magic:
            print(f"Combination N:{count} ({i} + {j} = {magic})")
            condition = False
        if condition == False:
            break
    if condition == False:
        break

if condition:
    print(f"{count} combinations - neither equals {magic}")



# Tenth Bonus Problem

n1 = int(input())
n2 = int(input())
n5 = int(input())
total = int(input())


for i in range(0, n1 + 1):
    for j in range(0, n2 + 1):
        for h in range(0, n5 + 1):
            if i * 1 + j * 2 + h * 5 == total:
                print(f"{i} * 1 lv. + {j} * 2 lv. + {h} * 5 lv. = {total} lv. ")



# Eleventh Bonus Problem

days = int(input())
hours = int(input())
total = 0
for i in range(1, days + 1):
    money = 0
    for j in range(1, hours + 1):
        if i % 2 == 0 and j % 2 != 0:
            money += 2.50
        elif i % 2 != 0 and j % 2 == 0:
            money += 1.25
        else:
            money += 1
    total += money
    print(f"Day: {i} - {money:.2f} leva")

print(f"Total: {total:.2f} leva")



# Twelfth Bonus Problem

n1 = int(input())
count = 0
password = ""
condition = False
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for h in range(1, 10):
                if i < j and k > h and i * j + k * h == n1:
                    count += 1
                    print(f"{i}{j}{k}{h} ", end="")
                    if count == 4:
                        condition = True
                        password = f"{i}{j}{k}{h}"
if condition:
    if count >= 1:
        print()
    print(f"Password: {password}")
else:
    if count >= 1:
        print()
    print("No!")



# Thirteenth Bonus Problem

n1 = int(input())
n2 = int(input())
end1 = int(input())
end2 = int(input())
count1 = 0
count2 = 0
result1 = 0
result2 = 0
for i in range(n1, n1 + end1 + 1):
    for j in range(n2, n2 + end2 + 1):
        for k in range(1, 100):
            if j % k != 0:
                count2 += 1
                if count2 == 97:
                    result2 = j
            if i % k != 0:
                count1 += 1
                if count1 == 97:
                    result1 = i
        if result1 != 0 and result2 != 0 and count1 == 97 and count2 == 97:
             print(f"{result1}{result2}")
        count1 = 0
        count2 = 0



# Fourteenth Bonus Problem

n = int(input())
l = int(input())
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(97, l + 97):
            for h in range(97, l + 97):
                for g in range(1, n + 1):
                    if g > i and g > j:
                        print(f"{i}{j}{chr(k)}{chr(h)}{g} ", end="")