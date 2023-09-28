# First Problem

text = str(input())
while text != "end":
    reverse = ""
    for ch in reversed(text):
        reverse += ch
    print(text + " = " + reverse)
    text = input()



# Second Problem

text = str(input()).split(" ")
result = ""
for element in text:
    for i in range(0, len(element)):
        result += element
print(result)



# Third Problem

substring = input()
string = input()
while substring in string:
    string = string.replace(substring, "")
print(string)



# Fourth Problem

forbidden = input().split(", ")
text = input()
for element in forbidden:
    while element in text:
        text = text.replace(element, "*" * len(element))
print(text)



# Fifth Problem

string = input()
digits = ""
letters = ""
other = ""
for ch in string:
    if ch.isdigit():
        digits += ch
    elif ch.isalpha():
        letters += ch
    else:
        other += ch
print(digits)
print(letters)
print(other)