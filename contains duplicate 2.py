
#
#                     NOT SOLVED
#

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9]
k = 3
n = len(nums)
flag = 0
i, j = 0, 1
while (i < n) and (j < n) and (k != 0):
    print(i, j)
    if nums[i] == nums[j]:
        flag = 1
        break
    else:
        j += 1
    if j == i + k + 1:
        i += 1
        j = i + 1
    if j == n and i < n - 1:
        j -= 1
        i += 1
    if i == j:
        break

# for i in range(n - k):
#     for j in range(i + 1, i + k + 1):
#         if nums[i] == nums[j]:
#             flag = 1
if flag == 1:
    print('true')
else:
    print('false')
