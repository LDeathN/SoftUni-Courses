# First Problem

string = input()
while True:
    command = input()
    if command == "Done":
        break
    command = command.split(" ")
    action = command[0]
    if action == "TakeOdd":
        raw_password = ""
        for i in range(0, len(string)):
            if i % 2 != 0:
                raw_password += string[i]
        string = raw_password
        print(raw_password)
    elif action == "Cut":
        index = int(command[1])
        length = int(command[2])
        substring = string[index:index + length]
        string = string.replace(substring, "", 1)
        print(string)
    elif action == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in string:
            string = string.replace(substring, substitute)
            print(string)
        else:
            print(f"Nothing to replace!")
print(f"Your password is: {string}")



# Second Problem

import re

n = int(input())
for _ in range(n):
    barcode = input()
    pattern = r"(@#+)([A-Z][A-Za-z0-9]{4,}[A-Z])(@#+)"
    match = re.match(pattern, barcode)

    if match:
        product_group = ''.join(re.findall(r'\d', match.group(2))) or "00"
        print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")



# Third Problem

heroes = int(input())
info = {}
for i in range(heroes):
    hero = input().split(" ")
    name = hero[0]
    hp = int(hero[1])
    mp = int(hero[2])
    info[name] = {"hp": hp, "mp": mp}
while True:
    command = input()
    if command == "End":
        break
    command = command.split(" - ")
    action = command[0]
    if action == "CastSpell":
        hero = command[1]
        mp_needed = int(command[2])
        spell = command[3]
        if info[hero]["mp"] - mp_needed >= 0:
            mp_left = info[hero]["mp"] - mp_needed
            info[hero]["mp"] = info[hero]["mp"] - mp_needed
            print(f"{hero} has successfully cast {spell} and now has {mp_left} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell}!")
    elif action == "TakeDamage":
        hero = command[1]
        damage = int(command[2])
        attacker = command[3]
        if info[hero]["hp"] - damage > 0:
            hp_left = info[hero]["hp"] - damage
            info[hero]["hp"] = info[hero]["hp"] - damage
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {hp_left} HP left!")
        else:
            del info[hero]
            print(f"{hero} has been killed by {attacker}!")
    elif action == "Recharge":
        hero = command[1]
        mp_healed = int(command[2])
        if info[hero]["mp"] + mp_healed > 200:
            recharged = 200 - info[hero]["mp"]
            info[hero]["mp"] = 200
        else:
            info[hero]["mp"] = info[hero]["mp"] + mp_healed
            recharged = mp_healed
        print(f"{hero} recharged for {recharged} MP!")
    elif action == "Heal":
        hero = command[1]
        hp_healed = int(command[2])
        if info[hero]["hp"] + hp_healed > 100:
            healed = 100 - info[hero]["hp"]
            info[hero]["hp"] = 100
        else:
            info[hero]["hp"] = info[hero]["hp"] + hp_healed
            healed = hp_healed
        print(f"{hero} healed for {healed} HP!")
for hero, stats in info.items():
    hp = stats["hp"]
    mp = stats["mp"]
    print(f"{hero}")
    print(f"  HP: {hp}")
    print(f"  MP: {mp}")