class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(0, len(nums), 2):
            x = []
            for j in range(nums[i]):
                x.append(nums[i+1])
            arr = arr+ x
        
        return arr