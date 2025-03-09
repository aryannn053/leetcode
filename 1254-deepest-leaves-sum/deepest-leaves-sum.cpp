/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left),
 * right(right) {}
 * };
 */
class Solution {
public:
    int ans = 0;
    int max = 0;

    void dfs(TreeNode* root, int cur) {
        if (root == nullptr) return;

        if (root->left == nullptr && root->right == nullptr) {
            if (cur == max) {
                ans += root->val;
            }
            if (cur > max) {
                ans = 0;
                max = cur;
                ans += root->val;
            }
        }
        dfs(root->left, cur+1);
        dfs(root->right, cur+1);
    }
    int deepestLeavesSum(TreeNode* root) {
        dfs(root, 1);
        return ans;
    }
};