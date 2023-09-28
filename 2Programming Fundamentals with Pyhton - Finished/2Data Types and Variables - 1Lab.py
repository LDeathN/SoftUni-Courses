# First Problem

name1 = str(input())
name2 = str(input())
delimiter = str(input())
print(f"{name1}{delimiter}{name2}")



# Second Problem

meters = int(input())
kilometers = meters / 1000
print(f"{kilometers:.2f}")



# Third Problem

pounds = int(input())
dollars = pounds * 1.31
print(f"{dollars:.3f}")



# Fourth Problem

from math import floor
centuries = int(input())
years = centuries * 100
days = floor(years * 365.2422)
hours = days * 24
minutes = hours * 60
print(f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")



# Fifth Problem

n = input()
for i in range(1, int(n) + 1):
    sum = 0
    print(f"{i} -> ", end = "")
    i = str(i)
    for j in range(0, len(i)):
        sum += int(i[j])
    if sum == 5 or sum == 7 or sum == 11:
        print("True")
    else:
        print("False")



# Sixth Problem

import sys
year = int(input())
times = 0
for i in range(year, sys.maxsize):
    times += 1
    correct = 0
    i_str = str(i)
    for j in range(10):
        count = 0
        for h in range(0, len(i_str)):
            if int(i_str[h]) == j:
                count += 1

        if count == 1:
            correct += 1

    if correct == len(i_str) and times > 1:
        print(i)
        break
