sentence = "The quick brown fox jumped over the lazy dog"

sentence = sentence.split()

n = len(sentence)
ma = 'maa'
output = ''
temp = ''
vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

for i in range(n):
    if sentence[i][0] not in vowel:
        temp = sentence[i][1:len(sentence[i])]
        temp = temp + sentence[i][0]
        temp = temp + ma
        if i < n-1:
            output = output + temp + ' '
        else:
            output = output + temp
    else:
        temp = sentence[i]
        temp = temp + ma
        if i < n - 1:
            output = output + temp + ' '
        else:
            output = output + temp
    temp = ''
    ma += 'a'

print(output)

