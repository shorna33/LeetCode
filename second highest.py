arr = [8, 5, 2, 9, 1, 3, 4, 9, 7]
l = len(arr)
first = second = 0
for i in range(l):
    if first < arr[i]:
        second = first
        first = arr[i]
    elif (second < arr[i]) and (arr[i] != first):
        second = arr[i]

print(first, second)
