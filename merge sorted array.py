nums1 = [0]
m = 0
nums2 = [1]
n = 1
i = m
j = 0
while i < m+n and j < n:
    nums1[i] = nums2[j]
    i += 1
    j += 1
temp = 0
for i in range(m+n):
    for j in range(i+1, m+n):
        if nums1[i] >= nums1[j]:
            temp = nums1[i]
            nums1[i] = nums1[j]
            nums1[j] = temp
print(nums1)