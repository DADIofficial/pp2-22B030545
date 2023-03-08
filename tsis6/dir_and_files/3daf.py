import os
a = input()
if os.path.exists(a):
    print(os.path.split(a)[0])
    print(os.path.split(a)[1])