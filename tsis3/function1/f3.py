def solve(numheads, numlegs):
    rabbits = numlegs/2 - numheads
    chickens = numheads - rabbits
    print("Rabbits:", rabbits)
    print("Chickens:", chickens)

print(solve(int(input()), int(input())))