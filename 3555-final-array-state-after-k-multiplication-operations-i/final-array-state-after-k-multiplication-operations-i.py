class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            j = nums.index(min(nums))
            nums[j] *= multiplier
        
        return nums