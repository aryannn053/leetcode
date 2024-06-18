class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        worker.sort()
        diff_profit = [(0,0)] + sorted(list(zip(difficulty, profit)))

        diff_i, cur_best_profit = 0, 0
        total_profit = 0
        for level in worker:
            while diff_i+1 < len(diff_profit) and diff_profit[diff_i+1][0] <= level:
                cur_best_profit = max(cur_best_profit, diff_profit[diff_i+1][1])
                diff_i += 1
            total_profit += cur_best_profit
        return total_profit