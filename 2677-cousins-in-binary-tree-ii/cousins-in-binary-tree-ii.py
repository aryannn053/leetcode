class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []
        def traverse (root, i):
            if root == None: return
            
            if len(arr)> i: arr[i] += root.val
            else: arr.append(root.val)
            
            traverse (root.left, i+1)
            traverse (root.right, i+1)
        traverse(root, 0)
        root.val = 0
        def traverse2 (root, i):
            if root==None: return

            temp = 0
            if len(arr) > i: temp += arr[i]
            if root.left: temp -= root.left.val
            if root.right: temp -= root.right.val

            if root.left: root.left.val = temp
            if root.right: root.right.val = temp

            traverse2(root.left, i+1)
            traverse2(root.right, i+1)

        traverse2(root, 1)
        return root