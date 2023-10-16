
class Solution:
    def lengthOfLIS(self, nums):
        lis = [1]*len(nums)
        i = len(nums) - 2
        while i >= 0:
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    lis[i] = max(lis[i], 1 + lis[j])
            i -= 1
        return max(lis)
    
nums = [1,5,7,2,4,58,32,21,73]
sol = Solution()
print(sol.lengthOfLIS(nums))