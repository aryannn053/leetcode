class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        g = defaultdict(list)
        gd = defaultdict(int)
        for i, j in pairs:
            g[i].append(j)
            gd[i] += 1
            gd[j] -= 1

        start, end = pairs[0][0], pairs[0][0]
        for k,v in gd.items():
            if v == 1:
                start = k
            if v == -1:
                end = k

        path = []
        def dfs(node):
            while g[node]:
                next = g[node].pop()
                dfs(next)
                path.append([node, next])
        dfs(start)
        return path[::-1]