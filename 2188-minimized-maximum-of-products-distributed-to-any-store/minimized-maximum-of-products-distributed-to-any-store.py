class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        lo, hi = 1, max(quantities)
        while lo < hi: 
            mid = lo + hi >> 1
            if sum(ceil(qty/mid) for qty in quantities) <= n: hi = mid 
            else: lo = mid + 1
        return lo