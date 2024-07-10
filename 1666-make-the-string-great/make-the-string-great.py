class Solution:
    def makeGood(self, s: str) -> str:
        
        while True:
            i=0
            f=0
            while i<len(s)-1:
                if (s[i].upper()==s[i+1] or s[i]==s[i+1].upper()) and s[i]!=s[i+1]:
                        s=s.replace(s[i]+s[i+1],"")
                        i+=2
                        f=1
                else:
                    i+=1
            if f==0:
                return s