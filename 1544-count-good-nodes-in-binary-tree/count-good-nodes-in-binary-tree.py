# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(root, maxx = float('-inf')):
            if not root: return
            if root.val >= maxx: 
                maxx = root.val
                self.res+=1
            dfs(root.left, maxx)
            dfs(root.right, maxx)
        dfs(root)
        return self.res