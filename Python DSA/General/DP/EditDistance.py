def minOperations(word1, word2):
    w1 = len(word1)
    w2 = len(word2)
    cache = [[float("inf")]*(w2+1) for i in range(w1+1)]

    for j in range(min(w1, w2)+1):
        cache[-1][j] = w2-j
        cache[j][-1] = w1-j

    for i in range(w2+1, w1):
        cache[i][-1] = w1-i

    for i in range(w1+1, w2):
        cache[-1][i] = w2-i
        
    for i in range(w1-1, -1, -1):
        for j in range(w2-1, -1, -1):
            if word1[i] == word2[j]:
                cache[i][j] = cache[i+1][j+1]
            else:
                cache[i][j] = 1 + min(cache[i+1][j+1], cache[i][j+1], cache[i+1][j])
    return cache[0][0]

word1 = "intention"
word2 = "execution"
res = minOperations(word1, word2)
print(res)