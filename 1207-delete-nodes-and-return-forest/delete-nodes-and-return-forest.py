# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        self.ans = []
        def explorer(root):
            if root is None:
                return False

            L=explorer(root.left)
            if L == True:
                root.left = None
            
            R=explorer(root.right)     
            if R==True:
                root.right =None

            if root.val in to_delete:
                if root.left is not None:
                    self.ans.append(root.left)
                if root.right is not None:
                    self.ans.append(root.right)
                return True
            return False
        m=explorer(root)
        if m == False:
            self.ans.append(root)

        return self.ans