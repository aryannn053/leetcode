class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        ans = 0
        adj = defaultdict(list)
        
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        def dfs(x, p):
            nonlocal ans
            res = values[x]
            for v in adj[x]:
                if v != p:
                    res += dfs(v, x)
            
            if res % k == 0:
                ans += 1
                res = 0
            
            return res
        
        dfs(0, -1)
        return ans