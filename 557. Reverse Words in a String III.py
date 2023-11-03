s = "Let's take LeetCode contest"

str = s.split()
temp = 0

for i in range(len(str)):
    word = list(str[i])
    n = len(word)
    for j in range(int(n/2)):
        temp = word[j]
        word[j] = word[n-j-1]
        word[n - j - 1] = temp
    str[i] = "".join(word)

s = " ".join(str)
print(s)
