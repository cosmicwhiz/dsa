class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def makeTree(arr, i, n):
    root = None
    # Base case for recursion 
    if i < n and arr[i] != None:
        root = TreeNode(arr[i]) 
        # insert left child 
        root.left = makeTree(arr, 2 * i + 1, n)
        # insert right child 
        root.right = makeTree(arr, 2 * i + 2, n)
          
    return root
