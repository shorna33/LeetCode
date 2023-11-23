x = 7
if x == 0:
    print('0')
    exit()
first = 1
last = x
while first <= last:
    mid = first + round((last - first) / 2)
    print(mid)
    if (mid * mid) == x:
        print(mid)
        exit()
    if (mid * mid) > x:
        last = mid - 1
    if (mid * mid) < x:
        first = mid + 1
print(last)
