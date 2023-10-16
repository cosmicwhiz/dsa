# from collections import defaultdict

# '''
#     Time Complexity: O(nlogn)
#     Space Complexity: O(1)
# '''
# def majorityElement(nums):
#     nums.sort()
#     return nums[len(nums)//2]

# '''
#     Time Complexity: O(n)
#     Space Complexity: O(n)
# '''
# def majorityElement_alt1(nums):
#     d = defaultdict(int)
#     half = len(nums) // 2
#     for n in nums:
#         d[n] += 1
#         if d[n] > half:
#             return n


# def majorityElement_alt2(nums):
#     pass

# nums = [1,1,1,3,3,3,1,1,1]
# res = majorityElement(nums)
# print(res)