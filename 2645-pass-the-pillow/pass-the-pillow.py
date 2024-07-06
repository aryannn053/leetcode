class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        flag = False
        curr = 0

        for i in range(time):
            if flag:
                curr -= 1
            else:
                curr += 1
            
            if curr == 1:
                flag = False
            
            if curr == n:
                flag = True
        
        if flag:
            return curr - 1
        return curr + 1