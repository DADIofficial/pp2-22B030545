string = input()
a = sum([1 for i in string if i.islower()])
b = sum([1 for i in string if i.isupper()])
print("Upper", b)
print("Lower", a)