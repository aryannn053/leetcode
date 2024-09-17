class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        ans = k % sum(chalk) 
        for i in range(len(chalk)):
            ans -= chalk[i]
            if ans < 0:
                return i