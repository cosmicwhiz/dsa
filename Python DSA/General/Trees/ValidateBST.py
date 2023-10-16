class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def isValidBST(root):
        def dfs(root):
            l, r = 1, 1
            try:
                if root.left:
                    if dfs(root.left) >= root.val:
                        l = -1
                if root.right:
                    if dfs(root.right) <= root.val:
                        r = -1
            except:
                return
            if l == -1 or r == -1:
                return 
            return root.val

        if dfs(root) is None:
            return False
        return True



root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)
target = root.right.right.right = TreeNode(8)
