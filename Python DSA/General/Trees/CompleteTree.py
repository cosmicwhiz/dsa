import TreeMaker as tm
from collections import defaultdict

def isCompleteTree(root):
    depth = [0]
    def countTraverse(node, k):
        if node is None:
            depth[0] = max(depth[0], k)
            return
        countTraverse(node.left, k+1)
        countTraverse(node.right, k+1)
    countTraverse(root, 0)
    
    leaf = set()
    ans = [True]
    def traverse(node, k):
        if node is None:
            if k < depth[0]: ans[0] = False
            elif k == depth[0]: leaf.add(None)
            return
        if k == depth[0]:
            if None in leaf: ans[0] = False
            leaf.add(node)
        traverse(node.left, k+1)
        traverse(node.right, k+1)
    traverse(root, 1)
    return ans[0]

root = tm.TreeNode(1)
root.left = tm.TreeNode(2)
root.right = tm.TreeNode(3)
root.left.left = tm.TreeNode(4)
root.left.right = tm.TreeNode(5)
root.right.right = tm.TreeNode(6)

res = isCompleteTree(root)
print(res)