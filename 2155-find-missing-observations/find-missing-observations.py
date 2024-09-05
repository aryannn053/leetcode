class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        
        sumN = mean * (len(rolls) + n) - sum(rolls)
        if (sumN < n) or (sumN > n * 6):
            return []
            
            
        roundedDownNumbers = sumN // n
        remaining = sumN % n
        
        nList = [roundedDownNumbers for _ in range(n)]
        if roundedDownNumbers == 6:
            return nList
        
        maxAdd = 6 - roundedDownNumbers
        numOfValsToChange = remaining // maxAdd
        remaining = remaining % maxAdd
        for i in range(0,numOfValsToChange):
            nList[i] = 6
        
        if remaining > 0:
            nList[numOfValsToChange] += remaining  

        return nList