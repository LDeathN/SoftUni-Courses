# First Problem

word = str(input())
words = []
list = ["a", "o", "u", "e", "i"]
for i in range(0, len(word)):
    words.append(word[i])
    letter = word[i]
    if letter.lower() in list:
        words.remove(word[i])
for j in range(0, len(words)):
    print(f"{words[j]}", end="")



# Second Problem

wagon = int(input())
wagons = []
for i in range(1, wagon + 1):
    wagons.append(0)
command = ""
while command != "End":
    command = str(input())
    if command == "End":
        continue
    check = command.split(" ")
    if check[0] == "add":
        wagons[len(wagons) - 1] += int(check[1])
    elif check[0] == "insert":
        wagons[int(check[1])] += int(check[2])
    elif check[0] == "leave":
        wagons[int(check[1])] -= int(check[2])
print(wagons)



# Third Problem

notes = [0] * 10
while True:
    command = str(input())
    if command == "End":
        break
    tokens = command.split("-")
    importance = int(tokens[0]) - 1
    note = tokens[1]
    notes.pop(importance)
    notes.insert(importance, note)
result = [element for element in notes if element != 0]
print(result)



# Fourth Problem

string = str(input()).split(" ")
palindrome = str(input())
result = []
for i in string:
    if i == "".join(reversed(i)):
        result.append(i)
print(result)
print(f"Found palindrome {result.count(palindrome)} times")



# Fifth Problem

names = str(input()).split(", ")
order = sorted(names, key=lambda x: (-len(x), x))
print(order)



# Sixth Problem

numbers = list(map(int, input().split(", ")))
found = map(
    lambda x: x if numbers[x] % 2 == 0 else "no",
    range(len(numbers))
)
even_found = list(filter(lambda a: a != "no", found))
print(even_found)



# Seventh Problem

employee_happiness = list(map(int, input().split(" ")))
happiness_factor = int(input())
happiness = list(map(lambda x: x * happiness_factor, employee_happiness))
filtered = list(filter(lambda x: x >= (sum(happiness) / len(happiness)), happiness))

if len(filtered) >= len(happiness) / 2:
    print(f"Score: {len(filtered)}/{len(happiness)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(happiness)}. Employees are not happy!")

