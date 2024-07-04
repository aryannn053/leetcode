class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        res = Counter(s)
        for i in range(1, len(s)):
            if res[s[i]] != res[s[i-1]]:
                return False
        
        return True