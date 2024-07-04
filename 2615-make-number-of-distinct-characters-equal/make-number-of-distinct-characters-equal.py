class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        counter1, counter2 = Counter(word1), Counter(word2)
        for char1, count1 in counter1.items():
            for char2, count2 in counter2.items():
                if char1 == char2:
                    if len(counter1) == len(counter2):
                        return True
                else:
                    if len(counter1) + (char2 not in counter1) - (count1 == 1) == len(counter2) + (char1 not in counter2) - (count2 == 1):
                        return True
        return False