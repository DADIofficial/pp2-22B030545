import re
for i in open('row.txt', encoding="UTF-8"):
    disol = re.findall(r'.+Дисоль.+', i)
    if disol != []:
        print(disol)
    bin = re.findall(r'БИН (\w+)', i)
    if bin != []:
        print(bin)