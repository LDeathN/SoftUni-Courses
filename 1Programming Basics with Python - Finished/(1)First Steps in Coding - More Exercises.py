# First Bonus Problem

a = float(input())
b = float(input())
h = float(input())

area = (a + b) * h / 2
print(f"{area:.2f}")



# Second Bonus Problem

a = float(input())
h = float(input())

area = a * h / 2
print(f"{area:.2f}")



# Third Bonus Problem

c = float(input())
f = (c * 9 / 5) + 32

print(f"{f:.2f}")



# Fourth Bonus Problem

price1 = float(input())
price2 = float(input())
weight1 = int(input())
weight2 = int(input())

sum = price1 * weight1 + price2 * weight2
euro = sum / 1.94

print(f"{euro:.2f}")



# Fifth Bonus Problem

w = float(input())
h = float(input())

w1 = w * 100
h1 = h * 100 - 100

num1 = h1 // 70
num2 = w1 // 120

total = num1 * num2 - 3
print(f"{total:.2f}")



# Sixth Bonus Problem

price1 = float(input())
price2 = float(input())
kilo1 = float(input())
kilo2 = float(input())
kilo3 = int(input())

kilo1p = price1 + (price1 * 0.60)
kilo2p = price2 + (price2 * 0.80)

sum = kilo1p * kilo1 + kilo2p * kilo2 + kilo3 * 7.50
print(f"{sum:.2f}")



# Seventh Bonus Problem

x = float(input())
y = float(input())
h = float(input())

side1 = (x * x) - (1.2 * 2)
side2 = x * x
side34 = (x * y - 1.5 * 1.5) * 2
roof12 = (x * h / 2) * 2
roof34 = x * y * 2

sums = side1 + side34 + side2
sumr = roof12 + roof34
green = sums / 3.4
red = sumr / 4.3

print(f"{green:.2f}")
print(f"{red:.2f}")



# Eighth Bonus Problem

from math import pi
r = float(input())
perimeter = 2 * pi * r
area = r * r * pi

print(f"{area:.2f}")
print(f"{perimeter:.2f}")



# Ninth Bonus Problem

weather = str(input())
if weather == "sunny":
    print("It's warm outside!")
else:
    print("It's cold outside!")



# Tenth Bonus Problem

degrees = float(input())

if 5.00 <= degrees <= 11.90:
    print("Cold")
elif 12.00 <= degrees <= 14.90:
    print("Cool")
elif 15.00 <= degrees <= 20.00:
    print("Mild")
elif 20.10 <= degrees <= 25.90:
    print("Warm")
elif 26.00 <= degrees <= 35.00:
    print("Hot")
else:
    print("unknown")