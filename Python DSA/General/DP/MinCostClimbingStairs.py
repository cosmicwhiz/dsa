
class Solution:
    def climbStairs(self, cost):
        minCosts = {}
        n = len(cost)-1
        def climb(step):
            if step > n:
                return 0
            if step in minCosts:
                return minCosts[step]
            minCosts[step] = cost[step] + min(climb(step+1), climb(step+2))
            return minCosts[step]
        climb(0)
        return min(minCosts[0], minCosts[1])


sol = Solution()
cost = [1,100,1,1,1,100,1,1,100,1]
minCost = sol.climbStairs(cost)
print("Minimum cost to reach to the top:",minCost)