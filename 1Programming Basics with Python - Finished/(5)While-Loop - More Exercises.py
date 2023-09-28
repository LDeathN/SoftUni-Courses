# First Bonus Problem

washer = int(input())
command = input()
available = washer * 750
count = 0
needed = 0
pots = 0
plates = 0
condition = True
while command != "End":
    count += 1
    number = int(command)
    if count % 3 == 0:
        needed += number * 15
        pots += number
    elif count % 3 != 0:
        needed += number * 5
        plates += number
    if needed > available:
        condition = False
        break
    command = input()

if condition:
    left = available - needed
    print("Detergent was enough!")
    print(f"{plates} dishes and {pots} pots were washed.")
    print(f"Leftover detergent {left} ml.")
else:
    more = needed - available
    print(f"Not enough detergent, {more} ml. more necessary!")



# Second Bonus Problem

expected = int(input())
command = input()
count = 0
money_cash = 0
money_card = 0
cash = 0
card = 0
sums = 0
num1 = 0
num2 = 0

while command != "End" and sums < expected:
    count += 1
    price = int(command)

    if count % 2 != 0 and price <= 100:
        money_cash = price
        num1 += money_cash
        sums += money_cash
        cash += 1
        print("Product sold!")
    elif count % 2 == 0 and price >= 10:
        money_card = price
        num2 += money_card
        sums += money_card
        card += 1
        print("Product sold!")
    else:
        print("Error in transaction!")

    if sums >= expected:
        continue
    command = input()

if command == "End":
    print("Failed to collect required money for charity.")

if sums >= expected:
    if cash == 0:
        average_cs = 0
    else:
        average_cs = num1 / cash

    if card == 0:
        average_cc = 0
    else:
        average_cc = num2 / card

    print(f"Average CS: {average_cs:.2f}")
    print(f"Average CC: {average_cc:.2f}")



# Third Bonus Problem

letter = str(input())
word = ""
words = ""
count_c = 0
count_o = 0
count_n = 0
while letter != "End":
    if letter == "A" or letter == "a":
        word += letter
    if letter == "B" or letter == "b":
        word += letter
    if letter == "C":
        word += letter
    if letter == "c":
        count_c += 1
        if count_c > 1:
            word += letter
    if letter == "D" or letter == "d":
        word += letter
    if letter == "E" or letter == "e":
        word += letter
    if letter == "F" or letter == "f":
        word += letter
    if letter == "G" or letter == "g":
        word += letter
    if letter == "H" or letter == "h":
        word += letter
    if letter == "I" or letter == "i":
        word += letter
    if letter == "J" or letter == "j":
        word += letter
    if letter == "K" or letter == "k":
        word += letter
    if letter == "L" or letter == "l":
        word += letter
    if letter == "M" or letter == "m":
        word += letter
    if letter == "N":
        word += letter
    if letter == "n":
        count_n += 1
        if count_n > 1:
            word += letter
    if letter == "O":
        word += letter
    if letter == "o":
        count_o += 1
        if count_o > 1:
            word += letter
    if letter == "P" or letter == "p":
        word += letter
    if letter == "Q" or letter == "q":
        word += letter
    if letter == "R" or letter == "r":
        word += letter
    if letter == "S" or letter == "s":
        word += letter
    if letter == "T" or letter == "t":
        word += letter
    if letter == "U" or letter == "u":
        word += letter
    if letter == "V" or letter == "v":
        word += letter
    if letter == "W" or letter == "w":
        word += letter
    if letter == "X" or letter == "x":
        word += letter
    if letter == "Y" or letter == "y":
        word += letter
    if letter == "Z" or letter == "z":
        word += letter

    if count_c >= 1 and count_o >= 1 and count_n >= 1:
        count_c = 0
        count_o = 0
        count_n = 0
        word = word + " "
        words = word
    letter = str(input())

print(words)



# Fourth Bonus Problem

i = 3
for i in range(3, 101, 3):
    print(i)



# Fifth Bonus Problem

number = int(input())
sum = 0
for i in range(0, number):
    num = int(input())
    sum += num
average = sum / number
print(f"{average:.2f}")