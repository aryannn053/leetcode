class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        def helper(i, s):
            s += nums[i]
            if i == len(nums)-1:
                return s
            if nums[i+1] > nums[i]:
                ans = helper(i+1, s)  
            else:
                ans = helper(i+1, 0)
            return max(ans, s)
        
        return helper(0, 0)