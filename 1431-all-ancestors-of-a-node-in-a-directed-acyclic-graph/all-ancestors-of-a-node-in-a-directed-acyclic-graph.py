class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        res = [set() for _ in range(n)]
        indeg = [0] * n
        adj = collections.defaultdict(list)
        
        for u, v in edges:
            adj[u].append(v)
            indeg[v] += 1
        
        q = deque(i for i in range(n) if indeg[i] == 0)
        
        while q:
            node = q.popleft()
            for nei in adj[node]:
                res[nei].update(res[node], [node])
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
        
        return [sorted(lst) for lst in res]