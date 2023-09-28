# First Problem

import re
names = input()
regex = r'\b[A-Z][a-z]{1,}\s[A-Z][a-z]{1,}\b'
matches = re.findall(regex, names)
print(" ".join(matches))



# Second Problem
import re

input_string = input()

phone_pattern = r'(\+359([ -])2\2\d{3}\2\d{4})\b'
matches = re.findall(phone_pattern, input_string)

valid_phones = [match[0] for match in matches]

print(", ".join(valid_phones))



# Third Problem
import re

input_string = input()

date_pattern = r'\b(?P<day>\d{2})(?P<separator>[.\-/])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})\b'
matches = re.finditer(date_pattern, input_string)

for match in matches:
    day = match.group('day')
    month = match.group('month')
    year = match.group('year')
    print(f"Day: {day}, Month: {month}, Year: {year}")



# Fourth Problem
import re

pattern = r"(?<!\S)-?(?:0|[1-9]\d*)(?:\.\d+)?(?!\S)"
text = input()
matches = re.findall(pattern, text)

for match in matches:
    print(match, end=" ")
