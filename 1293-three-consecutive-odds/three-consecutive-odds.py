class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cons = 0
        maximum = 0
        
        for i in range(len(arr)):
            if arr[i] % 2 != 0:
                cons += 1
                maximum = max(maximum, cons)
            else:
                maximum = max(maximum, cons)
                cons = 0
            
            if maximum == 3:
                return True
        
        return False