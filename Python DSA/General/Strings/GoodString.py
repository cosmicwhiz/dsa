def makeGood(s):
    i = 0
    while i < len(s) - 1:
        if abs(ord(s[i]) - ord(s[i+1])) == 32:
            s = s[:i] + s[i+2:]
            i -= 1
            if i < 0:
                i = 0
            continue
        i += 1
    return s

s = "AbcDdCBaeF"
res = makeGood(s)
print(res)