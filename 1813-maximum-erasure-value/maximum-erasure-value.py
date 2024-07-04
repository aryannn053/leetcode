class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        N = len(nums)

        sett = set()

        summ = 0
        maxx = 0

        while right < N:
            if nums[right] in sett:
                while left < right and nums[left] != nums[right]:
                    summ -= nums[left]
                    sett.remove(nums[left])
                    left += 1
                if nums[left] == nums[right]:
                    left += 1
            else:
                sett.add(nums[right])
                summ += nums[right]
                if summ > maxx:
                    maxx = summ
            right += 1
            
        return maxx