# First Problem

names = input().split(", ")
symbols = ["!", "@" "#", "$", "%", "^", "&", "*"]
for name in names:
    if 3 <= len(name) <= 16:
        flag = True
        result = ""
        for letter in name:
            if (letter.isdigit() or letter.isalpha() or letter.isalnum() or letter == "_" or letter == "-") and letter not in symbols:
                result += letter
            else:
                flag = False
        if flag:
            print(result)



# Second Problem

string = input().split(" ")
first = string[0]
second = string[1]
total = 0
if len(first) > len(second):
    for i in range(0, len(second)):
        total += ord(first[i]) * ord(second[i])
    for i in range(len(second), len(first)):
        total += ord(first[i])
elif len(first) < len(second):
    for i in range(0, len(first)):
        total += ord(second[i]) * ord(first[i])
    for i in range(len(first), len(second)):
        total += ord(second[i])
else:
    for i in range(0, len(first)):
        total += ord(first[i]) * ord(second[i])

print(total)



# Third Problem

file_path = input().split("\\")
for element in file_path:
    if "." in element:
        info = element.split(".")
        file_name = info[0]
        extension = info[1]
print(f"File name: {file_name}")
print(f"File extension: {extension}")



# Fourth Problem

string = input()
for letter in string:
    old = ord(letter)
    index = old + 3
    new = chr(index)
    print(new, end="")



# Fifth Problem

string = input()
for i in range(0, len(string)):
    if string[i] == ":" and string[i + 1] != " ":
        print(f"{string[i]}{string[i + 1]}")



# Sixth Problem

string = input()
result = string[0]
for i in range(1, len(string)):
    if string[i] != string[i - 1]:
        result += string[i]
print(result)



# Seventh Problem

string = input()
radius = 0
result = ""
for letter in string:
    if radius >= 1 and letter != ">" and not letter.isdigit():
        string = string.replace(letter, "", 1)
        radius -= 1
        continue
    elif letter.isdigit():
        radius += int(letter) - 1
        string = string.replace(letter, "", 1)
    else:
        result += letter
        string = string.replace(letter, "", 1)
print(result)



# Eight Problem

string = input().split()
results = []
for element in string:
    if element != "":
        digits = ""
        for i in range(1, len(element) - 1):
            digits += element[i]
        number = int(digits)
        if element[0].isupper():
            divide = ord(element[0]) - 64
            result = number / divide
        elif element[0].islower():
            multiply = ord(element[0]) - 96
            result = number * multiply
        if element[len(element) - 1].isupper():
            subtract = ord(element[len(element) - 1]) - 64
            result -= subtract
        elif element[len(element) - 1].islower():
            add = ord(element[len(element) - 1]) - 96
            result += add
        results.append(result)

total = 0
for i in results:
    total += float(i)
print(f"{total:.2f}")



# Ninth Problem

rage_quit = input().upper()
unique = []
temp = ""
final = ""
for letter in rage_quit:
    if not letter.isdigit() and letter not in unique:
        unique.append(letter)
for i in range(0, len(rage_quit)):
    if not rage_quit[i].isdigit():
        temp += rage_quit[i]
    elif rage_quit[i].isdigit():
        if i == len(rage_quit) - 1:
            multiply = int(rage_quit[i])
            final += temp * multiply
        elif rage_quit[i + 1].isdigit():
            multiply = int(rage_quit[i]) * 10 + int(rage_quit[i + 1])
            final += temp * multiply
            temp = ""
        elif not rage_quit[i + 1].isdigit():
            multiply = int(rage_quit[i])
            final += temp * multiply
            temp = ""
print(f"Unique symbols used: {len(unique)}")
print(final)



# Tenth Problem

string = input().split(",")
for tickets in string:
    ticket = ""
    for symbol in tickets:
        if symbol != " ":
            ticket += symbol
    if len(ticket) == 20:
        if ticket == "@@@@@@@@@@@@@@@@@@@@":
            print(f'ticket "{ticket}" - 10@ Jackpot!')
        elif ticket == "####################":
            print(f'ticket "{ticket}" - 10# Jackpot!')
        elif ticket == "$$$$$$$$$$$$$$$$$$$$":
            print(f'ticket "{ticket}" - 10$ Jackpot!')
        elif ticket == "^^^^^^^^^^^^^^^^^^^^":
            print(f'ticket "{ticket}" - 10^ Jackpot!')
        else:
            max1 = 0
            max2 = 0
            max3 = 0
            max4 = 0
            max5 = 0
            max6 = 0
            max7 = 0
            max8 = 0
            count1 = 0
            count2 = 0
            count3 = 0
            count4 = 0
            count5 = 0
            count6 = 0
            count7 = 0
            count8 = 0
            for i in range(0, 10):
                if ticket[i] == "@":
                    count1 += 1
                    if count1 > max1:
                        max1 = count1
                else:
                    count1 = 0

                if ticket[i] == "#":
                    count2 += 1
                    if count2 > max2:
                        max2 = count2
                else:
                    count2 = 0

                if ticket[i] == "$":
                    count3 += 1
                    if count3 > max3:
                        max3 = count3
                else:
                    count3 = 0

                if ticket[i] == "^":
                    count4 += 1
                    if count4 > max4:
                        max4 = count4
                else:
                    count4 = 0

            for i in range(10, 20):
                if ticket[i] == "@":
                    count5 += 1
                    if count5 > max5:
                        max5 = count5
                else:
                    count5 = 0

                if ticket[i] == "#":
                    count6 += 1
                    if count6 > max6:
                        max6 = count6
                else:
                    count6 = 0

                if ticket[i] == "$":
                    count7 += 1
                    if count7 > max7:
                        max7 = count7
                else:
                    count7 = 0

                if ticket[i] == "^":
                    count8 += 1
                    if count8 > max8:
                        max8 = count8
                else:
                    count8 = 0
            if max1 >= 6 and max5 >= 6:
                if max1 > max5:
                    print(f'ticket "{ticket}" - {max5}@')
                else:
                    print(f'ticket "{ticket}" - {max1}@')
            elif max2 >= 6 and max6 >= 6:
                if max2 > max6:
                    print(f'ticket "{ticket}" - {max6}#')
                else:
                    print(f'ticket "{ticket}" - {max2}#')
            elif max3 >= 6 and max7 >= 6:
                if max3 > max7:
                    print(f'ticket "{ticket}" - {max7}$')
                else:
                    print(f'ticket "{ticket}" - {max3}$')
            elif max4 >= 6 and max8 >= 6:
                if max4 > max8:
                    print(f'ticket "{ticket}" - {max8}^')
                else:
                    print(f'ticket "{ticket}" - {max4}^')
            else:
                print(f'ticket "{ticket}" - no match')
    else:
        print(f"invalid ticket")