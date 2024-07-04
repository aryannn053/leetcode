class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(nums)

        mid = n // 2

        res = 0

        for num in nums:
            res += abs(num - nums[mid])

        return res