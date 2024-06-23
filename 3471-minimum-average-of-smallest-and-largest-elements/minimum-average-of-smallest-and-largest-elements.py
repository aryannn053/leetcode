class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        # nums.sort()

        averages = []

        while len(nums) != 0:
            minElement = min(nums)
            maxElement = max(nums)

            averages.append((minElement+maxElement)/2)

            nums.remove(minElement)
            nums.remove(maxElement)
        
        return min(averages)