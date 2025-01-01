class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        l = []
        cur = nums[0].bit_count()
        mn = mx = nums[0]
        for n in nums[1:]:
            bc = n.bit_count()
            if cur == bc:
                mn = min(mn, n)
                mx = max(mx, n)
            else:
                if l and mn < l[-1][1]: return False
                l.append((mn,mx))
                cur = bc
                mn = mx = n
        if l and mn < l[-1][1]: return False
        l.append((mn,mx))

        return True