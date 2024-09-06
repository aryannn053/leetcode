class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        
        prob = {}

        for i in range(len(edges)):
            if edges[i][0] not in prob:
                prob[edges[i][0]] = { edges[i][1]:succProb[i] }
            else:
                prob[edges[i][0]][edges[i][1]] = succProb[i]
            if edges[i][1] not in prob:
                prob[edges[i][1]] = { edges[i][0]:succProb[i] }
            else:
                prob[edges[i][1]][edges[i][0]] = succProb[i]

        highest = set()
        maxHeap = []
        heapq.heappush(maxHeap,(1,start))

        while maxHeap:

            k=heapq.heappop(maxHeap)
            if k[1] in highest:
                continue

            if k[1] == end:
                return k[0]*-1

            highest.add(k[1])
        
            if prob.get(k[1]):
                for n,p in prob[k[1]].items():
                    if k[1]==start:
                        heapq.heappush(maxHeap,(-1*p,n))
                    elif n not in highest:
                        heapq.heappush(maxHeap,(k[0]*p,n))
        

        return 0