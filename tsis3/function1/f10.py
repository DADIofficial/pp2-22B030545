def unique(nums):
    sorted(nums)
    new = [nums[0]]
    for i in range(1, len(nums)):
        if nums[i-1] != nums[i]:
            new += nums[i]
    return new

print(unique(input().split()))