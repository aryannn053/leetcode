class Solution:
    def minSteps(self, n: int) -> int:
        prime,cur = [],2
        while cur<500:
            for j in prime:
                if not cur%j:
                    cur+=1
                    continue
                if j**2>cur:
                    break
            prime.append(cur)
            cur+=1
        res = 0
        for j in prime:
            while not n%j:
                n//=j
                res+=j
            if n==1:
                break
        else:
            return n
        return res