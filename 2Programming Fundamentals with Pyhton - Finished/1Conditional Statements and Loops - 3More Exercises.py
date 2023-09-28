# First Problem

n = (input())
for i in range(9, -1, -1):
    for j in range(0, len(n)):
        if i == int(n[j]):
            print(n[j], end="")



# Second Problem

word = str(input())
list = []
for i in range(0, len(word)):
    if 65 <= ord(word[i])<= 90:
        list.append(i)

print(list)



# Third Problem

animals = str(input())
list = animals.split(", ")

if list[len(list) - 1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    for i in range(0, len(list)):
        if list[i] == "wolf":
            print(f"Oi! Sheep number {len(list) - 1 - i}!"
                  f" You are about to be eaten by a wolf!")



# Fourth Problem

mess = str(input())
count = 0
list = ["water", "sand", "fish", "sun"]
for i in range(0, 4):
    word = mess.lower().split(list[i])
    if len(word) > 1:
        for j in range(1, len(word)):
            count += 1

print(count)
