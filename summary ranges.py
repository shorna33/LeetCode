
#
#                     NOT SOLVED
#


nums = [1,3]
n = len(nums)
a, b = 0, 0
output = []
i = 0
j = i + 1
if n == 1:
    output.append(str(nums[0]))
    print(output)
    exit()
while (i < n) and (j < n):
    a = nums[i]
    if (nums[j-1] + 1) == nums[j]:
        b = nums[j]
        j += 1
    else:
        if a == b:
            output.append(str(a))
        elif b > a:
            output.append(str(a) + "->" + str(b))
        i = j
        b = nums[i]
        j += 1
    if j == n:
        a = nums[i]
        if a == b:
            output.append(str(a))
        elif b > a:
            output.append(str(a) + "->" + str(b))

print(output)
