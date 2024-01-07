# First Problem

queue = [int(x) for x in input().split(",")]
stack = [int(x) for x in input().split(",")]
killed_monsters = 0

while queue and stack:
    armor = queue.pop(0)
    strength = stack.pop()
    if strength >= armor:
        killed_monsters += 1
        strength -= armor
        if strength > 0 and stack:
            stack[len(stack) - 1] += strength
        elif strength > 0:
            stack.append(strength)
    else:
        armor -= strength
        queue.append(armor)

if not queue:
    print("All monsters have been killed!")
if not stack:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {killed_monsters}")



# Second Problem

def is_valid(value, max_value):
    return 0 <= value < max_value


def next_move(command, current_row, current_col):
    if command == 'up' and is_valid(current_row-1, rows):
        return current_row-1, current_col
    if command == 'down' and is_valid(current_row+1, rows):
        return current_row+1, current_col
    if command == 'left' and is_valid(current_col-1, cols):
        return current_row, current_col-1
    if command == 'right' and is_valid(current_col+1, cols):
        return current_row, current_col+1
    return None, None


rows, cols = [int(x) for x in input().split(' ')]
field = []
start_row, start_col = None, None
boy_row, boy_col = None, None
line = ' '

for r in range(rows):
    row = list(input())
    field.append(row)
    if 'B' in row:
        boy_row = r
        boy_col = row.index('B')
        start_row = boy_row
        start_col = boy_col

while line:
    line = input()
    next_row, next_col = next_move(line, boy_row, boy_col)
    if next_row is None or next_col is None:
        print('The delivery is late. Order is canceled.')
        field[start_row][start_col] = ' '
        break
    if field[next_row][next_col] == '*':
        continue
    if field[next_row][next_col] == 'A':
        field[boy_row][boy_col] = '.'
        boy_row, boy_col = next_row, next_col
        field[boy_row][boy_col] = 'P'
        print("Pizza is delivered on time! Next order...")
        field[start_row][start_col] = 'B'
        break
    if field[next_row][next_col] == 'P':
        field[boy_row][boy_col] = '.'
        boy_row, boy_col = next_row, next_col
        field[next_row][next_col] = 'R'
        print("Pizza is collected. 10 minutes for delivery.")
        continue
    if not field[boy_row][boy_col] == 'R':
        field[boy_row][boy_col] = '.'
    boy_row, boy_col = next_row, next_col
    field[boy_row][boy_col] = '.'

for row in field:
    print(''.join(row))



# Third Problem

def accommodate_new_pets(capacity, max_weight, *args):
    result = []
    accommodated_pets = {}

    for pair in args:
        pet, weight = pair
        if capacity <= 0:
            result.append(f"You did not manage to accommodate all pets!")
            break
        if weight > max_weight:
            continue
        if pet not in accommodated_pets:
            accommodated_pets[pet] = 0
        accommodated_pets[pet] += 1
        capacity -= 1
    else:
        result.append(f"All pets are accommodated! Available capacity: {capacity}.")

    result.append("Accommodated pets:")
    [result.append(f"{pet}: {count}") for pet, count in sorted(accommodated_pets.items())]
    return "\n".join(result)



