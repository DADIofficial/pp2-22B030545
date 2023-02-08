def filter_prime(list):
    prime = []
    pro = True
    for i in list:
        for j in range(2, i):
            if j % 2 == 0:
                pro = False
                break
        if pro:
            prime.append(i)
        pro = True
    return(prime)

a = input().split()
for i in range (0, len(a)):
    a[i] = int(a[i])
print(filter_prime(a))