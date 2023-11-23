n = 4
output = 1
fib = [0 for i in range(n+2)]
fib[0] = 0
fib[1] = 1
for i in range(2, n+2):
    fib[i] = fib[i-1] + fib[i-2]
print(fib)
