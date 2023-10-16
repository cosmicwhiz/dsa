def minDeletionSize(strs):
    length = len(strs[0])
    deleted = 0
    i = 0
    while i < length:
        maxOrd = ord(strs[0][i])
        for w in strs[1:]:
            asciiVal = ord(w[i])
            if asciiVal < maxOrd:
                deleted += 1
                break
            else:
                maxOrd = asciiVal
        i += 1
    return deleted


strs = ["rrjk","furt","guzm"]
res = minDeletionSize(strs)
print(res)