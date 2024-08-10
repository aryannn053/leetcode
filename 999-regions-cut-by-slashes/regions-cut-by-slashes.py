class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        memo = {}
        def find(node: List[int]) -> List[int]:
            if node not in memo:
                memo[node] = node
                return node
            if memo[node] != node: 
                memo[node] = find(memo[node])
            return memo[node]

        def union(node1, node2):
            root1, root2 = find(node1), find(node2)
            memo[root1] = root2
        
        rows, cols = len(grid), len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "/" :
                    union((row,col,0), (row,col,1))
                    union((row,col,2), (row,col,3))
                elif grid[row][col] == "\\":
                    union((row,col,0), (row,col,3))
                    union((row,col,2), (row,col,1))
                else:
                    union((row,col,0), (row,col,1))
                    union((row,col,1), (row,col,2))
                    union((row,col,2), (row,col,3))
        
        for row in range(rows):
            for col in range(cols):
                if col+1 < cols:
                    union((row,col,3),(row,col+1,1))
                if row+1 < rows:
                    union((row,col,2),(row+1,col,0))
        
        roots = set()
        for row in range(rows):
            for col in range(cols):
                roots.add(find((row,col,0)))
                roots.add(find((row,col,1)))
                roots.add(find((row,col,2)))
                roots.add(find((row,col,3)))
        return len(roots)
        