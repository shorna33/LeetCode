s = "()(())()(())))"

n = len(s)
count = 0
stack = []
stack.append(-1)
top = 0

for i in range(n):
    if s[i] == '(':
        stack.append(i)
    else:
        stack.pop()
        if len(stack) == 0:
            stack.append(i)
        temp = i - stack[-1]
        if count < temp:
            count = temp


print(count)

