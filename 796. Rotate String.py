s = "abcde"
goal = "cedab"

if (len(s) == len(goal)) and (s in goal+goal):
    print('true')
else:
    print('false')