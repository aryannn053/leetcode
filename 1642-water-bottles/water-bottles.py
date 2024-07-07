class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles

        while numBottles >= numExchange:
            # numBottles: 6, nuMExchange: 4
            newBottles = numBottles // numExchange
            # 1

            ans += newBottles
            # 15 + 3 + 1 = 19

            numBottles = newBottles + numBottles % numExchange
            # numBottles = 3

        # 15 + 3 + 1 = 19
        return ans