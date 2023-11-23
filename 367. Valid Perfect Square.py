num = 256

if num == 1:
    print('true')
    exit(0)
else:
    low = 0
    high = num
    while low < high:
        mid = (low + high) // 2
        if mid * mid == num:
            print('true')
            exit(0)
        elif mid * mid > num:
            high = mid
        else:
            low = mid + 1
    print('false')
