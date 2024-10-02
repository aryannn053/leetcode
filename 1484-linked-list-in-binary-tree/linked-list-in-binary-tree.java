class Solution {
    public boolean isSubPath(ListNode head, TreeNode root) {
        if(root==null) return false;
        if(root.val == head.val)
            if(dfs(head, root))
                return true;
                
        return isSubPath(head, root.left) || isSubPath(head, root.right);
    }

    public boolean dfs(ListNode head, TreeNode root) {
        if(head==null) return true;
        if(root==null) return false;
        if(root.val != head.val) return false;
        return dfs(head.next, root.left) || dfs(head.next, root.right);
    }
}