class Solution:
    def equalFrequency(self, word: str) -> bool:
        word = sorted(list(Counter(word).values()),reverse=True)
        for i in range(len(word)):
            temp=word.copy()
            temp[i]-=1
            temp = [i for i in temp if i>0]
            if len(set(temp))==1:
                return True
                break
        return False