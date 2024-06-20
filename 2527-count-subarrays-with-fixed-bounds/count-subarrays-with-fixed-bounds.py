class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        left = 0
        pmin = -1
        pmax = -1

        for right in range(len(nums)):
            num = nums[right]
            if num < minK or num > maxK:
                left = right + 1
                pmin = -1
                pmax = -1
            else:
                if num == minK:
                    pmin = right
                if num == maxK:
                    pmax = right
                res += max(0, min(pmin, pmax) - left + 1)

        return res