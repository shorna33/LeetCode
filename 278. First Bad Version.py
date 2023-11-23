n = 5
bad = 4

left = 1
right = n
mid = 0
while left < right:
    mid = (left + right) // 2
    if isBadVersion(mid):
        right = mid
    else:
        left = mid + 1
print(left)
