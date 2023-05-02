nums = [3,2,3]
n = len(nums)
scol = len(set(nums))
count = [[0 for i in range(2)] for j in range(scol)]
sList = set(nums)
k = 0
for i in sList:
    count[k][0] = i
    for j in range(n):
        if count[k][0] == nums[j]:
            count[k][1] += 1
    k += 1
output = 0
limit = n / 2
if (n % 2) == 1:
    limit = n/2 + 0.5
for i in range(scol):
    if count[i][1] >= limit:
        output = count[i][0]
print(output)
