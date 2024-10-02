class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        dict1 = {}
        rank = 1
        for value in sorted(set(arr)):
            if value not in dict1:
                dict1[value] = rank
                rank+=1
            
        return [dict1[v] for v in arr]