class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        new = []
        mod = 10**9 + 7

        for i in range(len(nums)):
            cnt = nums[i]
            new.append(cnt)
            for j in range(i+1, len(nums)):
                cnt += nums[j]
                new.append(cnt)
        
        new.sort()
        return sum(new[left-1:right])%mod