products = {}
def maxProduct(nums):
    maxP = {}
    minP = {}

    def findProduct(i):
        if i == len(nums)-1:
            if nums[i] > 0:
                maxP[i] = nums[i]
                minP[i] = -nums[i]
            elif nums[i] < 0:
                maxP[i] = -nums[i]
                minP[i] = nums[i]
            else:
                maxP[i] = 1
                minP[i] = -1
            return
        findProduct(i+1)
        if nums[i] > 0:
            maxP[i] = nums[i] * maxP[i+1]
            minP[i] = min(nums[i], nums[i] * minP[i+1])
        elif nums[i] < 0:
            maxP[i] = nums[i] * minP[i+1]
            minP[i] = nums[i] * maxP[i+1]
        else:
            maxP[i] = 1
            minP[i] = -1
        return 
    findProduct(0)
    print(maxP)
    return max(maxP.values())


nums = [2,3,-2,4,2]
print(maxProduct(nums))
