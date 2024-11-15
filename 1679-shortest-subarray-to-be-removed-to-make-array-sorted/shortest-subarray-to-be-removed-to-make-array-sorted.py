class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n=len(arr)
        s=0
        while s<n-1 and arr[s]<=arr[s+1]:
            s+=1
        if s==n-1:return 0
        r=n-1
        while r>0 and arr[r]>=arr[r-1]:
            r-=1
        ans=min(n-1-s,r)
        i,j=0,r
        while i<=s and j<n:
            if arr[i]<=arr[j]:
                ans=min(ans,j-i-1)
                i+=1
            else:
                j+=1
        return ans