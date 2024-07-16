class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return Counter(nums).most_common()[0][0]