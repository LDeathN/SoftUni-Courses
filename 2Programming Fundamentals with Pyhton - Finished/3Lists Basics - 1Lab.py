# First Problem

first = str(input())
second = str(input())
third = str(input())
zoo = []
zoo.append(third)
zoo.append(second)
zoo.append(first)
print(zoo)



# Second Problem

n = int(input())
courses = []
for i in range(1, n + 1):
    course = str(input())
    courses.append(course)
print(courses)



# Third Problem

n = int(input())
positive = []
negative = []
count = 0
sum = 0
for i in range(1, n + 1):
    number = int(input())
    if number >= 0:
        positive.append(number)
        count += 1
    elif number < 0:
        negative.append(number)
        sum += number

print(positive)
print(negative)
print(f"Count of positives: {count}")
print(f"Sum of negatives: {sum}")



# Fourth Problem

n = int(input())
word = str(input())
sentences = []
true = []
for i in range(1, n + 1):
    sentence = str(input())
    sentences.append((sentence))
    new = sentence.split(word)
    if len(new) > 1:
        true.append((sentence))

print(sentences)
print(true)



# Fifth Problem

n = int(input())
even = []
odd = []
positive = []
negative = []
for i in range(1, n + 1):
    number = int(input())
    if number >= 0:
        positive.append(number)
    elif number < 0:
        negative.append(number)
    if number % 2 == 0:
        even.append(number)
    elif number % 2 != 0:
        odd.append(number)

command = str(input())
if command == "even":
    print(even)
elif command == "odd":
    print(odd)
elif command == "positive":
    print(positive)
elif command == "negative":
    print(negative)