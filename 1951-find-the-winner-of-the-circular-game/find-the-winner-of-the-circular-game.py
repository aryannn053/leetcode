class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums=[i for i in range(1, n+1)]

        ans=0

        while len(nums)!=1:
            ans=(ans+k-1)%len(nums)
            nums.remove(nums[ans])

        return nums[0]