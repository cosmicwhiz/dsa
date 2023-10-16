def combinationSum(candidates, target):
    def backtrack(index, arr, s, length):
        if s == target:
            res.append(arr[:])
            return
        elif index == length or s > target:
            return
        
        visited = set()
        for i in range(index, length):
            if candidates[i] in visited:
                continue
            visited.add(candidates[i])
            c = candidates[i]
            arr.append(c)
            backtrack(i+1, arr, s+c, length)
            arr.pop()
    
    res = []
    candidates.sort()
    backtrack(0, [], 0, len(candidates))
    return res

candidates = [10,1,2,7,6,1,5]
target = 8
ans = combinationSum(candidates, target)
print(ans)