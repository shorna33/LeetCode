nums = [-1, -1, -1, -1, -1, -1]
n = len(nums)
y = n-1
left_sum = nums[0]
right_sum = nums[n-1]
pivot_index = 0
s = 0
for x in range(n):
    s = s + nums[x]
if s == nums[0] or s == nums[y]:
    left_sum = 0
    right_sum = 0
else:
    x = 0
    for i in range(n):
        if (y - x) < 2:
            print(-1)
            exit()
        if left_sum < right_sum:
            left_sum = left_sum + nums[x + 1]
            x = x + 1
            continue
        elif left_sum > right_sum:
            right_sum = right_sum + nums[y - 1]
            y = y - 1
            continue
        elif left_sum == right_sum:
            if (y - x) >2:
                pivot_index = -1
            else:
                pivot_index = x + 1

print(pivot_index)