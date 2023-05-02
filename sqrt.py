
#
#                     NOT SOLVED
#


x = 16
if x == 0:
    print('0')
    exit()
first, last = 1, x
while first <= last:
    mid = first + (last - first) / 2
    if (mid * mid) == x:
        print(mid)
        exit()
    if (mid * mid) > x:
        last = mid - 1
    if (mid * mid) < x:
        first = mid + 1
print(last)
