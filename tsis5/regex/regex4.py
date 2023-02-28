import re
task4 = re.compile(r'[A-Z]{1}[a-z]+')
result = task4.findall(input())
print(result)