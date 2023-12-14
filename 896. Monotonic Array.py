nums = [1]

n = len(nums)
flag = 0

if n == 1:
    print('true')
    exit()

if (nums[0] >= nums[-1]) and (nums[0] >= nums[1]):
    for i in range(n-1):
        if nums[i] < nums[i+1]:
            flag = 1
            break
elif (nums[0] <= nums[-1]) and (nums[0] <= nums[1]):
    for i in range(n-1):
        if nums[i] > nums[i+1]:
            flag = 1
            break
else:
    flag = 1

if flag == 1:
    print('false')
else:
    print('true')
