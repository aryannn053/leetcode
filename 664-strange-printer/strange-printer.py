class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[n] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0
        for length in range(1, n):
            for left in range(n - length):
                right = left + length
                j = -1
                it = range(left, right)
                for i in it:
                    if s[i] != s[right]:
                        j = i
                        test = 1 + dp[j][i] + dp[i + 1][right]
                        if test < dp[left][right]:
                            dp[left][right] = test
                        break
                else:
                    dp[left][right] = 0
                for i in it:
                    test = 1 + dp[j][i] + dp[i + 1][right]
                    if test < dp[left][right]:
                        dp[left][right] = test
        return dp[0][n - 1] + 1