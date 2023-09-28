# First Problem

total = 0
while True:
    line = input()
    if not line.isalpha():
        price = float(line)
        if price > 0:
            total += price
        elif price < 0:
            print(f"Invalid price!")
    else:
        break
if total > 0:
    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total:.2f}$")
    taxes = total * 0.20
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    if line == "special":
        final = total + taxes
        final = final - final * 0.10
    else:
        final = total + taxes
    print(f"Total price: {final:.2f}$")
else:
    print(f"Invalid order!")



# Second Problem

waiting = int(input())
lift = input().split(" ")
count = 0
flag = False
while True:
    for i in range(0, len(lift)):
        if waiting == 0:
            flag = True
            break
        if int(lift[i]) <= 4:
            empty = 4 - int(lift[i])
            if waiting - empty >= 0:
                waiting = waiting - empty
                lift[i] = 4
            elif waiting - empty < 0:
                lift[i] = waiting + int(lift[i])
                waiting = 0
                print(f"The lift has empty spots!")
    if waiting == 0:
        flag = True
        break
    for element in lift:
        if element == 4:
            count += 1
            if count == len(lift):
                print(f"There isn't enough space! {waiting} people in a queue!")
                flag = True
    if flag:
        break
for element in range(0, len(lift)):
    if element != len(lift) - 1:
        print(lift[element], end=" ")
    else:
        print(lift[element])



# Third Problem

sequence = input().split(" ")
count = 0
while True:
    guess = input()
    empty = []
    if guess == "end":
        break
    first, second = guess.split(" ")
    first = int(first)
    second = int(second)
    if sequence == empty:
        continue
    if 0 <= first <= len(sequence) - 1 and 0 <= second <= len(sequence) - 1 and first != second:
        count += 1
        if sequence[first] == sequence[second]:
            print(f"Congrats! You have found matching elements - {sequence[first]}!")
            if first < second:
                sequence.pop(first)
                sequence.pop(second - 1)
            elif first > second:
                sequence.pop(second)
                sequence.pop(first - 1)
        elif sequence[first] != sequence[second]:
            print("Try again!")
    else:
        print(f"Invalid input! Adding additional elements to the board")
        count += 1
        key = str(-count) + "a"
        sequence.insert(len(sequence) // 2, key)
        sequence.insert(len(sequence) // 2 + 1, key)

if sequence == empty:
    print(f"You have won in {count} turns!")
else:
    print(f"Sorry you lose :(")
    for element in sequence:
        print(element, end=" ")

