
class Permutations:
    def permute(self, nums):
        def dfs(arr, visited):
            if len(arr) == 1:
                return [arr]
            pm = []
            for i in range(len(arr)):
                if arr[i] not in visited:
                    visited.add(arr[i])
                    newArr = arr[:i]+arr[i+1:]
                    p = dfs(newArr, set())
                    for a in p:
                        p1 = [arr[i]] + a
                        pm.append(p1)
            return pm
        return dfs(nums, set())

p = Permutations()
nums = [1, 2, 1, 1]
res = p.permute(nums)
print(res)