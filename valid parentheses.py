s = '[({}){}]'
s = list(s)
n = len(s)
opening = ['(', '{', '[']
closing = [')', '}', ']']
stack = [0 for i in range(n)]
flag = 0
top = 0
for i in range(n):
    for j in range(3):
        if s[i] == opening[j]:
            stack[top] = s[i]
            top += 1
            break
        if s[i] == closing[j]:
            if s[i] == ')' and stack[top-1] == '(':
                stack[top-1] = 0
                top -= 1
                break
            if s[i] == '}' and stack[top-1] == '{':
                stack[top-1] = 0
                top -= 1
                break
            if s[i] == ']' and stack[top-1] == '[':
                stack[top-1] = 0
                top -= 1
                break
            flag += 1
            break
for i in range(n):
    if stack[i] != 0:
        flag += 1

if flag > 0:
    print('false')
else:
    print('true')
