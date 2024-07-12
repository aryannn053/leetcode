class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        total, value, sign = 0, 0, 1

        for i, c in enumerate(s):
            if c.isdigit():
                value = value*10 + int(c)
            elif c in '+-':
                total += sign * value
                value = 0
                sign = 1 if c == '+' else -1
            elif c == '(':
                stack.append(total)
                stack.append(sign)
                sign = 1
                total = 0
            elif c == ')':
                total += sign * value
                value = 0
                total *= stack.pop()
                total += stack.pop()
        
        total += sign * value

        return total
            