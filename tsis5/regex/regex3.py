import re
task3 = re.compile(r'[a-z_]+')
result = task3.findall(input())
print(result)