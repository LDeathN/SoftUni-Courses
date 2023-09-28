# First Problem

products = input().split(" ")
dictionary = {}
for element in range(0, len(products), 2):
    key = products[element]
    value = products[element + 1]
    dictionary[key] = int(value)
print(dictionary)



# Second Problem

products = input().split(" ")
dictionary = {}
for i in range(0, len(products), 2):
    key = products[i]
    value = products[i + 1]
    dictionary[key] = int(value)
check = input().split(" ")
for i in check:
    if i in dictionary:
        print(f"We have {dictionary[i]} of {i} left")
    else:
        print(f"Sorry, we don't have {i}")



# Third Problem

dictionary = {}
while True:
    inputs = input()
    if inputs == "statistics":
        break
    product = inputs.split(": ")
    key = product[0]
    value = product[1]
    if key in dictionary:
        dictionary[key] += int(value)
    else:
        dictionary[key] = int(value)

quantity = 0
print("Products in stock:")
for element in dictionary:
    quantity += dictionary[element]
    print(f"- {element}: {dictionary[element]}")
print(f"Total Products: {len(dictionary)}")
print(f"Total Quantity: {quantity}")



# Fourth Problem

dictionary = {}
while True:
    info = input().split(":")
    if len(info) != 3:
        break
    key = info[0] + " - " + info[1]
    value = info[2]
    dictionary[key] = value
result = info[0].split("_")
final = " ".join(result)

for element in dictionary:
    if dictionary[element] == final:
        print(element)



# Fifth Problem

dictionary = {}
letters = input().split(", ")

for element in letters:
    key = element
    value = int(ord(element))
    dictionary[key] = value
print(dictionary)



# Sixth Problem

dictionary = {}
words = input().lower().split(" ")

for element in words:
    lower_element = element.lower()
    if lower_element not in dictionary:
        dictionary[lower_element] = 0
    dictionary[lower_element] += 1

for (key, value) in dictionary.items():
    if value % 2 != 0:
        print(key, end=" ")



# Seventh Problem

dictionary = {}
number = int(input())
for i in range(0, number):
    word = input()
    synonym = input()
    if word not in dictionary:
        dictionary[word] = []
    dictionary[word].append(synonym)
for element in dictionary:
    print(f"{element} - {', '.join(dictionary[element])}")