class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        cnt = 0

        for i in range(2, len(s)):
            x = s[i-2] + s[i-1] + s[i]

            if len(set(x)) == len(x):
                cnt += 1

        return cnt