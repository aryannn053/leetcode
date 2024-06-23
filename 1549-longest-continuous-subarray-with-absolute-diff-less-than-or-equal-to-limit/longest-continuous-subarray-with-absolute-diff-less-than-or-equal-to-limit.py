from sortedcontainers import SortedList

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxLen = 0 
        sl = SortedList()
        p1 = p2 = 0
        while p2 < len(nums):
            sl.add(nums[p2])
            while sl[-1] - sl[0] > limit:
                sl.remove(nums[p1])
                p1 += 1

            maxLen = max(maxLen, len(sl))
            p2 += 1

        return maxLen