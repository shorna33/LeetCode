n = 43261596
n = bin(n).replace("0b", "")
nums = list(str(n))
m = len(nums)
extra = 32 - m
rev = [0 for i in range(32)]
for i in range(m):
    rev[i] = nums[m-1-i]
if extra > 0:
    for i in range(m, 32):
        rev[i] = 0
revStr = ''.join(map(str, rev))
revInt = int(revStr, 2)
print(revInt)
