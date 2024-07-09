class Solution:
    def validStrings(self, n: int) -> List[str]:
        answ,stack = [],['0','1']
        while stack:
            s=stack.pop()
            if len(s)==n:
                answ.append(s)
            else:
                if s[-1]=='1':
                    stack.append(s+'0')
                stack.append(s+'1')
        return answ