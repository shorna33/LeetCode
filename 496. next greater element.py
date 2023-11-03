nums1 = [2, 4]
nums2 = [1, 2, 3, 4]

flag = 0
val = 0

for i in range(len(nums1)):
    flag = 0
    for j in range(len(nums2)):
        if nums1[i] == nums2[j]:
            k = j
            while k < len(nums2):
                if nums2[k] > nums2[j]:
                    flag = 1
                    val = nums2[k]
                    break
                k += 1
            break
    if flag == 1:
        nums1[i] = val
    else:
        nums1[i] = -1

print(nums1)
