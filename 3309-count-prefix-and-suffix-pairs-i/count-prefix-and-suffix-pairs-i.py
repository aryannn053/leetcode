class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(prefix, word):
            n1 = len(prefix)
            n2 = len(word)
            if n1 > n2:
                return False

            return prefix == word[:n1] and prefix == word[-n1:]
        
        n = len(words)
        cnt = 0
        for i in range(n-1):
            for j in range(i+1, n):
                if i != j and isPrefixAndSuffix(words[i], words[j]) == True:
                    cnt += 1
        
        return cnt