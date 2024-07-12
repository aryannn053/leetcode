class Solution:
    def minInsertions(self, s: str) -> int:
        n=len(s)
        dp=[[-1 for j in range(n)] for i in range(n)]
        def solve(i,j):
            if i>=j: return 0
            if dp[i][j]!=-1: return dp[i][j]
            res=min(solve(i+1,j),solve(i,j-1))+1
            if s[i]==s[j]: res=min(res,solve(i+1,j-1))
            dp[i][j]=res
            return res
        return solve(0,n-1)