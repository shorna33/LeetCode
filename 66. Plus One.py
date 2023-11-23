digits = [9]
n = len(digits)
sum = 0
for i in range(n):
    sum = sum + (digits[i] * 10 ** (n-1-i))
sum += 1
output = [int(i) for i in str(sum)]
print(output)
