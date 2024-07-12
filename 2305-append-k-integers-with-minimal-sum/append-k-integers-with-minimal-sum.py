class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums=list(set(nums))
        nums.sort()
        s=(k*(k+1))//2
        for i in nums:
            if i<=k:
                k+=1
                s-=i
                s+=k
        return s