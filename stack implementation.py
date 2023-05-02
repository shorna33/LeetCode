def push(stack, top, data):
    if top == len(stack):
        print('Stack Overflow')
        return
    top = top + 1
    stack[top] = data
    return stack, top


def pop(stack, top):
    if top == -1:
        print('Stack underflow')
        return
    stack[top] = 0
    top = top - 1
    return stack, top


stack = [0 for i in range(5)]
top = -1
stack, top = push(stack, top, 1)
stack, top = push(stack, top, 3)
stack, top = push(stack, top, 9)
stack, top = push(stack, top, 8)
stack, top = push(stack, top, 5)
print(stack)
stack, top = pop(stack, top)
print(stack)
stack, top = pop(stack, top)
print(stack)

##################    or    ##################
# stack = [1, 4, 3, 5]
# print(stack)
# stack.pop()
# print(stack)
# stack.append(8)
# print(stack)

