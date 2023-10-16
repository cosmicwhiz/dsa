
class Solution:
    def climbStairs(self, n):
        totalWays = {}
        def climb(step):
            if step == n:
                return 1
            elif step > n:
                return 0
            if step in totalWays:
                # print("Calculated",step,"already")
                return totalWays[step]
            totalWays[step] = climb(step+1) + climb(step+2)
            # print("totalWays["+str(step)+"] = "+str(totalWays[step]))
            return totalWays[step]
        climb(0)
        return totalWays[0]

sol = Solution()
totalSteps = 500
totalWays = sol.climbStairs(totalSteps) #10946
print(totalWays)
