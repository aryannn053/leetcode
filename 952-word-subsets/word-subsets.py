class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        need = Counter()
        for word in words2:
            need |= Counter(word)
        result = []
        for word in words1:
            if not (need - Counter(word)):
                result.append(word)

        return result