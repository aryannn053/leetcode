class Solution:
    def maxScore(self, s: str) -> int:
        l = 1
        score = []

        while 1:
            if l == len(s):
                break
            score.append(s[:l].count('0') + s[l:].count('1'))
            l += 1
        return max(score)