# First Problem

contests = {}
submissions = {}

# Collect contest data
while True:
    command = input()
    if command == "end of contests":
        break
    contest, password = command.split(":")
    contests[contest] = password

# Process submissions and calculate points
while True:
    command = input()
    if command == "end of submissions":
        break
    contest, password, username, points = command.split("=>")
    points = int(points)

    if contest in contests and contests[contest] == password:
        if username not in submissions:
            submissions[username] = {}
        if contest not in submissions[username] or points > submissions[username][contest]:
            submissions[username][contest] = points

# Calculate total points for each user
user_total_points = {}
for user, contests_data in submissions.items():
    total_points = sum(contests_data.values())
    user_total_points[user] = total_points

# Find the best user
best_user = max(user_total_points, key=user_total_points.get)
best_user_points = user_total_points[best_user]

# Sort users by name
sorted_users = sorted(submissions.keys())

# Print the best user
print(f"Best candidate is {best_user} with total {best_user_points} points.")
print(f"Ranking:")
# Print all students ordered by their names and contest points
for user in sorted_users:
    print(user)
    contests_data = submissions[user]
    sorted_contests = sorted(contests_data.keys(), key=lambda x: (-contests_data[x], x))
    for contest in sorted_contests:
        points = contests_data[contest]
        print(f"#  {contest} -> {points}")



# Second Problem

courses = {}
total_points = {}
total_points_per_name = {}

while True:
    string = input()
    if string == "no more time":
        break

    name, contest, points = string.split(" -> ")
    points = int(points)

    if contest not in courses:
        courses[contest] = {}

    if name not in courses[contest] or points > courses[contest][name]:
        courses[contest][name] = points

    if name not in total_points:
        total_points[name] = 0

    total_points[name] += points

    if name not in total_points_per_name:
        total_points_per_name[name] = 0

# Calculate and accumulate total points per name
for contest in courses:
    for name, points in courses[contest].items():
        total_points_per_name[name] += points

# Sort participants within each contest correctly
for contest in courses:
    participants = courses[contest]
    sorted_participants = sorted(
        participants.items(), key=lambda x: (-x[1], x[0])
    )  # Sort primarily by points (descending), then by name (ascending)
    courses[contest] = sorted_participants

# Print contest results
for contest in courses:
    participants = courses[contest]
    print(f"{contest}: {len(participants)} participants")

    for i, (name, points) in enumerate(participants, start=1):
        print(f"{i}. {name} <::> {points}")

# Print individual statistics including total points
print("Individual standings:")
sorted_users = sorted(total_points_per_name.items(), key=lambda x: (-x[1], x[0]))
for i, (name, points) in enumerate(sorted_users, start=1):
    print(f"{i}. {name} -> {points}")



# Third Problem

players = {}

while True:
    command = input()
    if command == "Season end":
        break

    if "vs" in command:
        player1, player2 = command.split(" vs ")
        if player1 in players and player2 in players:
            common_positions = set(players[player1].keys()) & set(players[player2].keys())
            if common_positions:
                total_skill_player1 = sum(players[player1][position] for position in common_positions)
                total_skill_player2 = sum(players[player2][position] for position in common_positions)
                if total_skill_player1 > total_skill_player2:
                    del players[player2]
                elif total_skill_player1 < total_skill_player2:
                    del players[player1]
    else:
        player, position, skill = command.split(" -> ")
        skill = int(skill)
        if player not in players:
            players[player] = {}
        if position not in players[player] or skill > players[player][position]:
            players[player][position] = skill

players = sorted(players.items(), key=lambda x: (-sum(x[1].values()), x[0]))

for player, positions in players:
    total_skill = sum(positions.values())
    print(f"{player}: {total_skill} skill")
    sorted_positions = sorted(positions.items(), key=lambda x: (-x[1], x[0]))
    for position, skill in sorted_positions:
        print(f"- {position} <::> {skill}")



# Fourth Problem

dwarfs = {}

while True:
    line = input()
    if line == "Once upon a time":
        break

    dwarf_name, dwarf_hat_color, dwarf_physics = line.split(" <:> ")
    dwarf_physics = int(dwarf_physics)

    if dwarf_name not in dwarfs:
        dwarfs[dwarf_name] = {}
    if dwarf_hat_color not in dwarfs[dwarf_name] or dwarf_physics > dwarfs[dwarf_name][dwarf_hat_color]:
        dwarfs[dwarf_name][dwarf_hat_color] = dwarf_physics

# Flatten the dwarf data with the highest physics for each name/color combination
flat_dwarfs = []
for name, colors in dwarfs.items():
    for color, physics in colors.items():
        flat_dwarfs.append((name, color, physics))

# Sort dwarfs by physics in descending order and then by the count of dwarfs with the same hat color in descending order
sorted_dwarfs = sorted(flat_dwarfs, key=lambda x: (-x[2], -sum(1 for dwarf in flat_dwarfs if dwarf[1] == x[1])))

# Print the sorted dwarfs
for dwarf in sorted_dwarfs:
    print(f"({dwarf[1]}) {dwarf[0]} <-> {dwarf[2]}")



# Fifth Problem

dragons_by_type = {}

# Initialize default values
default_damage = 45
default_health = 250
default_armor = 10

# Read the number of dragons
n = int(input())

# Process input data
for _ in range(n):
    data = input().split()
    dragon_type, dragon_name, damage, health, armor = data[0], data[1], data[2], data[3], data[4]

    # Convert damage, health, and armor to integers, or use default values if "null"
    damage = int(damage) if damage != "null" else default_damage
    health = int(health) if health != "null" else default_health
    armor = int(armor) if armor != "null" else default_armor

    # Update the dictionary with dragon data
    if dragon_type not in dragons_by_type:
        dragons_by_type[dragon_type] = []

    # Check if a dragon with the same name already exists
    existing_dragon = None
    for dragon in dragons_by_type[dragon_type]:
        if dragon["name"] == dragon_name:
            existing_dragon = dragon
            break

    if existing_dragon:
        # Update the existing dragon's stats
        existing_dragon["damage"] = damage
        existing_dragon["health"] = health
        existing_dragon["armor"] = armor
    else:
        # Add a new dragon to the list
        new_dragon = {
            "name": dragon_name,
            "damage": damage,
            "health": health,
            "armor": armor,
        }
        dragons_by_type[dragon_type].append(new_dragon)

# Sort the dragons alphabetically by name within each type
for dragon_type, dragon_list in dragons_by_type.items():
    dragons_by_type[dragon_type] = sorted(dragon_list, key=lambda x: x["name"])

# Print the aggregated data
for dragon_type, dragon_list in dragons_by_type.items():
    total_damage = sum(dragon["damage"] for dragon in dragon_list)
    total_health = sum(dragon["health"] for dragon in dragon_list)
    total_armor = sum(dragon["armor"] for dragon in dragon_list)
    num_dragons = len(dragon_list)

    average_damage = total_damage / num_dragons
    average_health = total_health / num_dragons
    average_armor = total_armor / num_dragons

    print(f"{dragon_type}::({average_damage:.2f}/{average_health:.2f}/{average_armor:.2f})")

    for dragon in dragon_list:
        print(f"-{dragon['name']} -> damage: {dragon['damage']}, health: {dragon['health']}, armor: {dragon['armor']}")
