# First Problem

vowels = [x for x in input().split(" ")]
consonants = [x for x in input().split(" ")]
words = ["rose", "tulip", "lotus", "daffodil"]
result = {"rose": "", "tulip": "", "lotus": "", "daffodil": ""}
stop =True
while vowels and consonants and stop:
    vowel = vowels.pop(0)
    consonant = consonants.pop()
    for word in words:
        if vowel in word and vowel not in result[word]:
            result[word] += vowel * len([x for x in word if x == vowel])
        if consonant in word and consonant not in result[word]:
            result[word] += consonant * len([x for x in word if x == consonant])
        if len(result[word]) >= len(word):
            print(f"Word found: {word}")
            stop = False
            break
if stop:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")



# Second Problem

matrix = [[x for x in input().split(" ")] for _ in range(8)]
count = 0
white = None
black = None
letters = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h"}
for i in range(8):
    for j in range(8):
        if matrix[i][j] == "w":
            white = (i, j)
        elif matrix[i][j] == "b":
            black = (i, j)

while True:
    count += 1
    if count % 2 != 0:
        player = white
        x, y = player
        if (x - 1, y - 1) == black:
            for key, value in letters.items():
                if y - 1 == key:
                    letter = value
            print(f"Game over! White win, capture on {letter}{9 - x}.")
            break
        elif (x - 1, y + 1) == black:
            for key, value in letters.items():
                if y + 1 == key:
                    letter = value
            print(f"Game over! White win, capture on {letter}{9 - x}.")
            break
        elif (x - 1, y) == (0, y):
            for key, value in letters.items():
                if y == key:
                    letter = value
            print(f"Game over! White pawn is promoted to a queen at {letter}8.")
            break
        else:
            white = (x - 1, y)

    elif count % 2 == 0:
        player = black
        x, y = player
        if (x + 1, y - 1) == white:
            for key, value in letters.items():
                if y - 1 == key:
                    letter = value
            print(f"Game over! Black win, capture on {letter}{7 - x}.")
            break
        elif (x + 1, y + 1) == white:
            for key, value in letters.items():
                if y + 1 == key:
                    letter = value
            print(f"Game over! Black win, capture on {letter}{7 - x}.")
            break
        elif (x + 1, y) == (7, y):
            for key, value in letters.items():
                if y == key:
                    letter = value
            print(f"Game over! Black pawn is promoted to a queen at {letter}1.")
            break
        else:
            black = (x + 1, y)



# Third Problem

def start_spring(**kwargs):
    result = []
    spring = {}
    for key, value in kwargs.items():
        if value not in spring:
            spring[value] = []
        spring[value].append(key)

    spring = sorted(spring.items(), key=lambda x: x)
    spring = dict(spring)
    spring = sorted(spring.items(), key=lambda x: len(x[1]), reverse=True)
    spring = dict(spring)

    for key, values in spring.items():
        if spring[key]:
            result.append(f"{key}:")
            values = sorted(values, key=lambda x: x)
            for value in values:
                result.append(f"-{value}")

    return "\n".join(result)


