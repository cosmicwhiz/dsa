class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def pathSum(self, root, targetSum):
        res = []
        def traverse(r, s, arr):
            lt, rt = 0, 0
            if r.left:
                arr.append(r.val)
                traverse(r.left, s+r.val, arr)
                arr.pop(-1)
                lt = 1
            if r.right:
                arr.append(r.val)
                traverse(r.right, s+r.val, arr)
                arr.pop(-1)
                rt = 1
            if lt == 0 and rt == 0:
                if s + r.val == targetSum:
                    arr.append(r.val)
                    newarr = []
                    for n in arr:
                        newarr.append(n)
                    res.append(newarr)
                    arr.pop(-1)
            return
        traverse(root, 0, [])
        return res


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
# root.left.left = TreeNode(11)
# root.left.left.left = TreeNode(7)
# root.left.left.right = TreeNode(2)
# root.right.left = TreeNode(13)
# root.right.right = TreeNode(4)
# root.right.right.left = TreeNode(5)
# root.right.right.right = TreeNode(1)


sol = Solution()
res = sol.pathSum(root, 5)
print(res)