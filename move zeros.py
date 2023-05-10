nums = [1, 0, 1]
n = len(nums)
if n == 1:
    print(nums)
    exit(0)
i = 0
j = 1
while (i < j) and (j < n):
    if nums[i] == 0 and nums[j] != 0:
        nums[i] = nums[j]
        nums[j] = 0
        i += 1
        j += 1
        continue
    if nums[i] == 0 and nums[j] == 0 and j < n:
        j += 1
        continue
    i += 1
    j += 1
print(nums)
