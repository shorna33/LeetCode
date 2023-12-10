nums = [4, 2, 5, 7]

n = len(nums)
temp = 0

for i in range(n):
    if ((i % 2 == 0 or i == 0) and (nums[i] % 2 == 0 or nums[i] == 0)) or (i % 2 == 1 and nums[i] % 2 == 1):
        continue
    else:
        if (i % 2 == 0) or i == 0:
            j = i + 1
            while j < n:
                if j % 2 == 1 and (nums[j] % 2 == 0 or nums[j] == 0):
                    temp = nums[j]
                    nums[j] = nums[i]
                    nums[i] = temp
                    break
                j += 1
        else:
            j = i + 1
            while j < n:
                if (j % 2 == 0 or j == 0) and nums[j] % 2 == 1:
                    temp = nums[j]
                    nums[j] = nums[i]
                    nums[i] = temp
                    break
                j += 1

print(nums)
