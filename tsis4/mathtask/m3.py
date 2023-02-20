import math
n = int(input("number of sides: "))
length = int(input("the length of a side: "))
print(0.25 * (n**2) * length / math.tan(math.radians(180/n)))