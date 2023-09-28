# First Problem

import re

numbers = []
while True:
    line = input()
    if not line:
        break
    matches = re.findall(r'\d+', line)
    numbers.extend(matches)

print(' '.join(numbers))



# Second Problem

import re

input_text = input()
variable_pattern = r'\b_([a-zA-Z0-9]+)\b'
variable_names = re.findall(variable_pattern, input_text)

print(','.join(variable_names))



# Third Problem

import re

def count_word_occurrences(text, target_word):
    pattern = re.compile(rf'\b{re.escape(target_word)}\b', re.IGNORECASE)

    matches = pattern.findall(text)

    return len(matches)

input_text = input()
target_word = input()
result = count_word_occurrences(input_text, target_word)
print(result)



# Fourth Problem

import re

def extract_emails(text):
    pattern = r'((?<=\s)[a-zA-Z0-9]+([-.]\w*)*@[a-zA-Z]+?([.-][a-zA-Z]*)*(\.[a-z]{2,}))'

    matches = re.findall(pattern, text)

    for match in matches:
        print(match[0])

text = input()
extract_emails(text)



# Fifth Problem

import re

pattern = r">>(?P<furniture>[A-Za-z]+)<<(?P<price>\d+(\.\d+)?)!(?P<quantity>\d+)"
total_cost = 0
furniture_list = []

while True:
    line = input()
    if line == "Purchase":
        break

    match = re.match(pattern, line)
    if match:
        furniture = match.group("furniture")
        price = float(match.group("price"))
        quantity = int(match.group("quantity"))

        total_cost += price * quantity
        furniture_list.append(furniture)

print("Bought furniture:")
for furniture in furniture_list:
    print(f"{furniture}")

print(f"Total money spend: {total_cost:.2f}")



# Sixth Problem

import re

def extract_links(text):
    pattern = r'\bwww\.[a-zA-Z0-9-]+\.[a-zA-Z.]+\b'

    matches = re.findall(pattern, text)

    return matches

user_input = []
while True:
    line = input()
    if not line:
        break
    user_input.append(line)

for line_number, line in enumerate(user_input, start=1):
    valid_links = extract_links(line)
    for link in valid_links:
        print(link)