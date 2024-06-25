class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        arr = []
        node = root
        def inorder(node):
            if node.left:
                inorder(node.left)
            arr.append(node.val)
            if node.right:
                inorder(node.right)
        inorder(node)
        def addsum(node):
            ind = arr.index(node.val)
            leng = len(arr)
            sums = sum(arr[ind:leng])
            print(sums)
            node.val = sums
            if node.left:
                addsum(node.left)
            if node.right:
                addsum(node.right)
        addsum(node)
        return node