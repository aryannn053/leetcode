class Solution:
    def similarPairs(self, words: List[str]) -> int:
        def fuq(x, y):
            x = set(x)
            y = set(y)
            uix = x - y
            uiy = y - x
            
            return len(list(uix)) == 0 and len(list(uiy)) == 0

        
        cnt = 0

        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if fuq(words[i], words[j]):
                    cnt += 1
        
        return cnt