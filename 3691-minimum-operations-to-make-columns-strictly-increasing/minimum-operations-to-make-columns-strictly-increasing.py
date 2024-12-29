class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        cur = None
        n = len(grid)
        cnt = 0

        for j in range(len(grid[0])):
            for i in range(n):
                if cur == None:
                    cur = grid[i][j]
                else:
                    if grid[i][j] <= cur:
                        old = grid[i][j]
                        grid[i][j] = cur+1
                        cur = grid[i][j]
                        cnt += grid[i][j]-old
                    else:
                        cur = grid[i][j]
            cur = None

        return cnt