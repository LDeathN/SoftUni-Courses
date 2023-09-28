# First Problem

number = int(input())
for i in range(number):
    string = input()
    string_name = string.split("@")[1].split("|")[0]
    string_age = string.split("#")[1].split("*")[0]
    print(f"{string_name} is {string_age} years old.")



# Second Problem

start = ord(input())
end = ord(input())
string = input()
total = 0
for symbol in string:
    if start < ord(symbol) < end:
        total += ord(symbol)
print(total)



# Third Problem

key = input().split(" ")
original = []
for i in key:
    original.append(i)
treasures = []
while True:
    key = []
    for i in original:
        key.append(i)
    treasure = input()
    if treasure == "find":
        break
    found = ""
    for i in range(0, len(treasure)):
        number = key[0]
        symbol = chr(ord(treasure[i]) - int(number))
        found += symbol
        key.remove(number)
        key.append(number)
    treasures.append(found)
for element in treasures:
    material = element.split("&")[1]
    coordinates = element.split("<")[1].split(">")[0]
    print(f"Found {material} at {coordinates}")



# Fourth Problem

result = ""
message = input().split(" | ")
for word in message:
    letters = word.split(" ")
    for letter in letters:
        if letter == ".-":
            result += "A"
        elif letter == "-...":
            result += "B"
        elif letter == "-.-.":
            result += "C"
        elif letter == "-..":
            result += "D"
        elif letter == ".":
            result += "E"
        elif letter == "..-.":
            result += "F"
        elif letter == "--.":
            result += "G"
        elif letter == "....":
            result += "H"
        elif letter == "..":
            result += "I"
        elif letter == ".---":
            result += "J"
        elif letter == "-.-":
            result += "K"
        elif letter == ".-..":
            result += "L"
        elif letter == "--":
            result += "M"
        elif letter == "-.":
            result += "N"
        elif letter == "---":
            result += "O"
        elif letter == ".--.":
            result += "P"
        elif letter == "--.-":
            result += "Q"
        elif letter == ".-.":
            result += "R"
        elif letter == "...":
            result += "S"
        elif letter == "-":
            result += "T"
        elif letter == "..-":
            result += "U"
        elif letter == "...-":
            result += "V"
        elif letter == ".--":
            result += "W"
        elif letter == "-..-":
            result += "X"
        elif letter == "-.--":
            result += "Y"
        elif letter == "--..":
            result += "Z"
    result += " "
print(result)



# Fifth Problem

print("<h1>")
title = input()
print("    " + title)
print("</h1>")
print("<article>")
article = input()
print("    " + article)
print("</article>")
while True:
    content = input()
    if content == "end of comments":
        break
    print("<div>")
    print("    " + content)
    print("</div>")
