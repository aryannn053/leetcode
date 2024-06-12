class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        def calculate(arr):
            for i in range(1, len(arr)):
                arr[i] = arr[i]+arr[i-1]
            return arr

        dp = [1] * n

        for i in range(k):
            dp = calculate(dp)
        
        return dp[-1]%1000000007