class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = len(s)

        for i in range(len(s)):
            ans = s[i]
            for j in range(i+1, len(s)):
                ans += s[j]

                if ans == ans[::-1]:
                    cnt += 1
        
        return cnt