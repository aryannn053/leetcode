class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        n=len(s)
        ss={'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
        for c in s:
            if c in 'aeiou':
                ss[c]+=1
        for i in range(len(s),0,-1):
            if n-i>0 and s[i] in 'aeiou':
                ss[s[i]]-=1
            sss = ss.copy()
            
            if all((value % 2 == 0 or value ==0) for value in ss.values()):
                return i

            for j in range(1,len(s)-i+1):
                if s[j-1] in 'aeiou':
                    sss[s[j-1]]-=1
                if s[j+i-1] in 'aeiou':
                    sss[s[j+i-1]]+=1


                if all((value % 2 == 0 or value ==0) for value in sss.values()):
                    return i
                
        return 0

                    