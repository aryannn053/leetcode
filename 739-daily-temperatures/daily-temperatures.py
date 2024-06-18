class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        stack =[]

        for i in range(n):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                prev_index = stack.pop()
                res[prev_index]= i -prev_index
            
            stack.append(i)
        return res