nums = [1]
n = len(nums)
output = 0
nums.sort()
if nums[0] != 0:
    print(0)
    exit(0)
for i in range(n):
    if nums[i] != i+1:
        output = i+1
print(output)
