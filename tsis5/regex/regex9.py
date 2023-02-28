import re
task9 = re.compile(r'[A-Z]')
n = input()
allup = task9.findall(n)
allword = task9.split(n)
sen = allword[0]
for i in range(len(allup)):
    sen += " " + allup[i] + allword[i+1]
print(sen)