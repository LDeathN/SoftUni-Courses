# First Problem
import re

participants = input().split(", ")
race_results = {}

while True:
    data = input()
    if data == "end of race":
        break

    pattern = r'[A-Za-z]+'
    name = ''.join(re.findall(pattern, data))

    pattern = r'\d'
    distance = sum(map(int, re.findall(pattern, data)))

    if name in participants:
        if name not in race_results:
            race_results[name] = 0
        race_results[name] += distance

sorted_results = dict(sorted(race_results.items(), key=lambda item: -item[1]))

top_3 = list(sorted_results.keys())[:3]

print(f"1st place: {top_3[0]}")
print(f"2nd place: {top_3[1]}")
print(f"3rd place: {top_3[2]}")



# Second Problem
import re
global_pattern = r"\%[A-Z][a-z]+\%[^\|\$\%\.]*?\<\w+\>[^\|\$\%\.]*?\|[0-9]+\|[\w\-]*?[0-9.]+[0-9](?=\$)"
result = []

while True:
    get_name = input()
    if get_name == 'end of shift':
        break
    if re.search(global_pattern, get_name):
        match = re.search(global_pattern, get_name)
        name = re.search(r"(?<=%)\w+(?=%)", match.group())
        product = re.search(r"(?<=<)\w+(?=>)", match.group())
        qty = re.search(r"(?<=\|)\d+(?=\|)", match.group())
        last = match.group().split('|')
        price = re.search(r"[\d.]+", last[-1])
        result.append([name.group(), product.group(), int(qty.group()), float(price.group())])

total = sum(list(map(lambda x: x[2]*x[3],result)))
for item in result:
    print(f"{item[0]}: {item[1]} - {(item[2] * item[3]):.2f}")
print(f"Total income: {total:.2f}")



# Third Problem
import re

number_of_messages = int(input())
attacked_planets = []
destroyed_planets = []

for message in range(number_of_messages):
    encrypted_message = input()
    decrypted_message = ''

    pattern = r'[starSTAR]'
    matches = len(re.findall(pattern, encrypted_message))

    for character in encrypted_message:
        decrypted_character = chr((ord(character)) - matches)
        decrypted_message += decrypted_character

    planets_pattern = r'.*@(?P<planet>[A-Z][a-z]+)[^\@\-\!\:\>]*:(?P<population>\d+)[^\@\-\!\:\>]*\!(?P<attack_type>A|D)\![^\@\-\!\:\>]*\->(?P<soldiers>\d+).*'
    planet_matches = re.finditer(planets_pattern, decrypted_message)
    for value in planet_matches:
        planet, attack_type = value.group('planet'), value.group('attack_type')

        if attack_type == 'A':
            attacked_planets.append(planet)
        else:
            destroyed_planets.append(planet)

print(f'Attacked planets: {len(attacked_planets)}')
for planet in sorted(attacked_planets):
    print(f'-> {planet}')

print(f'Destroyed planets: {len(destroyed_planets)}')
for planet in sorted(destroyed_planets):
    print(f'-> {planet}')



# Fourth Problem
import re

demons = re.split(", *", input())
demon_book = {}

demon_health_pattern = r'[^\d\+\-*\/\.]'
demon_damage_pattern = r'(?:\+|-)?[0-9]+(?:\.[0-9]+)?'
demon_operators_pattern = r'[*\/]'

for demon in demons:
    demon = demon.strip()
    demon_health = re.findall(demon_health_pattern, demon)
    demon_book[demon] = []
    demon_book[demon].append(sum(ord(match) for match in demon_health))

    demon_damage = re.finditer(demon_damage_pattern, demon)
    operators = re.findall(demon_operators_pattern, demon)
    current_demon_damage = 0

    for value in demon_damage:
        current_demon_damage += float(value.group(0))

    for operator in operators:
        if operator == '*':
            current_demon_damage *= 2
        elif operator == '/':
            current_demon_damage /= 2

    demon_book[demon].append(current_demon_damage)

for demon, qualities in sorted(demon_book.items()):
    print(f'{demon} - {qualities[0]} health, {qualities[1]:.2f} damage')



# Fifth Problem
import re


def extract_title_and_content(html_text):
    # Use regular expressions to extract the title and content
    title_match = re.search(r'<title>(.*?)<\/title>', html_text, re.IGNORECASE | re.DOTALL)
    content_match = re.search(r'<body>(.*?)<\/body>', html_text, re.IGNORECASE | re.DOTALL)

    title = title_match.group(1).strip() if title_match else ""
    content = re.sub(r'<.*?>', '', content_match.group(1), flags=re.DOTALL).strip() if content_match else ""

    return title, content

def main():
    html_text = input()
    title, content = extract_title_and_content(html_text)

    print(f"Title: {title}")
    print(f"Content: {content}")


if __name__ == "__main__":
    main()