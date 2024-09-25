class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        k=defaultdict(int)
        ans=[]
        for i in words:
            for j in range(len(i)):
                k[i[0:j+1]]+=1
        for i in words:
            temp=0
            for j in range(len(i)):
                temp+=k[i[0:j+1]]
            ans.append(temp)
        return ans