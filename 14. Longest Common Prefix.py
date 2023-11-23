strs = ["flower", "flaw", "floght"]

ans = ""
strs.sort()
first = strs[0]
last = strs[-1]
for i in range(min(len(first), len(last))):
    if first[i] != last[i]:
        print(ans)
        exit()
    ans += first[i]
print(ans)
