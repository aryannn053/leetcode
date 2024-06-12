class Solution:
    def sortColors(self, nums):
        count_map = {0: 0, 1: 0, 2: 0}
        
        for num in nums:
            count_map[num] += 1
        
        index = 0
        for color in range(3):
            while count_map[color] > 0:
                nums[index] = color
                index += 1
                count_map[color] -= 1