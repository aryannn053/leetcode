class DSU:
    def __init__(self, num):
        self.parents = [-1] * (num + 1)
        
    def findParent(self, i):
        if self.parents[i] < 0:
            return i
        
        else:
            self.parents[i] = self.findParent(self.parents[i])
            
        return self.parents[i]
    
    def union(self, i, j):
        iParent = self.findParent(i)
        jParent = self.findParent(j)
        
        if iParent == jParent:
            return False
        
        if abs(self.parents[iParent]) >= abs(self.parents[jParent]):
            self.parents[iParent] += self.parents[jParent]
            self.parents[jParent] = iParent
            
        else:
            self.parents[jParent] += self.parents[iParent]
            self.parents[iParent] = jParent
            
        return True

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice = DSU(n)
        bob = DSU(n)
        
        onlyAlice = []
        onlyBob = []
        both = []
        
        for x, y, z in edges:
            if x == 1:
                onlyAlice.append([y, z])
                
            elif x == 2:
                onlyBob.append([y, z])
                
            else:
                both.append([y, z])
                
        ans = 0
        
        for x, y in both:
            case1 = alice.union(x, y)
            case2 = bob.union(x, y)
            
            if not case1 and not case2:
                ans += 1
                
        for x, y in onlyAlice:
            if not alice.union(x, y):
                ans += 1
                
        for x, y in onlyBob:
            if not bob.union(x, y):
                ans += 1
            
        #print(alice.parents)
        #print(bob.parents)
        
        cnt = 0
        for elem in alice.parents[1:]:
            if elem < 0:
                cnt += 1
                
            if cnt > 1:
                return -1
        
        cnt = 0
        for elem in bob.parents[1:]:
            if elem < 0:
                cnt += 1
                
            if cnt > 1:
                return -1
        
        return ans