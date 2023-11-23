nums = [3,2,1]

num1 = -1
num2 = -1
num3 = -1

for i in range(len(nums)):
    if num1 < nums[i]:
        if num3 < num2:
            num3 = num2
        if num2 < num1:
            num2 = num1
        num1 = nums[i]
    elif (nums[i] < num1) and (nums[i] > num3) and (nums[i] > num2):
        if num3 < num2:
            num3 = num2
        num2 = nums[i]
    elif (nums[i] < num1) and (nums[i] < num2) and (nums[i] > num3):
        num3 = nums[i]


if num3 < 0:
    print(num1)
else:
    print(num3)
