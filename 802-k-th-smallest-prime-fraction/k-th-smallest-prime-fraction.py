class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        fractions = []
        
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                fractions.append((arr[i] / arr[j], [arr[i], arr[j]]))
        
        fractions.sort(key=lambda x: x[0])
        
        return fractions[k-1][1]