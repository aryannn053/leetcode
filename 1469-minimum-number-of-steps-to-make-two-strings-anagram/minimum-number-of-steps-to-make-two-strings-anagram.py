class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count = 0
        for i in set(s):
            sCount = s.count(i)
            tCount = t.count(i)
            if sCount == tCount :
                continue
            elif sCount>tCount:
                count+=(sCount-tCount)
            
        return count