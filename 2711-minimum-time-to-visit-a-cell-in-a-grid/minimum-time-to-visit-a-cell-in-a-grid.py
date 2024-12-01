class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] <= 1 or grid[1][0] <= 1: 
            m, n = len(grid), len(grid[0])
            pq = [(0, 0, 0)]
            dist = defaultdict(lambda : inf, {(0, 0) : 0})
            while pq: 
                x, i, j = heappop(pq)
                if (i, j) == (m-1, n-1): return x 
                for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j): 
                    if 0 <= ii < m and 0 <= jj < n: 
                        xx = x + 1 + max(0, (grid[ii][jj] - x)//2*2) 
                        if dist[ii, jj] > xx: 
                            heappush(pq, (xx, ii, jj))
                            dist[ii, jj] = xx 
        return -1 