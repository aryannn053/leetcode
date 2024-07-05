class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        current_tank, start = 0, 0

        for index, amount, in enumerate(gas):
            current_tank += amount-cost[index]

            if current_tank < 0:
                start = index + 1
                current_tank = 0
        
        return start