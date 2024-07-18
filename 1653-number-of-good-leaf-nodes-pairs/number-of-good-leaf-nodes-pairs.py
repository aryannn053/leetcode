# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        count = 0

        def dfs(node):  
            nonlocal count

            if node is None:
                return []
            
            if node.left is None and node.right is None:
                return [0]
            
            left_list = list(filter(lambda dist: dist + 2 <= distance, dfs(node.left)))
            right_list = list(filter(lambda dist: dist + 2 <= distance, dfs(node.right)))

            for dl in left_list:
                for dr in right_list:
                    if dl + dr + 2 <= distance:
                        count += 1
            
            combined = left_list + right_list

            return [dist + 1 for dist in combined]
        
        dfs(root)

        return count   