class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        arr = []
        for i in nums:
            if nums.count(i) == 2:
                arr.append(i)
                nums.remove(i)
            if len(arr) == 2:
                return arr