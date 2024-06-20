class Solution:
    def maxDistance(self, a: List[int], m: int) -> int:
        def valid(a,t,m):
            c=1
            prev=a[0]
            for i in range(1,len(a)):
                if (a[i]-prev>=t):
                    c += 1
                    prev = a[i]
            
            if (c >= m):
                return 1
            return 0
        
        a.sort()
        l = 1
        r = max(a)-min(a)
        ans=-1

        while (l <= r):
            mid = (l+r)//2

            if (valid(a,mid,m)):
                ans = mid
                l = mid+1
            else:
                r = mid-1
        
        return ans