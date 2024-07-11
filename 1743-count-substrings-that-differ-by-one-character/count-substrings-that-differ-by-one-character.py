class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        count = 0
        for i in range(len(s)):
            for j in range(len(t)):
                x,y = i,j
                d = 0
                while x < len(s) and y < len(t):
                    if s[x] != t[y]:
                        d += 1
                    if d == 1:
                        count += 1
                    if d == 2:
                        break
                    x += 1
                    y += 1
        return count   