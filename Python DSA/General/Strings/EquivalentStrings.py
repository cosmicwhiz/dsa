def equivalentStrings(word1, word2):
    str1 = ""
    str2 = ""
    w1 = len(word1)
    w2 = len(word2)
    length = min(w1, w2)
    for i in range(length):
        str1 += word1[i]
        str2 += word2[i]
    for j in range(i+1, w1):
        str1 += word1[j]
    for k in range(i+1, w2):
        str2 += word2[k]
    if str1 == str2:
        return True
    return False

word1 = ["ab", "c", "d", "ef"]
word2 = ["a", "bc", "d"]
res = equivalentStrings(word1, word2)
print(res)
        