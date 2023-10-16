# '''
#     Algorithm: Greedy BFS
#     Time Complexity: O(n)
#     Space Complexity: O(1)
# '''
# def jump(nums):
#     goal = len(nums) - 1
#     i = lastJumpPos = maxReach = jumps = 0
#     while lastJumpPos < goal:
#         maxReach = max(maxReach, i+nums[i])
#         if i == lastJumpPos:
#             lastJumpPos = maxReach
#             jumps += 1
#         i += 1
#     return jumps


# nums = [2,3,1,1,4]
# res = jump(nums)
# print(res)

# '''
#                         0
#                       /   \
#                     1       2
#                  /  |  \     \
#                 2   3   4     3
#               /     |          \
#             3       4           4
#           /
#         4

# '''
