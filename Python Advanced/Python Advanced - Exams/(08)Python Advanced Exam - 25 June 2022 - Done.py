# First Problem

eggs = [int(x) for x in input().split(", ")]
papers = [int(x) for x in input().split(", ")]
boxes = 0

while eggs and papers:
    egg = eggs.pop(0)
    paper = papers.pop()
    if egg <= 0:
        papers.append(paper)
        continue
    elif egg == 13:
        papers.append(paper)
        papers[0], papers[len(papers) - 1] = papers[len(papers) - 1], papers[0]
        continue
    elif egg + paper <= 50:
        boxes += 1
    elif egg + paper > 50:
        continue

if boxes >= 1:
    print(f"Great! You filled {boxes} boxes.")
else:
    print(f"Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join([str(x) for x in eggs])}")
if papers:
    print(f"Pieces of paper left: {', '.join([str(x) for x in papers])}")



# Second Problem

first, second = input().split(", ")
matrix = [[x for x in input().split(" ")] for _ in range(6)]
traps = []
walls = []
count = 0
rest1 = 0
rest2 = 0
player = None
waiting = None
exit = None

for i in range(6):
    for j in range(6):
        if matrix[i][j] == "E":
            exit = (i, j)
        elif matrix[i][j] == "T":
            traps.append((i, j))
        elif matrix[i][j] == "W":
            walls.append((i, j))

while True:
    command = input()
    command = tuple((int(command[1]), int(command[4])))
    count += 1
    if count % 2 != 0:
        if rest1 == 0:
            player = first
            waiting = second
        else:
            rest1 -= 1
            continue
    elif count % 2 == 0:
        if rest2 == 0:
            player = second
            waiting = first
        else:
            rest2 -= 1
            continue
    if command == exit:
        print(f"{player} found the Exit and wins the game!")
        break
    elif command in traps:
        print(f"{player} is out of the game! The winner is {waiting}.")
        break
    elif command in walls:
        print(f"{player} hits a wall and needs to rest.")
        if player == first:
            rest1 += 1
        elif player == second:
            rest2 += 1



# Third Problem

def shopping_cart(*args):
    cart = {"Soup": [], "Dessert": [], "Pizza": []}
    result = []

    for pair in args:
        if pair == "Stop":
            break
        meal, product = pair
        if product not in cart[meal]:
            if meal == "Soup" and len(cart[meal]) < 3:
                cart[meal].append(product)
            elif meal == "Pizza" and len(cart[meal]) < 4:
                cart[meal].append(product)
            elif meal == "Dessert" and len(cart[meal]) < 2:
                cart[meal].append(product)

    cart = sorted(cart.items(), key=lambda x: x)
    cart = dict(cart)
    cart = sorted(cart.items(), key=lambda x: len(x[1]), reverse=True)
    cart = dict(cart)

    for meal, products in cart.items():
        if not cart["Soup"] and not cart["Dessert"] and not cart["Pizza"]:
            result.append(f"No products in the cart!")
            break
        result.append(f"{meal}:")
        products = sorted(products)
        for item in products:
            result.append(f" - {item}")

    return "\n".join(result)



