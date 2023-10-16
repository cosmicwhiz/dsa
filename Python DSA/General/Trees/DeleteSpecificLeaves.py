def removeLeafNodes(root, target):
    def traverse(node):
        if node is None:
            return
        left = node.left = traverse(node.left)
        right = node.right = traverse(node.right)

        if left is None and right is None and node.val == target:
            return None
        return node
    return traverse(root)