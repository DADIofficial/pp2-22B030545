import re
task1 = re.compile(r'ab*')
result = task1.search(input())
print('exist') if result != None else print(None)