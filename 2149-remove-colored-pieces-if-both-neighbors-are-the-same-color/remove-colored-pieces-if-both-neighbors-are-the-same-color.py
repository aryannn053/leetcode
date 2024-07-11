class Solution:
    def winnerOfGame(self, colors: str) -> bool:

        num_A=num_B=0
        l=0
        while l < len(colors):
            r=l
            while r<len(colors) and colors[r]==colors[l]:
                if r-l+1>=3:
                    if colors[l]=="A":
                        num_A+= 1
                    else:
                        num_B+= 1
                r+=1
            
            l=r

        return num_A>num_B