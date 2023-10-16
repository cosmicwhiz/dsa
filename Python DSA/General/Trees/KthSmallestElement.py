class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallestElement(root, k):
    values = []
    count = [0]
    def traverse(node):
        if node is None:
            return
        traverse(node.left)
        if count[0] < k:
            values.append(node.val)
            count[0] += 1
        else:
            return
        traverse(node.right)
        
    traverse(root)
    return values[k-1]