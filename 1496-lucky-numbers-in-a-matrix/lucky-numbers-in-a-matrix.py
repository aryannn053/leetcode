class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        luck = []

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                arr = [matrix[k][j] for k in range(len(matrix))]

                if max(arr) == matrix[i][j] and min(matrix[i]) == matrix[i][j]:
                    luck.append(matrix[i][j])
        
        return luck