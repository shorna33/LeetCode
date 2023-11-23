num = 8128

sum = 0
divs = []
for i in range(1, round(num/2)+1):
    if (num % i) == 0:
        sum = sum + i

if sum == num:
    print('true')
else:
    print('false')
