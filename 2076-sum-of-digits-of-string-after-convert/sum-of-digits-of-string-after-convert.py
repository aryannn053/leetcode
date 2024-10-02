class Solution:
    def getLucky(self, s: str, k: int) -> int:
        l = string.ascii_lowercase
        s = list(s)

        for i in range(len(s)):
            s[i] = str(l.index(s[i])+1)
        
        s = ''.join(s)
        ans = s
        
        for i in range(k):
            x = 0
            for i in ans:
                x += int(i)
            ans = str(x)
        
        return int(ans)