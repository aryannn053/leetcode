
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        stack = [(root, False)]
        res = []
        while stack:

            currentNode, visited = stack.pop()
            if not currentNode:
                continue
            if visited:
                res.append(currentNode.val)
            else:
                stack.append((currentNode, True))
                stack.append((currentNode.right, False))
                stack.append((currentNode.left, False))
        return res
        