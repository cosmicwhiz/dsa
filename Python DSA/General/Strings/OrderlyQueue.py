def orderlyQueue(s, k):
    wordsFormed = {}
    while s not in wordsFormed:
        l = s[0]
        maxLetter, minLetter = l, l
        inOrder = True
        for c in s[:k]:
            maxLetter = max(maxLetter, c)
            minLetter = min(minLetter, c)
        diff = ord(maxLetter) - ord(minLetter)
        if not diff:
            return s
        wordsFormed[s] = diff
        i = s.index(maxLetter)
        s = s[:i] + s[i+1:] + maxLetter
    print(wordsFormed)
    return sorted(wordsFormed, reverse=True).pop()

s = "dabcbaai"
k = 6
res = orderlyQueue(s, k)
print(res)
