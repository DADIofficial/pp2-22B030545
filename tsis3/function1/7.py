def has_33(nums):
    n = 0    for i in nums:
        if i == 3:
            n += 1        else:
            n = 0        if n == 2:
            return(True)
    return(False)

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))
