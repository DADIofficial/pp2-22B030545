mynums = map(int, input().split())
mynums = list(filter(lambda x: x != 0 and x != 1, mynums))
isprime = list(filter(lambda x: all(map(lambda i: x % i != 0, range(2, int(x ** 0.5) + 1))), mynums))
print(isprime)