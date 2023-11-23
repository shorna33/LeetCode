nums1 = [1,2]
nums2 = [3,4]

nums = (nums1 + nums2)
nums.sort()
median = 0
n = len(nums)
if n % 2 == 0:
    median = (nums[int(n/2)] + nums[int(n/2)-1]) / 2
else:
    median = nums[int(n/2)]

print(median)
