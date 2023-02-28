import re
task10 = re.compile(r'[A-Z]')
n = input()
all_ = task10.findall(n)
for i in all_:
    n = task10.sub('_' + i.lower(), n, 1)
print(n)