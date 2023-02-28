import re
task6 = re.compile(r'[ .,]')
result = task6.sub(":", input())
print(result)