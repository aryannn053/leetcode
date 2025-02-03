class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans, inc, dec = 1, 1, 1
        for a, b in pairwise(nums):
            if a > b:
                dec += 1
                inc = 1
            elif a < b:
                inc += 1
                dec = 1
            else:
                dec = inc = 1
            ans = max(inc, dec, ans)
        return ans