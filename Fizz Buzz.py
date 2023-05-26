n = 5

f = 'Fizz'
b = 'Buzz'
a = 'FizzBuzz'

s = []

for i in range(1, n + 1):
    if ((i % 3) == 0) and ((i % 5) == 0):
        s.append(a)
    elif (i % 3) == 0:
        s.append(f)
    elif (i % 5) == 0:
        s.append(b)
    else:
        s.append(str(i))
print(s)
