def spy_game(nums):
    n = ""
    for i in nums:
        n += str(i)
    return "007" in n

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))
