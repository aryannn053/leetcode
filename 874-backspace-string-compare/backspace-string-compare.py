class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []

        for i in s:
            if i == "#":
                if len(s_stack) > 0:
                    s_stack.pop()
            else:
                s_stack.append(i)
        
        for i in t:
            if i == "#":
                if len(t_stack) > 0:
                    t_stack.pop()
            else:
                t_stack.append(i)
        
        print(s_stack, t_stack)
        return s_stack == t_stack