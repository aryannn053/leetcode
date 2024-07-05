class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ['A','E','O','U','I','a','e','i','o','u']

        consonants = []
        vowels_l = []

        for i in range(len(s)):
            if s[i] not in vowels:
                consonants.append(s[i])
            else:
                vowels_l.append(s[i])
        
        vowels_l.sort()

        idx = 0
        s = [*s]

        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = vowels_l[idx]
                idx += 1
        
        return ''.join(s)