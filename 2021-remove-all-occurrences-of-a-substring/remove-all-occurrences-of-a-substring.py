class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        if part not in s:
            return s
        else:
            i = s.index(part)
            if s[i:len(part)+i] == part:
                return self.removeOccurrences(s[:i] + s[len(part)+i:], part)