from itertools import permutations

def Permutation(a):
    perm = permutations(a)
    for i in (perm):
        for j in i:
            print(j, end = "")
        print()

x = input()
Permutation(x)