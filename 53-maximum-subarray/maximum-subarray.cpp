class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        long long best = -LLONG_MAX; long long sum = 0;
        int n = nums.size();

        for (int k = 0; k < n; k++) {
            sum = max((long long)nums[k], sum + nums[k]);
            best = max(best, sum);
        }

        return best;
    }
};