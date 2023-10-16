def reverseVowels(s):
    length = len(s)
    vowels = "aeiouAEIOU"
    v = {}
    wordVowels = []
    for i in range(length):
        c = s[i]
        if c in vowels:
            v[i] = c
            wordVowels.append(c)
    
    res = ""
    for i in range(length):
        if i in v:
            res += wordVowels.pop(-1)
        else:
            res += s[i]
    return res


s = "aA"
res = reverseVowels(s)
print(res)