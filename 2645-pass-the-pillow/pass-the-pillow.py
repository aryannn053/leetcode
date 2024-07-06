class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        flag = False
        pillow = 0

        for i in range(time):
            if flag == True:
                pillow -= 1
            else:
                pillow += 1
            
            if pillow == 1:
                flag = False

            if pillow == n:
                flag = True
        
        if flag:
            return pillow-1
        return pillow + 1