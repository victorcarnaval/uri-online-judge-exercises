nums = [int(x) for x in input().split()]
nums_clone = nums[:]
k = 0
j = 0

while k < len(nums):
    j = k
    while j < len(nums):
        if nums[k] > nums[j]:
            nums[k], nums[j] = nums[j], nums[k]
        j += 1
    print(nums[k] + "\n" if k == len(nums) else nums[k])
    k += 1

print()

for x in nums_clone:
    print(x)
