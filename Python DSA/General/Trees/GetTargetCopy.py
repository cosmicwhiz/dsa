class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def getTargetCopy(original, cloned, target):
        def bst(root):
            if root == target:
                return root.val
            if root.left:
                left = bst(root.left)
                if left is not None:
                    return left
            if root.right:
                right = bst(root.right)
                if right is not None:
                    return right
        val = bst(original)
        
        def bst2(root):
            if root.val == val:
                return root
            if root.left:
                left = bst2(root.left)
                if left:
                    return left
            if root.right:
                right = bst2(root.right)
                if right:
                    return right

        return bst2(cloned)
