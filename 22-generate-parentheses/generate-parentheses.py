class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(s,open_count,close_count):
            if len(s)==2*n:
                res.append(''.join(s))
                return
            
            if open_count < n:
                s.append('(')
                backtrack(s,open_count+1,close_count)
                s.pop()
            
            if open_count > close_count:
                s.append(')')
                backtrack(s,open_count,close_count+1)
                s.pop()
        
        backtrack([],0,0)
        return res