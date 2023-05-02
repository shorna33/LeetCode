nums = [2,7,11,15]
target = 9
nLen = len(nums)
sum = 0
pos = [0 for i in range(2)]
for i in range(nLen):
    for j in range(i, nLen):
        if i != j:
            sum = nums[i] + nums[j]
            if sum == target:
                pos[0] = i
                pos[1] = j
print(pos)
