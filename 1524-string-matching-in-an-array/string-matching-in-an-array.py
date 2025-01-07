class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        n = len(words)
        res = []
        for i in range(n):
            w1 = words[i]
            for j in range(i+1, n):
                w2 = words[j]
                if w1 in w2 and w1 not in res:
                    res.append(w1)
                    break
                elif w2 in w1 and w2 not in res:
                    res.append(w2)
                
        return res