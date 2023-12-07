nums = [1,2,3,4]

n = len(nums)
first = 0
second = 0
index = 0

for i in range(n):
    if first < nums[i]:
        second = first
        first = nums[i]
        index = i
    if (first > nums[i]) and (second < nums[i]):
        second = nums[i]

if (second * 2) <= first:
    print(index)
else:
    print('-1')
