n = 128
n = bin(n).replace("0b", "")
nums = list(str(n))
m = len(nums)
count = 0
for i in range(m):
    if nums[i] == '1':
        count += 1
print(count)
