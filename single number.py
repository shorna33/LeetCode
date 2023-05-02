def exists(stack, s):
    flag = 0
    for i in range(len(stack)):
        if stack[i] == s:
            flag = 1
    return flag


nums = [4,1,2,1,2]
n = len(nums)
stack = []
for i in range(n):
    s = nums[i]
    if exists(stack, s):
        stack.remove(s)
    else:
        stack.append(s)
output = stack[0]
print(output)
