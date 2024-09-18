class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]

        nums.sort(key=lambda x: x*10, reverse=True)

        for x in nums:
            print(x*10)

        if nums[0] == '0':
            return '0'

        return ''.join(nums)