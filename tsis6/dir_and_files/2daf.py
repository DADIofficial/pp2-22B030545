import os
a = input()

print(os.access(a, os.F_OK))
print(os.access(a, os.R_OK))
print(os.access(a, os.W_OK))
print(os.access(a, os.X_OK))