class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        n = [i for i in range(0,n)]

        ball = n[0]
        j = 1

        rev = False

        for i in range(k):
            if rev:
                ball = n[j]
                j -= 1
            else:
                ball = n[j]
                j += 1
            
            if j == len(n):
                rev = True
                j = len(n)-2
            
            if j == 0 and rev:
                rev = False
        
        return ball