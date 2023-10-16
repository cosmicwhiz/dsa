# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
    

# def countNodes(root):
#     if root is None:
#         return 0
#     def traverse(node, count):
#         if node is None:
#             return count
#         return traverse(node.left, count+1)
#     height = traverse(root, 0)
#     print(height)
#     emptyCount = [0]
#     def traverse2(node, count):
#         if node is None:
#                 return
#         left = traverse2(node.left, count+1)
#         right = traverse2(node.right, count+1)

#         if count == height - 2 and right is None:
#             emptyCount[0] += 1
#             if left is None:
#                 emptyCount[0] += 1
#         return node.val
#     traverse2(root, 0)
#     return 2**height-1-emptyCount[0]


# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# # root.left.right = TreeNode(5)
# # root.right.left = TreeNode(6)
# # root.left.left.left = TreeNode(7)
# # root.left.left.right = TreeNode(2)
# res = countNodes(root)
# print(res)