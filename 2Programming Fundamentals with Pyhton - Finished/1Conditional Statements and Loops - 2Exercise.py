# First Problem

name = str(input())
if name != "Johnny":
    print(f"Hello, {name}!")
else:
    print(f"Hello, my love!")



# Second Problem

age = int(input())
if age <= 14:
    print("drink toddy")
elif age <= 18:
    print("drink coke")
elif age <= 21:
    print("drink beer")
elif age > 21:
    print("drink whisky")



# Third Problem

n = int(input())
for i in range(1, n + 1):
    number = int(input())
    if number == 88:
        print("Hello")
    elif number == 86:
        print("How are you?")
    elif number < 88:
        print("GREAT!")
    elif number > 88:
        print("Bye.")



# Fourth Problem

divisor = int(input())
limit = int(input())
maximum = 0
current = 0
for i in range(1, limit + 1):
    if i % divisor == 0:
        current = i
    if current > maximum:
        maximum = current

print(maximum)


# Fifth Problem

n = int(input())
total = 0
for i in range(1, n + 1):
    price = float(input())
    days = int(input())
    amount = int(input())
    if 0.01 <= price <= 100.00 and 1 <= days <= 31 and 1 <= amount <= 2000:
        money = days * price * amount
        total += money
        print(f"The price for the coffee is: ${money:.2f}")

print(f"Total: ${total:.2f}")



# Sixth Problem

n = int(input())
flag = True
for i in range(1, n + 1):
    word = str(input())
    for j in range(0, len(word)):
        if word[j] == "," or word[j] == "." or word[j] == "_":
            flag = False
    if flag:
        print(f"{word} is pure.")
    else:
        print(f"{word} is not pure!")
        flag = True



# Seventh Problem

word = ""
while word != "End":
    word = str(input())
    if word == "End" or word == "SoftUni":
        continue
    for j in range(0, len(word)):
        for h in range(1, 3):
            print(word[j], end="")
    print()



# Eighth Problem

word = ""
coffee = 0
while word != "END":
    word = str(input())
    if word == "END":
        continue
    if word == "coding" or word == "cat" or word == "dog" or word == "movie":
        coffee += 1
    elif word == "CODING" or word == "CAT" or word == "DOG" or word == "MOVIE":
        coffee += 2
    if coffee > 5:
        print("You need extra sleep")
        break
if word == "END":
    print(coffee)



# Ninth Problem

name = ""
while name != "Welcome!":
    name = str(input())
    if name == "Welcome!":
        continue
    if name == "Voldemort":
        print("You must not speak of that name!")
        break
    length = len(name)
    if length < 5:
        print(f"{name} goes to Gryffindor.")
    elif length == 5:
        print(f"{name} goes to Slytherin.")
    elif length == 6:
        print(f"{name} goes to Ravenclaw.")
    elif length > 6:
        print(f"{name} goes to Hufflepuff.")

if name == "Welcome!":
    print("Welcome to Hogwarts.")



# Tenth Problem

word1 = str(input())
word2 = str(input())
count = 0

for j in range(0, len(word2)):
    letter = ord(word2[j])
    if ord(word2[j]) == ord(word1[j]):
        count += 1
        continue

    for i in range(0, 128):
        if i == letter:
            for g in range(0, count):
                if count < len(word2):
                    print(f"{word2[g]}", end="")

            count += 1
            i = chr(i)
            print(f"{i}", end="")
            for h in range(j + 1, len(word1)):
                print(f"{word1[h]}", end="")
            print()



# Eleventh Problem

budget = float(input())
price1 = float(input())
price2 = price1 * 0.75
price3 = price1 * 1.25
eggs = 0
loaves = 0
total = 0
loaf = 0
while budget >= total:
    loaf = price1 + price2 + price3 / 4
    total += loaf
    if total > budget:
        continue
    loaves += 1
    eggs += 3
    if loaves % 3 == 0:
        eggs -= loaves - 2

print(f"You made {loaves} loaves of Easter bread! "
      f"Now you have {eggs} eggs and {(budget - total + loaf):.2f}BGN left.")



# Twelfth Problem

amount = int(input())
days = int(input())
total = 0
money = 0
for day in range(1, days + 1):
    if day % 11 == 0:
        amount += 2
    if day % 2 == 0:
        decoration = 2 * amount
        money += decoration
        points = 5
        total += points
    if day % 3 == 0:
        decoration = 8 * amount
        money += decoration
        points = 13
        total += points
    if day % 5 == 0:
        decoration = 15 * amount
        money += decoration
        points = 17
        total += points
    if day % 5 == 0 and day % 3 == 0:
        total += 30

    if day % 10 == 0:
        total -= 20
        decoration = 5 + 3 + 15
        money += decoration
if days % 10 == 0:
    total -= 30

print(f"Total cost: {money}")
print(f"Total spirit: {total}")