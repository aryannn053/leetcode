class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maximum = 0
        for i in nums:
            maximum |= i
        @cache
        def helper(i, total):
            if i == len(nums):
                return 1 if total == maximum else 0
            return helper(i + 1, total | nums[i]) + helper(i + 1, total)
        
        return helper(0, 0)