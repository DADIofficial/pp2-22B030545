def reversed(n):
    k = n.split()
    r = ""
    for i in range(len(k)-1, -1, -1):
        r += k[i] + " "
        return(r)

print(reversed(input()))
