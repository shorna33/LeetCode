def fact(n, factorial):
    if n == 0:
        return 1
    else:
        factorial = n * fact(n - 1, factorial)
    return factorial


n = int(input("Input: "))
x = 0
result = 0
if n < 0:
    print("Invalid number")
    exit()
elif n <= 1:
    print("1")
    exit()
else:
    result = fact(n, x)
print("Factorial of " + str(n) + ": " + str(result))
