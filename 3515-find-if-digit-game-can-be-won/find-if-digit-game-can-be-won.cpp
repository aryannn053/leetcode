class Solution {
public:
    bool canAliceWin(vector<int>& nums) {
        int total = accumulate(nums.begin(), nums.end(), 0);
        int singleSum = 0;
        int doubleSum = 0;
    
        for (int num : nums) {
            if (num < 10) {
                singleSum += num;
            } else if (num >= 10 && num < 100) {
                doubleSum += num;
            }
        }
    
        int bobSingle = total - singleSum;
        int bobDouble = total - doubleSum;
    
        return singleSum > bobSingle || doubleSum > bobDouble;
    }
};