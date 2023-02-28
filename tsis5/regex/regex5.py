import re
task5 = re.compile(r'a.+b\Z')
result = task5.search(input())
print('exist') if result != None else print(None)