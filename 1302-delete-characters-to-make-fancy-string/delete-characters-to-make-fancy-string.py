class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = s[:2]
        for i in range(2,len(s)):
            if s[i] == s[i-1] and s[i] == s[i-2]:
                continue
            else:
                ans += s[i]
        return ans