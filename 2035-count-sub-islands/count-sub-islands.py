class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m,n=len(grid2),len(grid2[0])
        ans=0
        for i in range(m):
            for j in range(n):
                if grid2[i][j]:
                    f=1
                    q=[(i,j)]
                    while q:
                        ni,nj=q.pop(0)
                        if grid2[ni][nj]==0:continue
                        grid2[ni][nj]=0
                        if grid1[ni][nj]==0:f=0
                        if ni>0 and grid2[ni-1][nj]:q.append((ni-1,nj))
                        if ni<m-1 and grid2[ni+1][nj]:q.append((ni+1,nj))
                        if nj>0 and grid2[ni][nj-1]:q.append((ni,nj-1))
                        if nj<n-1 and grid2[ni][nj+1]:q.append((ni,nj+1))
                    if f:ans+=1
        return ans