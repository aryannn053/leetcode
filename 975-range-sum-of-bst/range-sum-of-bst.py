class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0

        if low <= root.val <= high:
            return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
        elif low <= root.val:
            return self.rangeSumBST(root.left, low, high)
        elif root.val <= high:
            return self.rangeSumBST(root.right, low, high)