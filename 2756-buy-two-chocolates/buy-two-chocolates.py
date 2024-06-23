class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()

        for i in range(1, len(prices)):
            if (prices[i-1]+prices[i]) <= money:
                return money-(prices[i-1]+prices[i])
        
        return money