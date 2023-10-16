class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxPathSum(root):
    pathSum = [-float("inf")]
    def traverse(node):
        if node  is None:
            return 0 

        left = traverse(node.left)
        right = traverse(node.right)
        leftSum = left + node.val
        rightSum = right + node.val 
        rValue = max(leftSum, rightSum, node.val)
        pathSum[0] = max(pathSum[0], rValue, leftSum+right)
        return rValue
    traverse(root)
    return pathSum[0]

root = TreeNode(-10)
print(root)
root = None
print(root)

root.left = TreeNode(9)
root.right = TreeNode(20)
root.left.left = TreeNode(10)
# # root.left.left.left = TreeNode(7)
# # root.left.left.right = TreeNode(2)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)
# # root.right.right.left = TreeNode(5)
# # root.right.right.right = TreeNode(1)
# res = maxPathSum(root)
# print(res)
