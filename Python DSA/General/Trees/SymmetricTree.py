import TreeMaker as tm

def isSymmetric(root):
    left, right = [], []
    def lt(node):
        if node != None:
            lc = lt(node.left)
            rc = lt(node.right)
            left.append(node.val)
            if lc + rc == 2:
                left[-2] = left[-3] = 1e3
            return 1 + lc + rc
        else:
            left.append(None)
            return 1

    def rt(node):
        if node != None:
            rc = rt(node.right)
            lc = rt(node.left)
            right.append(node.val)
            if lc + rc == 2:
                right[-2] = right[-3] = 1e3
            return 1 + lc + rc
        else:
            right.append(None)
            return 1
    
    sideNodes = lt(root.left)
    if sideNodes != rt(root.right):
        return False
    for i in range(sideNodes):
        if left[i] != right[i]: return False
    return True



nodes = [9,-42,-42,None,76,76,None,None,13,None,13]
root = tm.makeTree(nodes, 0, len(nodes))

res = isSymmetric(root)
print(res)