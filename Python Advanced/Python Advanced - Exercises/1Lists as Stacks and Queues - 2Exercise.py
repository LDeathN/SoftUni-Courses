# First Problem

stack = []
numbers = input().split(" ")
for number in numbers:
    stack.append(number)
while stack:
    print(stack.pop(), end=" ")



# Second Problem

stack = []
count = int(input())
for i in range(count):
    command = input().split(" ")
    action = command[0]
    if action == "1":
        number = int(command[1])
        stack.append(number)
    elif action == "2":
        if len(stack) >= 1:
            stack.pop()
    elif action == "3":
        if len(stack) >= 1:
            print(max(stack))
    elif action == "4":
        if len(stack) >= 1:
            print(min(stack))
while stack:
    if len(stack) != 1:
        print(stack.pop(), end=", ")
    else:
        print(stack.pop())



# Third Problem

queue = []
food_in_storage = int(input())
orders = input().split(" ")
for order in orders:
    order = int(order)
    queue.append(order)
print(max(queue))
for i in range(len(queue)):
    if food_in_storage - queue[0] >= 0:
        food_in_storage -= queue[0]
        queue.pop(0)
    else:
        break
if len(queue) == 0:
    print("Orders complete")
else:
    print("Orders left: ", end="")
    while queue:
        print(queue.pop(0), end=" ")



# Fourth Problem

stack = []
flag = True
clothes = input().split(" ")
capacity = int(input())
racks = 1
current_weight = 0
for cloth in clothes:
    cloth = int(cloth)
    stack.append(cloth)
stack.reverse()

while stack:
    for i in range(len(stack)):
        if stack:
            current_weight += stack[0]
            if capacity - current_weight >= 0:
                stack.pop(0)
            elif capacity - current_weight < 0:
                current_weight = 0
                racks += 1
                break
print(racks)



# Fifth Problem

tank = 0
queue = []
result = None
stop = False
petrol_pumps = int(input())

for pump in range(petrol_pumps):
    command = input().split(" ")
    petrol, kilometers = int(command[0]), int(command[1])
    queue.append((petrol, kilometers))

for i in range(len(queue)):
    remove = queue[i]
    if stop:
        break
    count = 0
    for pump in queue:
        tank += pump[0]
        tank -= pump[1]
        if tank < 0:
            queue.insert(len(queue), remove)
            queue.pop(0)
            tank = 0
            break
        count += 1
        if count == len(queue):
            result = i
            stop = True
            break
print(result)



# Sixth Problem

parentheses = input()
open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]
balanced = True
stack = []
for element in parentheses:
    if element in open_list:
        stack.append(element)
    elif element in close_list:
        pos = close_list.index(element)
        if (len(stack) > 0) and (open_list[pos] == stack[len(stack) - 1]):
            stack.pop()
        else:
            balanced = False
if balanced:
    print("YES")
else:
    print("NO")



# Seventh Problem

from datetime import datetime, timedelta

# Function to parse the input and create a dictionary of robots with their processing times
def parse_input(input_line):
    robots = {}
    data = input_line.split(';')
    for item in data:
        name, time = item.split('-')
        robots[name] = int(time)
    return robots

# Function to convert a time string to a datetime object
def parse_time(time_str):
    return datetime.strptime(time_str, '%H:%M:%S')

# Function to convert a datetime object to a formatted time string
def format_time(time_obj):
    return time_obj.strftime('%H:%M:%S')

# Input
robots_input = input()
start_time_input = input()
products = []

# Parse the robots' data
robots = parse_input(robots_input)

current_time = parse_time(start_time_input)

# Create a dictionary to track the next available time for each robot
robot_availability = {robot: parse_time(start_time_input) - timedelta(seconds=1) for robot in robots}

# Simulation
while True:
    product = input()
    if product == "End":
        break

    available_robots = [robot for robot, time in robot_availability.items() if time <= current_time]

    if available_robots:
        robot = available_robots[0]
        current_time += timedelta(seconds=1)
        print(f"{robot} - {product} [{format_time(current_time)}]")
        robot_availability[robot] = current_time + timedelta(seconds=robots[robot] - 1)
    else:
        products.append(product)
        current_time = min(robot_availability.values())

# Printing the queue products
while products:
    available_robots = [robot for robot, time in robot_availability.items() if time <= current_time]

    if available_robots:
        robot = available_robots[0]
        product = products.pop(0)
        current_time += timedelta(seconds=1)
        print(f"{robot} - {product} [{format_time(current_time)}]")
        robot_availability[robot] = current_time + timedelta(seconds=robots[robot] - 1)

    current_time = min(robot_availability.values())



# Eighth Problem

green_light = int(input())
free_window = int(input())
crash = False
passed = 0
cars = []
entered = []
left = 0
while True:
    command = input()
    if command == "END" or crash:
        break
    if command != "green":
        cars.append(command)
    elif command == "green":
        time = green_light
        while cars:
            car = cars.pop(0)
            left = time - len(car)
            if left > 0:
                time -= len(car)
                passed += 1
            elif left == 0:
                passed += 1
                break
            else:
                entered.append(car)
                break
        time = free_window
        while entered:
            time -= abs(left)
            if time >= 0:
                entered.pop(0)
                passed += 1
            else:
                crash = True
                print("A crash happened!")
                print(f"{car} was hit at {car[len(car) + time]}.")
                break
if not crash:
    print("Everyone is safe.")
    print(f"{passed} total cars passed the crossroads.")



# Ninth Problem

price_for_bullet = int(input())
gun_barrel = int(input())
left_bullets = gun_barrel
bullets = input().split(" ")
locks = input().split(" ")
value_of_intelligence = int(input())
stack = [int(number) for number in bullets]
queue = [int(number) for number in locks]
while queue:
    if left_bullets != 0:
        bullet = stack.pop()
        lock = queue[0]
        left_bullets -= 1
        if bullet > lock:
            print("Ping!")
        else:
            print("Bang!")
            queue.pop(0)
        value_of_intelligence -= price_for_bullet
    if left_bullets == 0 and stack != []:
        print("Reloading!")
        left_bullets = gun_barrel
        continue
    elif not stack:
        break


if not queue:
    print(f"{len(stack)} bullets left. Earned ${value_of_intelligence}")
else:
    print(f"Couldn't get through. Locks left: {len(queue)}")



# Tenth Problem

cups_capacity = input().split(" ")
bottles_capacity = input().split(" ")
wasted_liters = 0
cup = 0
stack = [int(number) for number in bottles_capacity]
queue = [int(number) for number in cups_capacity]
while queue:
    if not stack:
        break
    bottle = stack.pop()
    if cup == 0:
        cup = queue[0]
    cup -= bottle
    if cup <= 0:
        queue.pop(0)
        wasted_liters += abs(cup)
        cup = 0
if stack:
    print("Bottles: ", end="")
    for bottle in stack:
        print(bottle, end=" ")
if queue:
    print("Cups: ", end="")
    for cup in queue:
        print(cup, end=" ")
print()
print(f"Wasted litters of water: {wasted_liters}")
