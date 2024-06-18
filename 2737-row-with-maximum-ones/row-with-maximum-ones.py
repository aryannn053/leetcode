class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        result = []
        maximum = 0

        current_index = 0

        for i in range(len(mat)):
            if mat[i].count(1) > maximum:
                maximum = mat[i].count(1)
                current_index = i
        
        return [current_index, maximum]