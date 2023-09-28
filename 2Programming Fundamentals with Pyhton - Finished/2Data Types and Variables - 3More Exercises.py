# First Problem

a = int(input())
b = int(input())
print("Before:")
print(f"a = {a}")
print(f"b = {b}")
c = b
b = a
a = c
print("After:")
print(f"a = {a}")
print(f"b = {b}")



# Second Problem

n = int(input())
count = 0
for i in range(n, 0, -1):
    if n % i == 0:
        count += 1
if count == 2:
    print("True")
else:
    print("False")



# Third Problem

key = int(input())
n = int(input())
word = []
for i in range(1, n + 1):
    str1 = ord(str(input()))
    new1 = str1 + key
    word.append(new1)
for j in range(0, n):
    print(chr(word[(j)]), end="")



# Fourth Problem

n = int(input())
check = []
true = 0
for i in range(1, n + 1):
    random = str(input())
    if random == "(" or random == ")":
        check.append(random)
for j in range(0, len(check)):
    if j % 2 == 0:
        if check[j] == "(":
            true += 1
    if j % 2 != 0:
        if check[j] == ")":
            true += 1
if true == len(check):
    print("BALANCED")
else:
    print("UNBALANCED")
