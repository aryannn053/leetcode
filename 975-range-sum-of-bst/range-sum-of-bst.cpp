/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int rangeSumBST(TreeNode* root, int low, int high) {
        vector<int> res;

        preorder(root, low, high, res);

        return accumulate(res.begin(), res.end(), 0);
    }
private:
    void preorder(TreeNode* root, int low, int high, vector<int>& res) {
        if (root == nullptr) return;

        if (low <= root->val && root->val <= high) {
            res.push_back(root->val);
        }
        preorder(root->left, low, high, res);
        preorder(root->right, low, high, res);
    }
};