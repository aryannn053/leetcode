class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if n == '11' or n == '10':
            return '9'

        l = len(n)
        if l % 2 == 0:
            half = l//2
        else: 
            half = l//2 + 1
        
        def palindromise(s):
            revers = s[0:l - half][::-1]
            if len(s) < l - half:
                return s + s[-1] + revers
            return s + revers

        halfValue = int(n[0:half])
        up = str(halfValue + 1)
        mid = str(halfValue)
        down = str(halfValue - 1)

        up_p = palindromise(up)
        mid_p = palindromise(mid)
        down_p = palindromise(down)
 
        dif_up = int(up_p) - int(n)
        dif_mid = abs(int(mid_p) - int(n))
        dif_down = int(n) - int(down_p)
 
        if dif_mid != 0:
            if dif_mid <= dif_up and dif_mid < dif_down:
                return mid_p
        if dif_down > dif_up:
            return up_p
        else:
            return down_p