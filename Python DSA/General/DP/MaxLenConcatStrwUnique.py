# Maximum Length of a Concatenated String with Unique Characters
from collections import defaultdict


def maxLength(arr):
    l = len(arr)
    concatLen = [0]
    def dp(curStr, i):
        if i == l:
            return len(curStr)
        count = i
        for s in arr[i:]:
            print(s)
            letters = {}
            found = False
            for c in s:
                if c in curStr or c in letters:
                    found = True
                    break
                letters[c] = 1
            if not found:
                print("next")
                concatLen[0] = max(dp(curStr+s, count+1), concatLen[0], len(s))
            count += 1
        return len(curStr)
    
    dp("", 0)
    return concatLen[0]

arr = ["jnfbyktlrqumowxd","mvhgcpxnjzrdei"]
res = maxLength(arr)
print(res)