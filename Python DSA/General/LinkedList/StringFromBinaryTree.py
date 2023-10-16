class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    res = ""

    # def showRes(self):
    #     return self.res

    # def printTree(self, root):
    #     self.res += str(root.val)
    #     if root.left:
    #         self.res += "("
    #         self.printTree(root.left)
    #     else:
    #         if root.right:
    #             self.res += "(()"

    #     if root.right:
    #         self.res += "("
    #         self.printTree(root.right)
    #     self.res += ")"

    def tree2str(self, root):

        def showRes():
            return self.res[:-1]

        def printTree(root):
            self.res += str(root.val)
            if root.left:
                self.res += "("
                printTree(root.left)
            else:
                if root.right:
                    self.res += "()"

            if root.right:
                self.res += "("
                printTree(root.right)
            self.res += ")"

        printTree(root)
        return showRes()


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

sol = Solution()
# sol.printTree(root)
# print(sol.showRes()[:-1])
print(sol.tree2str(root))