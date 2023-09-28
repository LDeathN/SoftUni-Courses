# First Problem

n = float(input())

if n == 0:
    print("zero")
elif abs(n) < 1:
    print("small ", end="")
elif abs(n) > 1000000:
    print("large ", end="")

if n > 0:
    print("positive")
elif n < 0:
    print("negative")



# Second Problem

n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1 > n2 and n1 > n3:
    print(n1)
elif n2 > n1 and n2 > n3:
    print(n2)
else:
    print(n3)



# Third Problem

word = str(input())

for i in range(len(word) - 1, -1, -1):
    print(word[i], end="")



# Fourth Problem

n = int(input())
flag = True
for i in range(1, n + 1):
    number = int(input())
    if number % 2 != 0:
        print(f"{number} is odd!")
        flag = False
        break

if flag:
    print("All numbers are even.")



# Fifth Problem

number = 0
while not 1 <= number <= 100:
    number = float(input())

print(f"The number {number} is between 1 and 100")



# Sixth Problem

budget = int(input())
price = ""
while price != "End":
    price = input()
    if price == "End":
        continue
    price = int(price)
    budget -= price
    if budget < 0:
        print("You went in overdraft!")
        break
if budget >= 0:
    print("You bought everything needed.")



# Seventh Problem

n = int(input())

for i in range(1, n):
    for j in range(1, i + 1):
        print("*", end="")
    print()

for i in range(1, n + 1):
    print("*", end="")
print()

for i in range(n - 1, 0, -1):
    for j in range(i, 0, -1):
        print("*", end="")
    print()