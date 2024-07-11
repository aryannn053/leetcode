class Solution:
    def reverseParentheses(self, s: str) -> str:
        self.stack = []
        s = list(s)
        
        for i in range(len(s)):
            if s[i] == '(':
                self.stack.append(i)
            elif s[i] == ')':
                j = self.stack.pop()
                s[j:i+1] = s[j:i+1][::-1]
        
        result = ''.join([char for char in s if char not in '()'])
        return result