from collections import defaultdict
import TreeMaker as tm

def kthLargestSum(root, k):
    levelSums = defaultdict(int)
    maxLvl = [0]
    def traverse(node, lvl):
        if node is None:
            maxLvl[0] = max(maxLvl[0], lvl-1)
            return
        levelSums[lvl] += node.val
        traverse(node.left, lvl+1)
        traverse(node.right, lvl+1)
        return
    traverse(root, 1)
    if maxLvl[0] < k: return -1
    return sorted(list(levelSums.values()), reverse=True)[k-1]


arr = [1,None,3]
root = tm.makeTree(arr, 0, len(arr))
k = 1
res = kthLargestSum(root, k)
print(res)

