class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        d = {}
        lastOccurrence = -1
        for i, e in enumerate(nums):
            if e in d:
                lastOccurrence = max(lastOccurrence, d[e])
            d[e] = i
        
        lastOccurrence +=1
        if lastOccurrence == 0:
            return 0
        else:
            return math.ceil(lastOccurrence/3)