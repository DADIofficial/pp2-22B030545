import re
task7 = re.compile(r'_.')
n = input()
all_ = task7.findall(n)
for i in all_:
    n = task7.sub(i[1].upper(), n, 1)
print(n)