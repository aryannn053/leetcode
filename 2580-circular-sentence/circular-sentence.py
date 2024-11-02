class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]:
            return False
        sentence = sentence.split(" ")
        for i in range(len(sentence)-1):
            s1 = sentence[i]
            s2 = sentence[i+1]
            if s1[-1] != s2[0]:
                return False
        return True