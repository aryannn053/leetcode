class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        length=max(max(candidates)+1,target+1)
        dp=[[] for i in range(length)]
        for num in candidates:
            dp[num].append([num])
            for i in range(num,length):
                dp[i]=[j+[num] for j in dp[i-num]]+dp[i]
        return dp[target]