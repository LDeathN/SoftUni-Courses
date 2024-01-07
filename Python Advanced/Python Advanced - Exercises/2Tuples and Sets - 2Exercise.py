# First Problem

number = int(input())
unique = set()
for i in range(number):
    name = input()
    if name not in unique:
        unique.add(name)
for name in unique:
    print(name)



# Second Problem

numbers = list(map(int, input().split(" ")))
first = set()
second = set()
number = numbers.pop(0)
for i in range(number):
    element = int(input())
    if element not in first:
        first.add(element)
number = numbers.pop(0)
for j in range(number):
    element = int(input())
    if element not in second:
        second.add(element)
if (first & second):
    matching = first & second
    for element in matching:
        print(element)



# Third Problem

number = int(input())
unique = set()
for i in range(number):
    chemicals = input().split(" ")
    for chemical in chemicals:
        if chemical not in unique:
            unique.add(chemical)
for element in unique:
    print(element)



# Fourth Problem

text = input()
dictionary = {}
for character in text:
    if character not in dictionary:
        dictionary[character] = 1
    else:
        dictionary[character] += 1
unique = sorted(dictionary)
for character in unique:
    print(f"{character}: {dictionary[character]} time/s")



# Fifth Problem

number = int(input())
check1 = set()
check2 = set()
intersections = []
maximum = 0
for i in range(number):
    line = input().split("-")
    first = line[0].split(",")
    second = line[1].split(",")
    for j in range(int(first[0]), int(first[1]) + 1):
        check1.add(j)
    for h in range(int(second[0]), int(second[1]) + 1):
        check2.add(h)
    result = check1 & check2
    check1 = set()
    check2 = set()
    intersections.append(list(result))
for element in intersections:
    if len(element) > maximum:
        maximum = len(element)
        result = element
print(f"Longest intersection is {result} with length {maximum}")



# Sixth Problem

N = int(input())
odd = set()
even = set()

for i in range(1, N + 1):
    name = input()
    name_ascii_sum = sum(ord(char) for char in name)
    division_result = name_ascii_sum // i

    if division_result % 2 == 1:
        odd.add(division_result)
    else:
        even.add(division_result)

if sum(odd) == sum(even):
    result = ', '.join(map(str, odd | even))
elif sum(odd) > sum(even):
    result = ', '.join(map(str, odd - even))
else:
    result = ', '.join(map(str, even ^ odd))

print(result)