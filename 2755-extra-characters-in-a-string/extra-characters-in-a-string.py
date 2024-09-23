class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = [0] * (n+1)
        teststr = ""
        for i, c in enumerate(s):
            teststr += c
            newdp = dp[i] + 1
            for d in dictionary:
                backtrack = len(d)
                if teststr.endswith(d):
                    newdp = min(newdp, dp[i-backtrack+1])
            dp[i+1] = newdp
        
        return dp[-1]