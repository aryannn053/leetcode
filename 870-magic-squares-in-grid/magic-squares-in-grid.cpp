class Solution {
public:
    int numMagicSquaresInside(vector<vector<int>>& grid) {
        if(grid.size()<3) return 0;
        if(grid[0].size()<3) return 0;
        int cnt=0;
        for(int i=1;i<grid.size()-1;i++){
            for(int j=1;j<grid[i].size()-1;j++){
                if(grid[i][j]==5){
                    set<int> s;
                    for(int x=i-1;x<=i+1;x++){
                        for(int y=j-1;y<=j+1;y++){
                            if(grid[x][y]<=9&&grid[x][y]>0) s.insert(grid[x][y]);
                        }
                    }
                    if(s.size()==9)
                    if((grid[i-1][j-1]+grid[i-1][j]+grid[i-1][j+1])==15&&
                    (grid[i][j-1]+grid[i][j]+grid[i][j+1])==15&&
                    (grid[i+1][j-1]+grid[i+1][j]+grid[i+1][j+1])==15&&
                    (grid[i-1][j-1]+grid[i][j]+grid[i+1][j+1])==15&&
                    (grid[i+1][j-1]+grid[i][j]+grid[i-1][j+1])==15&&
                    (grid[i-1][j-1]+grid[i][j-1]+grid[i+1][j-1])==15&&
                    (grid[i-1][j]+grid[i][j]+grid[i+1][j])==15&&
                    (grid[i-1][j+1]+grid[i][j+1]+grid[i+1][j+1])==15) cnt++;
                }
            }
        }
        return cnt;

        
    }
};