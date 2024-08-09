class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res = [[rStart, cStart]]
        if rows * cols == 1:
            return res
        
        dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
        n = 0
        step = 0
        r, c = rStart, cStart
        
        while len(res) < rows * cols:
            step += 1
            for i in range(2):
                for _ in range(step):
                    r += dr[n]
                    c += dc[n]
                    if 0 <= r < rows and 0 <= c < cols:
                        res.append([r, c])
                        if len(res) == rows * cols:
                            return res
                n = (n + 1) % 4
        
        return res