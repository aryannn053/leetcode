class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        for i, time in enumerate(timePoints):
            h, m = map(int, time.split(':'))
            timePoints[i] = 1440 if (h == 0 and m == 0) else (h * 60 + m) 
        
        timePoints.sort()
        res = 1440 - (timePoints[-1] - timePoints[0]) 
        for i in range(len(timePoints) - 1):
            res = min(res, timePoints[i + 1] - timePoints[i])
        
        return res