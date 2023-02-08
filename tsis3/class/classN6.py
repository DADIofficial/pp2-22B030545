def isprime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
nums = input().split()
for i in range(0, len(nums)):
    nums[i] = int(nums[i])
prime_nums = list(filter(lambda x: isprime(x), nums))
print(prime_nums)