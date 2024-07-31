class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        N = len(books)
        dp = [0] * (N + 1)

        for i in range(1, N + 1):
            width = books[i - 1][0]
            height = books[i - 1][1]

            dp[i] = dp[i - 1] + height

            for j in range(i - 1, 0, -1):
                if books[j - 1][0] + width <= shelfWidth:
                    dp[i] = min(dp[i], dp[j - 1] + max(height, books[j - 1][1]))
                else:
                    break

                width += books[j - 1][0]
                height = max(height, books[j - 1][1])
        
        return dp[N]