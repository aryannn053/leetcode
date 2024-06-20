class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner1={}
        winner2={}

        num2={}
        for ma in matches:
            num2[ma[1]]=num2.get(ma[1],0)+1
        for ma in matches:
            if ma[0] not in num2 and ma[0] not in winner1 :
                winner1[ma[0]]=1
            if ma[0] in num2 and num2[ma[0]]==1  and ma[0] not in winner2 :
                winner2[ma[0]]=1
            if ma[1] in num2 and num2[ma[1]]==1 and ma[1] not in winner2:
                winner2[ma[1]]=1
            
            
        return [sorted(winner1.keys()),sorted(winner2.keys())]