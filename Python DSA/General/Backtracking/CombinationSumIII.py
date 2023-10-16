def combinationSum(k, n):
    def backtrack(start, arr, arrLen, s, length):
        if arrLen == k and s == n:
            res.append(arr[:])
            return
        elif s > n or start == length:
            return
        
        for i in range(start, length):
            arr.append(i)
            backtrack(i+1, arr, arrLen+1, s+i, length)
            arr.pop()
    
    res = []
    backtrack(1, [], 0, 0, 10)
    return res

k = 3
n = 9
ans = combinationSum(k, n)
print(ans)