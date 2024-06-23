class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]

        for num in range(1, int(sqrt(n)) + 1):
            if num * num > n:
                continue

            square = num * num
            for targetIdx in range(1, n + 1):
                if targetIdx % square == 0:
                    dp[targetIdx] = targetIdx // square
                else:
                    dp[targetIdx] = min((targetIdx // square) + dp[targetIdx%square], dp[targetIdx])

        return dp[-1]