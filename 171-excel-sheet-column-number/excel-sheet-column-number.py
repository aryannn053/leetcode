class Solution:
    def titleToNumber(self, c: str) -> int:
        i = 0
        num = 0
        while i<len(c):
            num = num*26
            num += (ord(c[i])-ord('A'))+1
            i+=1
        return num