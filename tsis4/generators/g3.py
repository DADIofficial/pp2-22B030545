def gen_div3and4(n):
    for i in range (1, n):
        if i % 12 == 0:
            yield i

a = gen_div3and4(int(input()))
for i in a:
    print(i)
