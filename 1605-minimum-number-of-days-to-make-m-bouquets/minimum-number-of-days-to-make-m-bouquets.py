class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def possible(arr, day, k, m):
            cnt = 0
            nob = 0
            
            for i in range(len(arr)):
                if arr[i] <= day:
                    cnt += 1
                else:
                    nob += cnt//k
                    cnt = 0
            
            nob += cnt//k
            if nob >= m:
                return True
            return False
        if len(bloomDay) < m*k:
            return -1

        low = min(bloomDay)
        high = max(bloomDay)

        while low <= high:
            mid = (low+high)//2
            if possible(bloomDay,mid,k,m):
                high = mid-1
            else:
                low = mid+1

        return low