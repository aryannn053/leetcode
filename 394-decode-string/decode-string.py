class Solution:
    def decodeString(self, s: str) -> str:
        nums = "0123456789"
        stack = []
        for char in s:
            #print(stack)
            if char == ']':
                temp_s = ''
                num=''
                while stack[-1] != '[':
                    temp_s = stack.pop()+temp_s
                stack.pop()
                while stack and stack[-1] in nums:
                    num+= stack.pop()
                num = int(num[::-1])
                while num:
                    stack.append(temp_s)
                    num-=1
            else:
                stack.append(char)
        l = "".join(map(str,stack))
        return l