class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        min_row=m-1
        max_row=0
        min_col=n-1
        max_col=0
        for i in range(m):
            for j in range(n):
                if(grid[i][j]==1):
                    min_row=min(i,min_row)
                    max_row=max(max_row,i)
        for i in range(n):
            for j in range(m):
                if(grid[j][i]==1):
                    min_col=min(min_col,i)
                    max_col=max(max_col,i)
        return (max_row-min_row+1)*(max_col-min_col+1)
        